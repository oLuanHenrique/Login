from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Implementar lógica de login aqui
    return f'Login: {username}, {password}'

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        new_username = request.form['newUsername']
        new_password = request.form['newPassword']
        # Implementar lógica de cadastro aqui
        return f'Cadastro: {new_username}, {new_password}'
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
