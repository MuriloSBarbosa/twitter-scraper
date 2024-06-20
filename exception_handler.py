
from flask.json import jsonify
from flask import Flask
from twikit import errors


class handle_exceptions():
    def __init__(self, app: Flask):
        self.app = app
        self.register_error_handlers()

    def register_error_handlers(self):
        self.app.errorhandler(errors.Unauthorized)(self.unauthorized)
        self.app.errorhandler(errors.BadRequest)(self.bad_request)
        self.app.errorhandler(ValueError)(self.internal_server_error)

    def unauthorized(self, e):
        return jsonify({'message': str(e)}), 401
    
    def bad_request(self, e):
        return jsonify({'message': str(e)}), 400
    
    def internal_server_error(self, e):
        return jsonify({'message': str(e)}), 500