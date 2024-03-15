import argparse
import glob
import os
from  yt_dlp import YoutubeDL


def parse_args():
    #Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, type=str)
    args = parser.parse_args()
    return args.url

def download_video(url):
    # Download video from url and save with name video and return the filepath
    with YoutubeDL(params={"outtmpl": "download/video"}) as ydl:
        ydl.download([url])
        filepath = glob.glob("download/video.*")[0]
    return filepath
    
def main():
    # Download video from url
    url = parse_args()
    
    # Create download directory if it does not exist
    if not os.path.exists("download"):
        os.makedirs("download")
    
    filepath = download_video(url)
    return filepath

if __name__=='__main__':
    main()