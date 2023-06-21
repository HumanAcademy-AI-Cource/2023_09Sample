#!/usr/bin/env python3

# 必要なライブラリをインポート
from flask import Flask, render_template, jsonify

# Flaskを使用する準備
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# カウントを保持する変数
counter = 0

@app.route("/counter", methods=["GET"])
def count_button():
    """ボタンが押されたら処理させる関数"""
    global counter
    counter = counter + 1
    print("ボタンが押された回数（counter={}）".format(counter))
    return jsonify({"count": counter})
    

@app.route("/")
def main():
    """トップページにアクセスしたときに実行される関数"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)