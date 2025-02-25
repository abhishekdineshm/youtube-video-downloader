import yt_dlp

# Mapping option numbers to quality settings
QUALITY_MAP = {
    "1": ("720p", "bestvideo[height<=720]+bestaudio/best"),
    "2": ("1080p", "bestvideo[height<=1080]+bestaudio/best"),
    "3": ("2K", "bestvideo[height<=1440]+bestaudio/best"),
    "4": ("4K", "bestvideo[height<=2160]+bestaudio/best")
}

def download_video(url, quality_option, output_path="downloads"):
    """Downloads YouTube video in the selected quality."""
    quality_name, format_choice = QUALITY_MAP.get(quality_option, ("best", "best"))

    ydl_opts = {
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "format": format_choice,
        "merge_output_format": "mp4",
    }

    print(f"\nDownloading in {quality_name}... Please wait!")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("\nDownload Complete! ✅")

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
