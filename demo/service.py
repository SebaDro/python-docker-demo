import json

from flask import request, Response, abort
from demo import app


@app.route("/greeting", methods=["GET"])
def greeting():
    # Read the value for query parameter 'name'.
    # If no query parameter have been specified, use a default value.
    name = request.args.get("name", default="KomMonitor", type=str)

    # Return the Response
    return Response(f"Hello {name}", mimetype='text/plain')