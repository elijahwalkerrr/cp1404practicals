from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World :)</h1>"

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def c_to_f(celsius):
    return celsius * 9 / 5 + 32


@app.route('/convert/<celsius_value>')
def convert(celsius_value):
    try:
        celsius = float(celsius_value)
        f = c_to_f(celsius)
        return f"{celsius}°C = {f:.2f}°F"
    except ValueError:
        return "Invalid number. Try: /convert/25"


if __name__ == "__main__":
    app.run()