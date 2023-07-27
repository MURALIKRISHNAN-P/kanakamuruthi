from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def function():
    return render_template('index.html')

@app.route('/index.html')
def function1():
    return render_template('index.html')

@app.route('/pipes.html')
def function2():
    return render_template('pipes.html')

@app.route('/other.html')
def function3():
    return render_template('other.html')

@app.route('/traders.html')
def function4():
    return render_template('traders.html')

if __name__ == '__main__':
    app.run(debug=True)