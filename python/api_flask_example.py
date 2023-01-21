# https://www.youtube.com/watch?v=qbLc5a9jdXo
# https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#create-the-tables
# source ~/venv/python311/bin/activate
# pip install flask flask-sqlalchemy

# to run from cmd:
# flask --app api-flask-example run

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api-flask-example.db"
db = SQLAlchemy(app)
db.init_app(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name}: {self.description}"


@app.route("/")
def index():
    return "<p>Hello!</p>"


@app.route("/api")
def api():
    items = Item.query.all()
    output = []
    for item in items:
        item_data = {
            "id": item.id,
            "name": item.name,
            "description": item.description,
        }
        output.append(item_data)
    return {"items": output}


@app.route("/api/<id>")
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(
        {"id": item.id, "name": item.name, "description": item.description}
    )


@app.route("/api", methods=["POST"])
def add_item():
    # test via
    # curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "test, "descrption": "test"}' localhost:5000/api
    if request.json:
        item = Item(
            name=request.json["name"], description=request.json["description"]
        )
        db.session.add(item)
        db.session.commit()
        return {"id": item.id}
    return -1


@app.route("/api/<id>", methods=["DELETE"])
def add_item():
    # test via
    # curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "test, "descrption": "test"}' localhost:5000/api
    item = Item.query.get(id)
    if item is None:
        return {"error": "not found"}
    db.session.delete(item)
    db.session.commit()
    return {"message": f"{id} deleted"}
