from moviepy import VideoFileClip, concatenate_videoclips

def cut_and_join_video(input_video, segments, output_video):
    """
    قطع أجزاء مختلفة من فيديو ثم دمجها معًا

    :param input_video: مسار الفيديو الأصلي
    :param segments: قائمة من الأزواج (start, end) بالثواني
                     مثال: [(0, 10), (30, 50), (60, 90)]
    :param output_video: مسار الفيديو الناتج
    """

    try:
        # Load video
        video = VideoFileClip(input_video)

        clips = []

        # Cut each segment
        for start, end in segments:
            clip = video.subclip(start, end)
            clips.append(clip)

        # Join clips together
        final_video = concatenate_videoclips(clips)

        # Export final video
        final_video.write_videofile(output_video)

        # Cleanup
        video.close()
        final_video.close()

        print("Video processed successfully!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    input_file = "input.mp4"

    # قطع مقاطع مختلفة (بالثواني)
    segments_to_keep = [
        (0, 10),     # من 0 إلى 10 ثواني
        (25, 40),    # من 25 إلى 40
        (60, 80)     # من 60 إلى 80
    ]

    output_file = "output.mp4"

    cut_and_join_video(input_file, segments_to_keep, output_file)

# final_video = concatenate_videoclips(clips, method="compose")