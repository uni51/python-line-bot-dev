from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return request.args.get("param", "paramで表示したい値を入力してください。")


if __name__ == "__main__":
    app.run()