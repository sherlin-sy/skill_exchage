from flask import Blueprint, request, jsonify
from app import db
from models import Message

message_bp = Blueprint("message", __name__)


@message_bp.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()

    message = Message(
        sender_id=data["sender_id"],
        receiver_id=data["receiver_id"],
        content=data["content"]
    )

    db.session.add(message)
    db.session.commit()

    return jsonify({"message": "Message sent"})
