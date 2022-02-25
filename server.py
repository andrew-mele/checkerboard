from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def board():
    return render_template('index.html', across = 8, down = 8, color1 = 'red', color2='black')

@app.route('/<int:num>')
def board2(num):
    return render_template('index.html', across = num, down=8, color1 ='red', color2='black')


@app.route('/<int:num>/<int:num2>')
def board3(num, num2):
    return render_template('index.html', across = num, down = num2, color1='red', color2='black')

@app.route('/<int:num>/<int:num2>/<string:one>')
def board4(num, num2, one):
    return render_template('index.html', across = num, down = num2, color1= one, color2='black')

@app.route('/<int:num>/<int:num2>/<string:one>/<string:two>')
def board5(num, num2, one, two):
    return render_template('index.html', across = num, down = num2, color1= one, color2= two)

if __name__=="__main__":
    app.run(debug=True)