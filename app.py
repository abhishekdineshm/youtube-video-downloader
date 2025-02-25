from flask import Flask, request, render_template, jsonify, send_file
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

QUALITY_MAP = {
    "1": ("720p", "bestvideo[height<=720]+bestaudio/best"),
    "2": ("1080p", "bestvideo[height<=1080]+bestaudio/best"),
    "3": ("2K", "bestvideo[height<=1440]+bestaudio/best"),
    "4": ("4K", "bestvideo[height<=2160]+bestaudio/best"),
}

progress = {"status": "idle", "percent": 0, "filename": ""}

def progress_hook(d):
    """Updates the global progress variable to track download progress."""
    if d["status"] == "downloading":
        progress["status"] = "downloading"
        progress["percent"] = d.get("_percent_str", "0%").strip()
    elif d["status"] == "finished":
        progress["status"] = "finished"
        progress["filename"] = d["filename"]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    global progress
    url = request.json["url"]
    quality = request.json["quality"]
    
    progress = {"status": "downloading", "percent": "0%", "filename": ""}
    quality_name, format_choice = QUALITY_MAP.get(quality, ("best", "best"))
    output_template = os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s")

    ydl_opts = {
        "outtmpl": output_template,
        "format": format_choice,
        "merge_output_format": "mp4",
        "progress_hooks": [progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return jsonify({"status": "completed", "filename": progress["filename"]})

@app.route("/progress", methods=["GET"])
def get_progress():
    return jsonify(progress)

@app.route("/download_file", methods=["GET"])
def download_file():
    if progress["status"] == "finished" and progress["filename"]:
        return send_file(progress["filename"], as_attachment=True)
    return "No file available", 404

if __name__ == "__main__":
    app.run(debug=True)
