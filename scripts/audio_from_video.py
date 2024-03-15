import os
import argparse
import glob


def parse_args():
    #Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', required=False, type=str, default="../data/test.mp4")
    parser.add_argument('--output_path', required=False, type=str, default="../data/test.wav")  
    args = parser.parse_args()
    return args.filepath, args.output_path


def audio_from_video(filepath, output_path):
    # Extract audio from video and save as wav file
    try:
        os.system(f"ffmpeg -i '{filepath}' -ab 160k -ac 2 -ar 16000 -vn '{output_path}'")
    except Exception as e:
        print(e)
        

def main():
    filepath, output_path = parse_args()
    
    if filepath == "download/video":
        filepath = glob.glob("download/video.*")[0]
    
    audio_from_video(filepath, output_path)


if __name__=='__main__':
    main()