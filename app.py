from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

db.create_all()
"""Flask app for Cupcakes
"""

@app.get("/api/cupcakes")
def list_all_cupcakes():
    """ Show info about all cupcakes.
    Respond with JSON like: {cupcakes: [{id, flavor, size, rating, image}, ...]}."""

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.get("/api/cupcakes/<int:cupcake_id>")
def list_single_cupcake(cupcake_id):
    """Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}
     RETURN 404 if cannot found"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post("/api/cupcakes")
def create_cupcake():
    """Create cupcake from form data & return it.

        Respond with JSON like {cupcake: {id, flavor, size, rating, image}}
    """

    #plucks out data from json that was sent by the client
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    #needs to do get or None for optional image here since we haven't reached the database yet
    image = request.json.get("image") or None #edge case in test


    #then we access the database below
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image = image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    # Return w/status code 201 --- return tuple (json, status)
    return (jsonify(cupcake=serialized), 201)



@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """Update cupcake from with data from form & return it.

        Respond with JSON like {cupcake: {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size",cupcake.size)
    cupcake.rating = request.json.get("rating",cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()

    serialized = cupcake.serialize()

    # Return w/status code 200 --- return tuple (json, status)
    return (jsonify(cupcake=serialized), 200)



@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """Delete cupcake from form data & check status code.
        Raise a 404 if the cupcake cannot be found
        Respond with JSON like {"delete":{cupcake_id}}
    """
    Cupcake.get_or_404(cupcake_id)
    Cupcake.query.filter_by(id=cupcake_id).delete()

    db.session.commit()

    # Return w/status code 200 --- return tuple (json, status)
    return (jsonify(delete = cupcake_id), 200)