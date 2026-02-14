from flask import Blueprint, jsonify
from models import User, Exchange

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])


@admin_bp.route("/exchanges", methods=["GET"])
def get_exchanges():
    exchanges = Exchange.query.all()
    return jsonify([{"id": e.id, "skill": e.skill_name, "status": e.status} for e in exchanges])
