# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:38:44 2024

@author: RexWei
"""

import os
from dotenv import load_dotenv

# 載入 .env 文件中的環境變數
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DB_USER = os.getenv('DB_USER', 'default_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'default_db')
