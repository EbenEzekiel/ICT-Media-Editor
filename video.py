from moviepy import VideoFileClip

def extract_video_sections(input_path, sections, output_prefix="clip"):
    """
    Extract multiple sections from a video.

    Parameters:
    - input_path (str): Path to the input video file
    - sections (list of tuples): List of (start_time, end_time) in seconds
    - output_prefix (str): Prefix for output clip filenames

    Example:
    sections = [(0, 10), (30, 45), (60, 75)]
    """
    video = VideoFileClip(input_path)

    output_files = []

    for i, (start, end) in enumerate(sections):
        clip = video.subclipped(start, end)
        output_path = f"{output_prefix}_{i+1}.mp4"
        clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        output_files.append(output_path)

    video.close()
    return output_files


# Example usage:
if __name__ == "__main__":
    sections = [(0, 5), (10, 20), (30, 40)]
    files = extract_video_sections("input.mp4", sections)
    print("Saved clips:", files)