from flask import Flask, render_template, request
from models import db, Video

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///platform.db"
db.init_app(app)


GTV_BASE = "https://storage.googleapis.com/gtv-videos-bucket/sample"


def seed_data():
    if Video.query.count() > 0:
        return
    sample_videos = [
        Video(title="Big Buck Bunny", description="An open source short film.",
              category="Animation", video_url=f"{GTV_BASE}/BigBuckBunny.mp4",
              thumbnail_url=f"{GTV_BASE}/images/BigBuckBunny.jpg"),
        Video(title="Elephants Dream", description="An open source animated film.",
              category="Animation", video_url=f"{GTV_BASE}/ElephantsDream.mp4",
              thumbnail_url=f"{GTV_BASE}/images/ElephantsDream.jpg"),
        Video(title="For Bigger Blazes", description="A short sample promo clip.",
              category="Talks", video_url=f"{GTV_BASE}/ForBiggerBlazes.mp4",
              thumbnail_url=f"{GTV_BASE}/images/ForBiggerBlazes.jpg"),
    ]
    db.session.bulk_save_objects(sample_videos)
    db.session.commit()


@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    if query:
        videos = Video.query.filter(Video.title.ilike(f"%{query}%")).all()
    else:
        videos = Video.query.all()
    return render_template("index.html", videos=videos, query=query)


@app.route("/video/<int:video_id>")
def video_detail(video_id):
    video = Video.query.get_or_404(video_id)
    related = Video.query.filter(Video.category == video.category, Video.id != video.id).all()
    return render_template("video.html", video=video, related=related)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(debug=True)
