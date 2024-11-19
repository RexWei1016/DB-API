from flask import request, abort

def validate_json():
    if not request.is_json:
        abort(400, 'Content-Type must be application/json')
    data = request.json
    if not data:
        abort(400, 'Invalid JSON body')
    return data
