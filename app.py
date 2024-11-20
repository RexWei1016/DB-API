from flask import Flask
from flask_restx import Api
from flask_cors import CORS  # 新增這行
from config import Config
from routes.user_routes import user_api
from routes.daily_monitor_routes import daily_monitor_api
from routes.exercise_record_routes import exercise_record_api
from routes.food_record_routes import food_record_api
from routes.consultation_routes import consultation_api
from routes.coach_routes import coach_api

# 初始化 Flask 應用
app = Flask(__name__)
app.config.from_object(Config)

# 啟用 CORS，允許來自指定的域名
CORS(
    app, 
    resources={r"/*": {"origins": ["https://rexwei1016.github.io", "http://localhost:3000", "http://127.0.0.1:3000"]}},
    supports_credentials=True,  # 確保支持跨域憑證
    methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"],  # 確保允許所有相關的 HTTP 方法
)


# 創建全局的主 API
main_api = Api(
    app,
    doc='/swagger',  # 全局 Swagger 頁面路徑
    title='健康管理後端API',
    version='1.0',
    description='2024/11/20版本'
)

# 添加所有的 Namespaces
main_api.add_namespace(user_api, path='/user')
main_api.add_namespace(daily_monitor_api, path='/daily_monitor')
main_api.add_namespace(exercise_record_api, path='/exercise_record')
main_api.add_namespace(food_record_api, path='/food_record')
main_api.add_namespace(consultation_api, path='/consultation')
main_api.add_namespace(coach_api, path='/coach')

# 啟動應用
if __name__ == '__main__':
    app.run(debug=True)
