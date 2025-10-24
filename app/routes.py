from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import Item, db

api = Blueprint("api", __name__)

@api.route("/items", methods=["GET"])
@jwt_required()
def get_items():
    items = Item.query.all()
    return jsonify([{"id": i.id, "name": i.name, "description": i.description} for i in items])


@api.route("/items/<int:id>", methods=["GET"])
@jwt_required()
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify({"id": item.id, "name": item.name, "description": item.description})


@api.route("/items", methods=["POST"])
@jwt_required()
def create_item():
    data = request.get_json()
    item = Item(name=data["name"], description=data.get("description"))
    db.session.add(item)
    db.session.commit()
    return jsonify({"message": "Item created successfully"}), 201


@api.route("/items/<int:id>", methods=["PUT"])
@jwt_required()
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get("name", item.name)
    item.description = data.get("description", item.description)
    db.session.commit()
    return jsonify({"message": "Item updated successfully"})


@api.route("/items/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})
