from flask import Blueprint, request, g
from api.extensions import authorized


bp = Blueprint("git", __name__, url_prefix="/git")


@bp.route("/test", methods=["POST"])
@authorized
def test():
    return "Git blueprint loaded.", 200
