from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace
from controllers.daily_monitor_controller import DailyMonitorController
from utils.validation import validate_json

# 創建 Blueprint 和 Namespace
daily_monitor_blueprint = Blueprint('daily_monitor', __name__)
daily_monitor_api = Namespace('日常數據', description='日常數據專用API')

# 定義數據模型
daily_monitor_model = daily_monitor_api.model('DailyMonitor', {
    'm_date': fields.String(required=True, description='Measurement date (YYYY-MM-DD)'),
    'id': fields.String(required=True, description='User ID'),
    'weight': fields.Float(description='Weight (kg)'),
    'height': fields.Float(description='Height (cm)'),
    'b_pressure': fields.String(description='Blood pressure (e.g., "120/80")'),
    'sleep_dt': fields.String(description='Sleep date (YYYY-MM-DD)'),
    'sleep_duration': fields.String(description='Sleep duration (HH:MM:SS)'),
    'sleep_quality': fields.String(description='Sleep quality (e.g., "Good", "Fair", "Poor")')
})

@daily_monitor_api.route('/')
class DailyMonitor(Resource):
    @daily_monitor_api.expect(daily_monitor_model)
    def post(self):
        data = validate_json()
        response, status = DailyMonitorController.create_record(data)
        return response, status

@daily_monitor_api.route('/<string:user_id>')
class DailyMonitorByUser(Resource):
    def get(self, user_id):
        response, status = DailyMonitorController.get_records(user_id)
        return response, status

@daily_monitor_api.route('/<string:user_id>/<string:m_date>')
class DeleteDailyMonitor(Resource):
    def delete(self, user_id, m_date):
        response, status = DailyMonitorController.delete_record(user_id, m_date)
        return response, status
