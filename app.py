from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

db.create_all()
"""Flask app for Cupcakes

GET /api/cupcakes: info about all cupcakes
"""

@app.get("/api/cupcakes")
def list_all_desserts():
    """ Respond with JSON like: {cupcakes: [{id, flavor, size, rating, image}, ...]}."""

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.get("/api/cupcakes/<int:cupcake_id>")
def list_single_dessert(cupcake_id):
    """Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}
     RETURN 404 if cannot found"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def create_dessert():
    """Create cupcake from form data & return it.

    Respond with JSON like {cupcake: {id, flavor, size, rating, image}}
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]



    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image = image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    # Return w/status code 201 --- return tuple (json, status)
    return (jsonify(cupcake=serialized), 201)











"""
GET /api/cupcakes/[cupcake-id]: info about one cupcake
            SHOULD RAISE 404 if not found (use get_or_404 here???)









POST/api/cupcakes: create cupcake with FLAVOR, SIZE, RATING and IMAGE
    (TRY IT OUT IN INSOMNIA, SET IT TO JSON FOR BODY TEXT)
Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}






PATCH /api/cupcakes/[cupcake-id]: update one cupcake using its id(passed in URL)
                Request body mau include flavor, size, rating and image but not all

                RETURN 404 if cannot found
Respond with JSON like {cupcake: {id, flavor, size, rating, image}}

DELETE /api/cupcakes/[cupcake-id]: delete cupcake given its id (passed in URL)
    Respond with JSON like {deleted: [cupcake-id]}


"""