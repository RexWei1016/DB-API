from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return jsonify({"message": "Welcome to the API server!"})

@main_bp.route('/register', methods=['POST'])
def register():
    account = request.json.get('account')
    username = request.json.get('username')
    password = request.json.get('password')
    birth = request.json.get('birth')
    sex = request.json.get('sex')
    cname = request.json.get('cname')
    use = request.json.get('use')
    number = request.json.get('number')

    # 調用控制器中的業務邏輯
    response, status = UserController.register_user(account, username, password, birth, sex, cname, use, number)
    return jsonify(response), status

@main_bp.route('/login', methods=['POST'])
def login():
    account = request.json.get('account')
    password = request.json.get('password')

    # 調用控制器中的業務邏輯
    response, status = UserController.login_user(account, password)
    return jsonify(response), status
