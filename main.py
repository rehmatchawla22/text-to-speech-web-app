from flask import Flask, render_template, request
import pyttsx3
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Directory to save generated audio files
AUDIO_FOLDER = "static/audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():
    audio_file = None

    if request.method == "POST":
        text = request.form["text"]

        if text.strip():
            engine = pyttsx3.init()

            # Set speech properties
            engine.setProperty("rate", 150)
            engine.setProperty("volume", 0.9)

            voices = engine.getProperty("voices")
            if len(voices) > 0:
                engine.setProperty("voice", voices[0].id)

            # Save speech file
            filename = "speech.mp3"
            filepath = os.path.join(AUDIO_FOLDER, filename)

            engine.save_to_file(text, filepath)
            engine.runAndWait()

            audio_file = f"/static/audio/{filename}"

    return render_template("index.html", audio_file=audio_file)

if __name__ == "__main__":
    app.run(debug=True)
