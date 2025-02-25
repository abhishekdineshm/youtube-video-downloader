# **YouTube Video Downloader**

A simple Python script to download YouTube videos in different resolutions using `yt-dlp`.

---

## **🚀 Features**
✅ Choose from **720p, 1080p, 2K, or 4K** video quality.  
✅ Automatically selects the best available format for the chosen resolution.  
✅ Merges video and audio into a single **MP4 file**.  

---

## **📌 Requirements**
Ensure you have the following installed:  

- **Python 3.x** ([Download Here](https://www.python.org/downloads/))  
- **yt-dlp** (YouTube downloader tool)  
- **FFmpeg** (for merging video and audio)  

---

## **⚙️ Installation**  

### **1️⃣ Install `yt-dlp`**  
```sh
pip install yt-dlp
```

### **2️⃣ Install `FFmpeg`**  

#### **For Windows**:  
[Download FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.  

#### **For Mac**:  
```sh
brew install ffmpeg
```

#### **For Linux**:  
```sh
sudo apt install ffmpeg  # Debian/Ubuntu
sudo yum install ffmpeg  # CentOS/RHEL
```

---

## **▶️ Usage**  

### **Run the script**:  
```sh
python youtube-video-downloader.py.py
```

### **Steps:**  
1️⃣ Enter the **YouTube video URL** when prompted.  
2️⃣ Choose a **video quality** by entering a number:  

```
1️⃣  720p
2️⃣  1080p
3️⃣  2K
4️⃣  4K
```

3️⃣ The video will start downloading, and the final **MP4 file** will be saved in the `downloads/` folder.  

---

## **💡 Example Run**  

```
Enter YouTube Video URL: https://www.youtube.com/watch?v=EXAMPLE_ID

Select Video Quality:
1️⃣  720p
2️⃣  1080p
3️⃣  2K
4️⃣  4K

Enter your choice (1-4): 2

Downloading in 1080p... Please wait!
Download Complete! ✅
```

---

## **🛠 Troubleshooting**  

🔹 **If you see an error related to `yt-dlp`**, update it:  
```sh
yt-dlp -U
```

🔹 **If downloads are slow or fail**, try using a **VPN** or updating **FFmpeg**.  

---

## **📜 License**  
This project is open-source under the **MIT License**.  

---

## **🙌 Credits**  
💡 Built using `yt-dlp`  
🎥 Uses `FFmpeg` for processing video and audio  

---

