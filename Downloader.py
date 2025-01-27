import yt_dlp

def download_youtube_videos(video_urls):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Select best quality
            'outtmpl': '%(title)s.%(ext)s',       # Save with video title as filename
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for url in video_urls:
                print(f"Downloading video from URL: {url}")
                ydl.download([url])
        print("All downloads completed.")
    except Exception as e:
        print(f"An error occurred: {e}")


video_urls = [
        "Link 1",
        "Link 2",
    ]
    
  
download_youtube_videos(video_urls)
