from flask import Blueprint
from flask_restx import Api

swagger_blueprint = Blueprint('swagger', __name__)
swagger_api = Api(
    swagger_blueprint,
    doc='/swagger',  # 全局統一的 Swagger 頁面
    title='Health Management API',
    version='1.0',
    description='Unified API Documentation'
)
