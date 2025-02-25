YouTube Video Downloader

A simple Python script to download YouTube videos in different resolutions using yt-dlp.

Features

Choose from 720p, 1080p, 2K, or 4K video quality.

Automatically selects the best available format for the chosen resolution.

Merges video and audio into a single MP4 file.

Requirements

Make sure you have the following installed:

Python 3.x (Download Here)

yt-dlp (YouTube downloader tool)

FFmpeg (for merging video and audio)

Installation

Install yt-dlp:

pip install yt-dlp

Install FFmpeg:

Windows: Download FFmpeg and add it to your system PATH.

Mac: Install via Homebrew:

brew install ffmpeg

Linux: Install using apt or yum:

sudo apt install ffmpeg  # Debian/Ubuntu
sudo yum install ffmpeg  # CentOS/RHEL

Usage

Run the script:

python youtube_downloader.py

Enter the YouTube video URL when prompted.

Choose a video quality by entering a number:

1️⃣  720p
2️⃣  1080p
3️⃣  2K
4️⃣  4K

The video will start downloading, and the final MP4 file will be saved in the downloads/ folder.

Example Run

Enter YouTube Video URL: https://www.youtube.com/watch?v=EXAMPLE_ID

Select Video Quality:
1️⃣  720p
2️⃣  1080p
3️⃣  2K
4️⃣  4K

Enter your choice (1-4): 2

Downloading in 1080p... Please wait!
Download Complete! ✅

Troubleshooting

If you see an error related to yt-dlp, update it:

yt-dlp -U

If downloads are slow or fail, try using a VPN or updating FFmpeg.
