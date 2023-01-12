import os

from flask import request, Response, abort
from demo import app

default_greeting = "Hello"


@app.route("/greeting", methods=["GET"])
def greeting():
    # Read the value for query parameter 'name'.
    # If no query parameter have been specified, use a default value.
    name = request.args.get("name", default="KomMonitor", type=str)

    # Read out the CUSTOM_GREETINGS environment variable. If not set, use a default greeting.
    greetings_text = os.environ.get("CUSTOM_GREETING", default_greeting)

    # Return the Response
    return Response(f"{greetings_text} {name}!", mimetype='text/plain')
