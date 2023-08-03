# Importar el módulo random para generar números aleatorios
import random

class Tragamonedas:
    def __init__(self):
        self.simbolos = ["🍒", "🍋", "🍇", "🍊", "🔔", "⭐", "7️⃣"]
        self.premios = {
        "🍒": 10,
        "🍋": 20,
        "🍇": 30,
        "🍊": 40,
        "🔔": 50,
        "⭐": 75,
        "7️⃣": 100,
        }
    # Definir una función para simular el giro de los rodillos
    def girar_rodillos(self):
        # Elegir tres símbolos al azar y guardarlos en una lista
        resultado = random.choices(self.simbolos, k=3)
        # Devolver la lista como resultado del giro
        return resultado

    # Definir una función para calcular el premio según el resultado del giro
    def calcular_premio(self, resultado):
        # Inicializar el premio en cero
        premio = 0
        # Si los tres símbolos son iguales, asignar un premio según el símbolo
        if resultado[0] == resultado[1] == resultado[2]:
            print(f"{resultado[0]} {resultado[1]} {resultado[2]}")
            simbolo = resultado[0]
            premio = self.premios[simbolo]
        
        for simbolo in resultado:
            if resultado.count(simbolo) == 2:
                premio = self.premios[simbolo] // 2
                break
            
        # Devolver el premio como resultado de la función
        return premio

# Definir una función para simular el juego de la máquina tragamonedas
def jugar_tragamonedas():
    tragamonedas = Tragamonedas()
    saldo = 100
    giro = 10
    while saldo >= giro:
        input("Presione Enter para girar: ")
        saldo -= giro
        resultado = tragamonedas.girar_rodillos()
        premio = tragamonedas.calcular_premio(resultado)
        saldo += premio
        print(f"Has ganado {premio} y tu saldo actual es {saldo}.")

    else:
        print("No tienes más saldo para jugar. Fin del juego.")


if __name__ == '__main__':
    jugar_tragamonedas()
