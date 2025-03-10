from flask import Flask, request, jsonify
from face_detector import detect_face
from time_checker import check_time
import random

app = Flask(__name__)

responses = {
    "on_time": [
        "มาตรงเวลาสุดยอด!", "นาฬิกาตายหรือเปล่าเนี่ย!", "ตรงเป๊ะเลยนะวันนี้!"
    ],
    "late": [
        "สายอีกแล้วนะ!", "แก้ตัวว่าอะไรดีล่ะวันนี้?", "เช้าไปไหมสำหรับการมาทำงาน?",
        "วันนี้มีอะไรดี ถึงมาสายอีก?", "เดี๋ยวให้รางวัลมาสายดีไหม?",
        "นาฬิกาปลุกเสียเหรอ?", "ทำไมไม่มาให้เช้ากว่านี้?", "อีกนิดจะเป็นกะบ่ายแล้วนะ!",
        "มีใครมาสายกว่านี้ไหมนะ?", "แถมโอทีให้ดีไหมเนี่ย?"
    ]
}

@app.route("/check-in", methods=["POST"])
def check_in():
    file = request.files.get("image")
    username = request.form.get("username")

    if not file or not username:
        return jsonify({"error": "Missing image or username"}), 400

    if not detect_face(file):
        return jsonify({"error": "No face detected"}), 400

    status, timestamp = check_time()
    response_text = random.choice(responses[status])

    return jsonify({
        "user": username,
        "timestamp": timestamp,
        "message": response_text
    })

if __name__ == "__main__":
    app.run(debug=True)
