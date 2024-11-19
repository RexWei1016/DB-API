from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace
from controllers.consultation_controller import ConsultationController
from utils.validation import validate_json

# 創建 Blueprint 和 Namespace
consultation_blueprint = Blueprint('consultation', __name__)
consultation_api = Namespace('諮詢紀錄', description='諮詢專用(與教練) API')

# 定義數據模型
consultation_model = consultation_api.model('Consultation', {
    'cID': fields.Integer(required=True, description='Coach ID'),
    'ID': fields.String(required=True, description='User ID'),
    'con_time': fields.String(required=True, description='Consultation time (YYYY-MM-DD HH:MM:SS)'),
    'content': fields.String(description='Consultation content')
})

@consultation_api.route('/')
class Consultation(Resource):
    @consultation_api.expect(consultation_model)
    def post(self):
        data = validate_json()
        response, status = ConsultationController.create_record(data)
        return response, status

@consultation_api.route('/<string:user_id>')
class ConsultationByUser(Resource):
    def get(self, user_id):
        response, status = ConsultationController.get_records(user_id)
        return response, status

@consultation_api.route('/<int:cID>/<string:user_id>/<string:con_time>')
class DeleteConsultation(Resource):
    def delete(self, cID, user_id, con_time):
        response, status = ConsultationController.delete_record(cID, user_id, con_time)
        return response, status
