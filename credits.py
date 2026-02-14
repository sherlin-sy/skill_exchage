from flask import Blueprint, jsonify
from models import User

credits_bp = Blueprint("credits", __name__)


@credits_bp.route("/<int:user_id>", methods=["GET"])
def get_credits(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"credits": user.credits})
    return jsonify({"message": "User not found"}), 404
