#Импорт
from flask import (
    Flask, 
    render_template
)

def result_calculate(size: int, lights: int, device: int):
    #Переменные для энергозатратности приборов
    home_coef: int = 100
    light_coef: float = 0.04
    devices_coef: int = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 


def make_app() -> Flask:
    
    app: Flask = Flask(__name__)

    #Первая страница
    @app.route('/')
    def index():
        return render_template('index.html')

    #Вторая страница
    @app.route('/<int:size>')
    def lights(size):
        return render_template(
            'lights.html', 
            size = size
        )

    #Третья страница
    @app.route('/<int:size>/<int:lights>')
    def electronics(size: int, lights: int):
        return render_template(
            'electronics.html',
            size = size, 
            lights = lights                           
        )

    #Расчет
    @app.route('/<int:size>/<int:lights>/<int:device>')
    def end(size: int, lights: int, device: int):
        return render_template('end.html', 
            result=result_calculate(
                size,
                lights, 
                device
            )
        )

    return app
