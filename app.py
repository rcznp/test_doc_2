###recieves voice recordings from watch
# pip instal flask first,then just run "python app.py"
from flask import Flask, request
import os
import time
# from transcription import transcribe_local

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
TRANSCRIPT_FOLDER = "transcripts"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TRANSCRIPT_FOLDER, exist_ok=True)
@app.route("/upload", methods=["POST"])
def upload_audio():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filename = f"audio_{int(time.time())}.3gp"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    print(f"✅ Saved to {filepath}")
    return "File uploaded", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=("cert.pem", "key.pem"))
    # Note: Replace "cert.pem" and "key.pem" with your actual certificate and key file paths.
    #cmd: "openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes"

