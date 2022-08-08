"""Models for Cupcake app."""


""" Model names Cupcake
Columns: id, flavor, size, rating, image with default"""

""""database called cupcakes, connect Cupcake model to db
run seed.py"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cupcake(db.Model):
    """Dessert."""

    __tablename__ = "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    flavor = db.Column(
        db.String(50),
        nullable=False
    )

    size = db.Column(
        db.String(50),
        nullable=False
    )


    rating = db.Column(
        db.Integer(),
        nullable=False
    )

    image = db.Column(
        db.Text,
        nullable=False,
        default="https://tinyurl.com/demo-cupcake"
    )

    def serialize(self):
        """Serialize to dictionary."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)