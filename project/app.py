from flask import Flask, request, logging

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.warn("hoge")
    return "hoge"

if __name__ == "__main__":
    app.run()