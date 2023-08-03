from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from juego import Tragamonedas

# Configuraciones
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/walke/OneDrive/Documentos/CodoaCodo/back-end-python/maquina/datos.db'
db = SQLAlchemy(app)

# Tabla de base de datos
class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, default=100, nullable=False)
    

with app.app_context():
    db.create_all()

juego = Tragamonedas()

@app.route('/')
def index():
    return render_template('index.html')

# Ruta del juego
@app.route('/juego', methods=['GET', 'POST'])
def play_game():

    player = Player.query.first()
    if request.method == 'POST':

        if player.balance >= 10:
            # Procesar un giro
            resultado = juego.girar_rodillos()
            premio = juego.calcular_premio(resultado)

            # Actualizar saldo del jugador
            player.balance -= 10
            if premio > 0: player.balance += premio
            db.session.commit()

            return render_template('juego.html', resultado=resultado, premio=premio, balance=player.balance, premios=juego.premios)
        else:
            return redirect(url_for('index'))
        
    else:
        player.balance = 10
        db.session.commit()
        return render_template('juego.html', balance=player.balance, premios=juego.premios)
    
if __name__ == '__main__':
    app.run(debug=True)