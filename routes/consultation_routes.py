from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace
from controllers.consultation_controller import ConsultationController
from utils.validation import validate_json

# 創建 Blueprint 和 Namespace
consultation_blueprint = Blueprint('consultation', __name__)
consultation_api = Namespace('諮詢紀錄', description='諮詢專用(與教練) API')

# 定義數據模型
consultation_model = consultation_api.model('Consultation', {
    'cID': fields.String(required=True, description='Coach ID'),  # 修改為 String
    'ID': fields.String(required=True, description='User ID'),
    'con_time': fields.String(required=True, description='Consultation time (YYYY-MM-DD HH:MM:SS)'),
    'content': fields.String(description='Consultation content')
})

# 定義更新模型
update_content_model = consultation_api.model('UpdateContent', {
    'new_content': fields.String(required=True, description='New content for consultation')
})

@consultation_api.route('/')
class Consultation(Resource):
    @consultation_api.expect(consultation_model)
    def post(self):
        """建立新的諮詢紀錄"""
        data = validate_json()
        response, status = ConsultationController.create_record(data)
        return response, status

@consultation_api.route('/<string:user_id>')
class ConsultationByUser(Resource):
    def get(self, user_id):
        """根據用戶 ID 查詢諮詢紀錄"""
        response, status = ConsultationController.get_records(user_id)
        return response, status

@consultation_api.route('/coach/<string:cID>')
class ConsultationByCoach(Resource):
    def get(self, cID):
        """根據教練 ID 查詢所有諮詢紀錄"""
        response, status = ConsultationController.get_records_by_coach(cID)
        return response, status

@consultation_api.route('/<string:cID>/<string:user_id>/<string:con_time>')
class DeleteConsultation(Resource):
    def delete(self, cID, user_id, con_time):
        """刪除特定諮詢紀錄"""
        response, status = ConsultationController.delete_record(cID, user_id, con_time)
        return response, status

    @consultation_api.expect(update_content_model)
    def put(self, cID, user_id, con_time):
        """更新特定諮詢紀錄的內容"""
        data = validate_json()
        new_content = data.get('new_content')
        response, status = ConsultationController.update_record_content(cID, user_id, con_time, new_content)
        return response, status

# 將 Namespace 添加到 Blueprint 中
api = Api(consultation_blueprint)
api.add_namespace(consultation_api)
