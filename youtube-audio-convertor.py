import os
import yt_dlp

def download_audio_from_youtube(url, output_path='./audios'):
    """
    Download a YouTube video and convert it to audio using yt-dlp
    
    Args:
        url (str): YouTube video URL
        output_path (str): Directory to save the audio files
    
    Returns:
        str: Path to the saved audio file
    """
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Created directory: {output_path}")
        
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'paths': {'home': output_path},
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'verbose': True
        }
        
        # Download and convert to audio
        print(f"Downloading and converting audio from: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info).replace(f'.{info["ext"]}', '.mp3')
            
        print(f"Audio saved to: {filename}")
        return os.path.join(output_path, filename)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def batch_download_audio(urls, output_path='./downloads'):
    """
    Download multiple YouTube videos and convert them to audio
    
    Args:
        urls (list): List of YouTube video URLs
        output_path (str): Directory to save the audio files
    
    Returns:
        list: Paths to the saved audio files
    """
    saved_files = []
    for i, url in enumerate(urls):
        print(f"\nProcessing video {i+1}/{len(urls)}")
        audio_path = download_audio_from_youtube(url, output_path)
        if audio_path:
            saved_files.append(audio_path)
    
    print(f"\nDownloaded {len(saved_files)} audio files")
    return saved_files

# Example usage
if __name__ == "__main__":
    # Single video download
    url = "https://www.youtube.com/watch?v=Gafy3BgThhs&ab_channel=KalebBrasee"  # Replace with your desired YouTube URL
    download_audio_from_youtube(url)
    
    # Batch download example
    # urls = [
    #     "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    #     "https://www.youtube.com/watch?v=9bZkp7q19f0"
    # ]
    # batch_download_audio(urls)