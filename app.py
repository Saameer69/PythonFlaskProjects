from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Trying flask for first time ever'

if __name__ == '__main__':
    app.run(debug=True)
