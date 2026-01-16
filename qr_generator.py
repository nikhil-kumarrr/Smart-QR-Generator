import qrcode
import os

def generate_qr(data):
    os.makedirs("output", exist_ok=True)

    qr = qrcode.make(data)
    path = "output/qr.png"
    qr.save(path)

    return path
