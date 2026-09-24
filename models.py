from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, default="")
    category = db.Column(db.String(50), default="General")
    # hosted URLs for now so the app plays without local media files
    video_url = db.Column(db.String(300), nullable=False)
    thumbnail_url = db.Column(db.String(300), default="")
