from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <h1>Welcome to SaveFromAll</h1>
    <p>This will be a video downloader app (YouTube, TikTok, Facebook).</p>
    """)

if __name__ == "__main__":
    app.run(debug=True)
