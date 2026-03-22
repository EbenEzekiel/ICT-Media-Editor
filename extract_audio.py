from moviepy import VideoFileClip

def extract_audio(video_path, output_audio_path):
    try:
        # Load the video file
        video = VideoFileClip(video_path)
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to a file
        audio.write_audiofile(output_audio_path)
        
        print(f"Audio extracted successfully to: {output_audio_path}")
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    video_file = "input_video.mp4"
    audio_file = "output_audio.mp3"
    
    extract_audio(video_file, audio_file)