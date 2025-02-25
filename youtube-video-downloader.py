import yt_dlp
import os
import subprocess

# Mapping option numbers to quality settings
QUALITY_MAP = {
    "1": ("720p", "bestvideo[height<=720]+bestaudio/best"),
    "2": ("1080p", "bestvideo[height<=1080]+bestaudio/best"),
    "3": ("2K", "bestvideo[height<=1440]+bestaudio/best"),
    "4": ("4K", "bestvideo[height<=2160]+bestaudio/best")
}

def open_download_folder(path):
    """Opens the download folder where the video is saved."""
    if os.name == "nt":  # Windows
        subprocess.run(["explorer", path], shell=True)
    elif os.uname().sysname == "Darwin":  # macOS
        subprocess.run(["open", path])
    else:  # Linux
        subprocess.run(["xdg-open", path])

def download_video(url, quality_option, output_path="downloads"):
    """Downloads YouTube video in the selected quality and opens the folder."""
    quality_name, format_choice = QUALITY_MAP.get(quality_option, ("best", "best"))

    # Ensure the download directory exists
    os.makedirs(output_path, exist_ok=True)

    # Define output template
    output_template = os.path.join(output_path, "%(title)s.%(ext)s")

    ydl_opts = {
        "outtmpl": output_template,
        "format": format_choice,
        "merge_output_format": "mp4",
    }

    print(f"\nDownloading in {quality_name}... Please wait!")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\nDownload Complete! ✅")

    # Convert folder path to absolute and open it
    abs_folder_path = os.path.abspath(output_path)
    print(f"\n📂 Your videos are saved in: {abs_folder_path}")

    # Open the folder containing the videos
    open_download_folder(abs_folder_path)

if __name__ == "__main__":
    video_url = input("\nEnter YouTube Video URL: ")

    print("\nSelect Video Quality:")
    print("1️⃣  720p")
    print("2️⃣  1080p")
    print("3️⃣  2K")
    print("4️⃣  4K")

    quality_choice = input("\nEnter your choice (1-4): ").strip()

    if quality_choice in QUALITY_MAP:
        download_video(video_url, quality_choice)
    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 4.")
