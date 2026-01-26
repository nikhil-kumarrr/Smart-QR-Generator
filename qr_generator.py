import qrcode
import os

def generate_qr(data):
    # Output folder create agar na ho
    os.makedirs("output", exist_ok=True)

    # QR generate
    qr = qrcode.make(data)
    path = "output/qr.png"
    qr.save(path)

    return path
