from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, default="")
    category = db.Column(db.String(50), default="General")
    filename = db.Column(db.String(200), nullable=False)  # file in static/videos/
    thumbnail = db.Column(db.String(200), default="")  # file in static/thumbnails/
