from flask import Flask, request, send_file, jsonify
from moviepy import VideoFileClip
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/extract", methods=["POST"])
def extract_audio():
    try:
        if "video" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        video_file = request.files["video"]
        output_format = request.form.get("format", "mp3")

        # Generate unique filenames
        video_filename = str(uuid.uuid4()) + ".mp4"
        audio_filename = str(uuid.uuid4()) + f".{output_format}"

        video_path = os.path.join(UPLOAD_FOLDER, video_filename)
        audio_path = os.path.join(OUTPUT_FOLDER, audio_filename)

        # Save uploaded video
        video_file.save(video_path)

        # Extract audio
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)

        # Clean up video file
        video.close()
        os.remove(video_path)

        # Send audio file back
        return send_file(audio_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)