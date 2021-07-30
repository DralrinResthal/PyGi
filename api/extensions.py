import json
from flask import request, current_app
from logging import getLogger

err_log = getLogger("errlog")
app_log = getLogger("applog")


def authorized(func):
    def auth_wrapper(*args, **kwargs):
        data = request.json
        headers = request.headers

        try:
            data["authToken"]
        except KeyError as e:
            app_log.info(
                f"Invalid request made. No authToken. \n{json.dumps(data, indent=2, sort_keys=False)}\n{headers}"
            )
            return "Not Allowed", 403

        try:
            data["userInfo"]["userName"]
        except KeyError as e:
            app_log.info(
                f"Invalid request made. No userName. \n{json.dumps(data, indent=2, sort_keys=False)}\n{headers}"
            )
            return "Not Allowed", 403

        if data["authToken"] != current_app.config["AUTHTOKEN"]:
            app_log.info(
                f"Invalid request made. Unauthorized authToken used. \n{json.dumps(data, indent=2, sort_keys=False)}\n{headers}"
            )
            return "Not Allowed", 403

        app_log.info(
            f"Request authorized successfully. \n{json.dumps(data, indent=2, sort_keys=False)}"
        )
        return func(*args, **kwargs)

    return auth_wrapper
