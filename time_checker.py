from flask import Flask, request, jsonify
from face_detector import detect_face
from time_checker import check_time
import random

app = Flask(__name__)

responses = {
    "on_time": [
        "มาตรงเวลาสุดยอด!", "นาฬิกาตายหรือเปล่าเนี่ย!", "ตรงเป๊ะเลยนะวันนี้!",
        "เหลือเชื่อ! วันนี้มาไว!", "เช็คดูสิว่านี่คือโลกความจริงหรือเปล่า?",
        "พระอาทิตย์ยังไม่ขึ้นเลยนะ!", "มาเช้าขนาดนี้จะเอารางวัลไหม?",
        "ใครจ้างคุณให้มาตรงเวลาวันนี้?", "ต้องบันทึกประวัติศาสตร์!",
        "ครั้งแรกในรอบปีที่คุณมาตรงเวลา!", "ดีใจที่ยังมีคนตรงเวลาอยู่!",
        "ให้รางวัลตัวเองได้เลย!", "นี่ใช่คุณจริง ๆ หรือเปล่า?",
        "สงสัยดาวเคราะห์จะเรียงตัวพอดี!", "โอ้โห! ปาฏิหาริย์มีจริง!",
        "คุณต้องตั้งปลุกสักสิบรอบแน่ ๆ!", "ฉันไม่อยากเชื่อสายตาตัวเอง!",
        "นี่คุณหุ่นยนต์หรือเปล่า?", "วันนี้โลกต้องจารึก!",
        "โชคดีที่ได้เห็นวันนี้!", "พลังงานบางอย่างผลักดันคุณมาแน่นอน!",
        "รู้ไหมว่าคุณมาตรงเวลากว่าหัวหน้าอีก!", "สาบานว่านี่ไม่ใช่ความฝัน?",
        "แปลกใจที่คุณไม่มาก่อนพระอาทิตย์ขึ้น!", "ยังไม่ถึงวันสิ้นโลกใช่ไหม?",
        "ใครไปสะกิดคุณให้รีบตื่น?", "หรือคุณมีแฝดที่ตรงเวลากว่า?"
    ],
    "late": [
        "สายอีกแล้วนะ!", "แก้ตัวว่าอะไรดีล่ะวันนี้?", "เช้าไปไหมสำหรับการมาทำงาน?",
        "นาฬิกาคุณเดินช้ากว่าชาวบ้านหรือไง?", "นี่คุณแวะไปทัวร์โลกมาก่อนหรือเปล่า?",
        "รอคุณจนดอกไม้เหี่ยวเลย!", "บริษัทเปลี่ยนเวลาเข้างานแล้วเหรอ?",
        "คุณมาตามเวลาไทยหรือตามเวลามิติอื่น?", "โอ้โห! นึกว่าจะไม่มาแล้ว!",
        "ถ้ามีแข่งมาสาย คุณต้องได้ที่หนึ่งแน่ ๆ!", "คุณกำลังสร้างสถิติใหม่ใช่ไหม?",
        "ถ้าคุณเป็นรถไฟ คงโดนโวยแล้ว!", "นาฬิกาปลุกคุณมีไว้ประดับเหรอ?",
        "แถวนี้ไม่มีรถติดเลยนะ!", "คุณออกเดินทางเมื่อไหร่ บ่ายเมื่อวานเหรอ?",
        "ที่บ้านคุณมีไทม์โซนของตัวเองหรือเปล่า?", "ทำไมต้องมาสายทุกวันเลยนะ!",
        "แบบนี้ต้องจองโต๊ะสายเป็นประจำให้เลยไหม?", "สงสัยต้องเปลี่ยนชื่อคุณเป็น Mr. สาย!",
        "ถ้าสายเป็นกีฬา คุณคงเป็นแชมป์แล้ว!", "วันนี้ไม่ใช่วันหยุดนะรู้ตัวไหม?",
        "อย่าบอกนะว่า UFO ลักพาตัวคุณไปก่อนมา!", "คนอื่นเลิกงานกันแล้ว คุณพึ่งมา!",
        "ทายสิว่าใครมาสายอีกแล้ว?", "คุณนี่แหละตัวจริงแห่งการมาสาย!",
        "ถ้าการมาสายเป็นอาชีพ คุณคงรวยไปแล้ว!", "แบบนี้ต้องให้รางวัล 'มาสายแห่งปี'!"
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
