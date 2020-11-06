from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    message = "Salut Timmy !"
    return message

if __name__ == '__main__':
    app.run(debug=True)