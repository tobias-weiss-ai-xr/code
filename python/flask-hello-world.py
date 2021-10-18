# https://blog.tanka.la/2020/02/20/debug-your-flaskpython-web-application-using-visual-studio-code/
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(port=1234, threaded=True)