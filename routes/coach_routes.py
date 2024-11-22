from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace
from controllers.CoachController import CoachController
from controllers.consultation_controller import ConsultationController
from utils.validation import validate_json

coach_blueprint = Blueprint('coach', __name__)
coach_api = Namespace('教練', description='教練註冊、登入與查詢 APIs')

# 定義教練數據模型
register_model = coach_api.model('Register', {
    'cID': fields.String(required=True, description='Coach ID'),
    'password': fields.String(required=True, description='Coach password'),
    'name': fields.String(required=True, description='Coach name'),
    'onboarding': fields.String(required=True, description='Onboarding date'),
    'exp': fields.String(required=True, description='Expertise')
})

clogin_model = coach_api.model('Login', {
    'cID': fields.String(required=True, description='Coach ID'),
    'password': fields.String(required=True, description='Coach password')
})

@coach_api.route('/register')
class Register(Resource):
    @coach_api.expect(register_model)
    def post(self):
        data = validate_json()
        response, status = CoachController.register_coach(**data)
        return response, status

@coach_api.route('/login')
class Login(Resource):
    @coach_api.expect(clogin_model)
    def post(self):
        data = validate_json()
        response, status = CoachController.login_coach(data['cID'], data['password'])
        return response, status

@coach_api.route('/all')
class GetAllCoaches(Resource):
    def get(self):
        # 調用 CoachController.get_all_coaches() 方法來獲取所有教練
        response, status = CoachController.get_all_coaches()
        return response, status
