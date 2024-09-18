from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Hardcoded user credentials for demonstration
users = {
    "student1": "kira123",
    "student2": "password456",
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def validate_login():
    username = request.form['username']
    password = request.form['password']

    # Check if the credentials are correct
    if users.get(username) == password:
        return redirect(f'/dashboard/{username}')
    else:
        return "Invalid login. Please try again."

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
