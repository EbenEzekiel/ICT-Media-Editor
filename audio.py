from moviepy import AudioFileClip

def extract_audio_sections(input_path, sections, output_prefix="audio_clip"):
    """
    Extract multiple sections from an audio file.

    Parameters:
    - input_path (str): Path to the input audio file
    - sections (list of tuples): List of (start_time, end_time) in seconds
    - output_prefix (str): Prefix for output clip filenames

    Returns:
    - List of saved file paths

    Example:
    sections = [(0, 10), (30, 45), (60, 75)]
    """
    audio = AudioFileClip(input_path)
    output_files = []

    for i, (start, end) in enumerate(sections):
        clip = audio.subclipped(start, end)
        output_path = f"{output_prefix}_{i+1}.mp3"
        clip.write_audiofile(output_path)
        output_files.append(output_path)

        clip.close()

    audio.close()
    return output_files


# Example usage:
if __name__ == "__main__":
    sections = [(0, 5), (10, 20), (30, 40)]
    files = extract_audio_sections("input.mp3", sections)
    print("Saved clips:", files)