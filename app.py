from flask import Flask, render_template, request
from models import db, Video

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///platform.db"
db.init_app(app)


def seed_data():
    if Video.query.count() > 0:
        return
    sample_videos = [
        Video(title="Big Buck Bunny", description="An open source short film.",
              category="Animation", filename="big_buck_bunny.mp4", thumbnail="big_buck_bunny.jpg"),
        Video(title="Elephants Dream", description="An open source animated film.",
              category="Animation", filename="elephants_dream.mp4", thumbnail="elephants_dream.jpg"),
        Video(title="Sample Talk", description="A short sample talk video.",
              category="Talks", filename="sample_talk.mp4", thumbnail="sample_talk.jpg"),
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
