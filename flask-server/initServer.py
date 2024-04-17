from flask import Flask

app = Flask(__name__)


@app.route('/')
def content():
    return "Server is up"

if __name__ == '__main__':
    app.run(port=8001)