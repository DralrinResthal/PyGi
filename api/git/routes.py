from flask import Blueprint, request, g
from api.extensions import authorized


bp = Blueprint("git", __name__, url_prefix="/git")


@bp.route("/test", methods=["POST"])
@authorized
def test():
    return "Git blueprint loaded.", 200


@bp.route("/clone", methods=["GET"])
def clone():
    pass


@bp.route("/branch", methods=["POST"])
def branch():
    pass


@bp.route("/commit", methods=["POST"])
def commit():
    pass


@bp.route("/push", methods=["POST"])
def push():
    pass


# Because there is only 1 "github" route, it is in git
@bp.route("/pr", methods=["POST"])
def pr():
    pass
