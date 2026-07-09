from flask import Flask, render_template, request
from ai_video import generate_video

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/generate", methods=["POST"])
def generate():

    prompt = request.form.get("prompt")

    try:
        video = generate_video(prompt)

        return render_template(
            "dashboard.html",
            prompt=prompt,
            video=video
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
