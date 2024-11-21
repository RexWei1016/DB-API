from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace
from controllers.user_controller import UserController
from utils.validation import validate_json

user_blueprint = Blueprint('user', __name__)

user_api = Namespace('使用者註冊', description='一般使用者註冊用')

# 電話號碼模型
phone_model = user_api.model('Phone', {
    'phone': fields.String(required=True, description='Phone number'),
    'phone_type': fields.String(required=True, description='Phone type (e.g., home, mobile, work)')
})

# 使用者模型
user_model = user_api.model('User', {
    'account': fields.String(required=True, description='User account'),
    'username': fields.String(required=True, description='User name'),
    'password': fields.String(required=True, description='Password'),
    'birth': fields.String(description='Birth date'),
    'sex': fields.String(description='Sex'),
    'cname': fields.String(description='Chinese name'),
    'use': fields.String(description='Usage type'),
    'number': fields.String(description='Primary number'),
    'phones': fields.List(fields.Nested(phone_model), description='List of phone numbers')
})

login_model = user_api.model('UserLogin', {
    'account': fields.String(required=True, description='User account'),
    'password': fields.String(required=True, description='User password')
})

@user_api.route('/register')
class Register(Resource):
    @user_api.expect(user_model)
    def post(self):
        data = validate_json()
        response, status = UserController.register_user(
            account=data.get('account'),
            username=data.get('username'),
            password=data.get('password'),
            birth=data.get('birth'),
            sex=data.get('sex'),
            cname=data.get('cname'),
            use=data.get('use'),
            number=data.get('number'),
            phones=data.get('phones', [])
        )
        return response, status

@user_api.route('/login')
class Login(Resource):
    @user_api.expect(login_model)
    def post(self):
        data = validate_json()
        account = data.get('account')
        password = data.get('password')
        response, status = UserController.login_user(account, password)
        return response, status


@user_api.route('/users')
class Users(Resource):
    def get(self):
        response, status = UserController.get_all_users()
        return response, status
