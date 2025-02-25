from flask import Flask, request, render_template, jsonify
import yt_dlp
import os
import subprocess

app = Flask(__name__)

DOWNLOAD_FOLDER = os.path.abspath("downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

QUALITY_MAP = {
    "1": ("720p", "bestvideo[height<=720]+bestaudio/best"),
    "2": ("1080p", "bestvideo[height<=1080]+bestaudio/best"),
    "3": ("2K", "bestvideo[height<=1440]+bestaudio/best"),
    "4": ("4K", "bestvideo[height<=2160]+bestaudio/best"),
}

progress = {"status": "idle", "percent": "0%", "filename": ""}

def progress_hook(d):
    global progress
    if d["status"] == "downloading":
        progress["status"] = "downloading"
        progress["percent"] = d.get("_percent_str", "0%").strip()
    elif d["status"] == "finished":
        progress["status"] = "finished"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    global progress
    url = request.json.get("url")
    quality = request.json.get("quality")

    if not url or not quality:
        return jsonify({"error": "Missing URL or quality selection"}), 400

    print(f"DEBUG: Received Download Request - URL: {url}, Quality: {quality}")

    progress = {"status": "downloading", "percent": "0%", "filename": ""}
    quality_name, format_choice = QUALITY_MAP.get(quality, ("best", "best"))
    output_template = os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s")

    ydl_opts = {
        "outtmpl": output_template,
        "format": format_choice,
        "merge_output_format": "mp4",
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
        "progress_hooks": [progress_hook],
        "verbose": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get("title", "video")
            video_filename = f"{video_title}.mp4"
            video_path = os.path.join(DOWNLOAD_FOLDER, video_filename)
            
            progress["filename"] = video_path if os.path.exists(video_path) else ""
            
            if os.path.exists(video_path):
                subprocess.Popen(["explorer", "/select,", video_path])
    except yt_dlp.utils.DownloadError as e:
        print(f"DEBUG: Error - {str(e)}")
        return jsonify({"error": str(e)}), 500

    return jsonify({"status": "completed", "message": "Download completed successfully."})

@app.route("/progress", methods=["GET"])
def get_progress():
    return jsonify(progress)

if __name__ == "__main__":
    app.run(debug=True)
