from flask import Blueprint, request
from flask_restx import Api, Resource, fields

# 匯入控制器
from controllers.user_controller import UserController
from controllers.daily_monitor_controller import DailyMonitorController
from controllers.exercise_record_controller import ExerciseRecordController
from controllers.food_record_controller import FoodRecordController
from controllers.consultation_controller import ConsultationController

# 初始化 Blueprint 和 Api
blueprint = Blueprint('api', __name__)
api = Api(blueprint, doc='/swagger', title='Health Management API', version='1.0', description='Health API Documentation')

# 定義數據模型
user_model = api.model('User', {
    'account': fields.String(required=True, description='User account'),
    'username': fields.String(required=True, description='User name'),
    'password': fields.String(required=True, description='Password'),
    'birth': fields.String(description='Birth date'),
    'sex': fields.String(description='Sex'),
    'cname': fields.String(description='Chinese name'),
    'use': fields.String(description='Usage type'),
    'number': fields.String(description='Phone number')
})

# 使用 RESTx 定義路由
@api.route('/register')
class Register(Resource):
    @api.expect(user_model)
    def post(self):
        data = request.json
        response, status = UserController.register_user(**data)
        return response, status  # 直接返回控制器的結果

@api.route('/login')
class Login(Resource):
    @api.doc(params={'account': 'User account', 'password': 'Password'})
    def post(self):
        account = request.json.get('account')
        password = request.json.get('password')
        response, status = UserController.login_user(account, password)
        return response, status  # 直接返回控制器的結果

# 身體記錄量測 API 路由
@api.route('/daily_monitor')
class DailyMonitor(Resource):
    def post(self):
        data = request.json
        response, status = DailyMonitorController.create_record(data)
        return response, status

@api.route('/daily_monitor/<string:user_id>')
class DailyMonitorByUser(Resource):
    def get(self, user_id):
        response, status = DailyMonitorController.get_records(user_id)
        return response, status

@api.route('/daily_monitor/<string:user_id>/<string:m_date>')
class DeleteDailyMonitor(Resource):
    def delete(self, user_id, m_date):
        response, status = DailyMonitorController.delete_record(user_id, m_date)
        return response, status

# 運動記錄 API 路由
@api.route('/exercise_record')
class ExerciseRecord(Resource):
    def post(self):
        data = request.json
        response, status = ExerciseRecordController.create_record(data)
        return response, status

@api.route('/exercise_record/<string:user_id>')
class ExerciseRecordByUser(Resource):
    def get(self, user_id):
        response, status = ExerciseRecordController.get_records(user_id)
        return response, status

@api.route('/exercise_record/<string:user_id>/<string:exe_date>')
class DeleteExerciseRecord(Resource):
    def delete(self, user_id, exe_date):
        response, status = ExerciseRecordController.delete_record(user_id, exe_date)
        return response, status

# 飲食記錄 API 路由
@api.route('/food_record')
class FoodRecord(Resource):
    def post(self):
        data = request.json
        response, status = FoodRecordController.create_record(data)
        return response, status

@api.route('/food_record/<string:user_id>')
class FoodRecordByUser(Resource):
    def get(self, user_id):
        response, status = FoodRecordController.get_records(user_id)
        return response, status

@api.route('/food_record/<string:user_id>/<string:eat_date>/<int:fID>')
class DeleteFoodRecord(Resource):
    def delete(self, user_id, eat_date, fID):
        response, status = FoodRecordController.delete_record(user_id, eat_date, fID)
        return response, status

# 諮詢記錄 API 路由
@api.route('/consultation')
class Consultation(Resource):
    def post(self):
        data = request.json
        response, status = ConsultationController.create_record(data)
        return response, status

@api.route('/consultation/<string:user_id>')
class ConsultationByUser(Resource):
    def get(self, user_id):
        response, status = ConsultationController.get_records(user_id)
        return response, status

@api.route('/consultation/<int:cID>/<string:user_id>/<string:con_time>')
class DeleteConsultation(Resource):
    def delete(self, cID, user_id, con_time):
        response, status = ConsultationController.delete_record(cID, user_id, con_time)
        return response, status
