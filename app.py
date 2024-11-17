from flask import Flask
from config import Config
from routes.main_routes import blueprint  # 匯入 blueprint

# 初始化 Flask 應用
app = Flask(__name__)
app.config.from_object(Config)

# 註冊 Blueprint
app.register_blueprint(blueprint, url_prefix='/')

# 啟動應用
if __name__ == '__main__':
    app.run(debug=True)
