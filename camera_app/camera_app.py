#!/usr/bin/env python3

# 必要なライブラリをインポート
from flask import Flask, render_template, jsonify, send_from_directory
import cv2
import os
import datetime


# Flaskを使用する準備
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route("/shot", methods=["GET"])
def shot():
    """OpenCVで写真撮影する処理"""
    # カメラの準備
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    image = cap.read()[1]
    # ファイル名にタイムスタンプを付与したいで、現在時刻を取得
    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), "JST")).strftime("%Y%m%d_%H%M%S")
    # タイムスタンプを使ってファイル名を決めておく
    filename = "datas/{}.JPG".format(timestamp)

    # 画像データを置く場所が無ければ作成
    if not os.path.isdir("datas"):
        os.makedirs("datas")

    # 画像を保存
    cv2.imwrite(filename, image)
    
    # 保存した画像のファイル名を送り返す
    return jsonify({"photo_name": filename})


@app.route("/")
def main():
    """トップページにアクセスしたときに実行される関数"""
    return render_template("index.html")


@app.route("/datas/<path:name>")
def datas(name):
    """datas/xxx.JPGという形式のURLでファイルをダウンロードできるようにする設定"""
    return send_from_directory("./datas", name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)