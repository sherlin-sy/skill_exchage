from flask import Blueprint, request, jsonify
from app import db
from models import Exchange, User, CreditTransaction
from datetime import datetime

exchange_bp = Blueprint("exchange", __name__)


@exchange_bp.route("/request", methods=["POST"])
def request_exchange():
    data = request.get_json()

    exchange = Exchange(
        requester_id=data["requester_id"],
        provider_id=data["provider_id"],
        skill_name=data["skill_name"],
        scheduled_time=datetime.strptime(data["scheduled_time"], "%Y-%m-%d %H:%M")
    )

    db.session.add(exchange)
    db.session.commit()

    return jsonify({"message": "Exchange request sent"})


@exchange_bp.route("/complete/<int:id>", methods=["POST"])
def complete_exchange(id):
    exchange = Exchange.query.get(id)

    if exchange:
        exchange.status = "completed"

        provider = User.query.get(exchange.provider_id)
        requester = User.query.get(exchange.requester_id)

        provider.credits += 1
        requester.credits -= 1

        db.session.add(CreditTransaction(user_id=provider.id, amount=1, reason="Teaching"))
        db.session.add(CreditTransaction(user_id=requester.id, amount=-1, reason="Learning"))

        db.session.commit()

        return jsonify({"message": "Exchange completed"})
    return jsonify({"message": "Exchange not found"}), 404
