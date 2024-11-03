# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:39:08 2024

@author: RexWei
"""

from psycopg2 import pool
from config import Config

# 設置資料庫連線池
db_pool = pool.SimpleConnectionPool(
    1, 100,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD,
    host=Config.DB_HOST,
    port=Config.DB_PORT,
    dbname=Config.DB_NAME
)

def fetch_data(query, params=None):
    """從資料庫中查詢資料"""
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    except Exception as e:
        print(f"查詢時發生錯誤: {e}")
    finally:
        db_pool.putconn(conn)

def modify_data(query, params):
    """執行資料庫寫入或更新操作"""
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
    except Exception as e:
        print(f"執行資料庫操作時發生錯誤: {e}")
        conn.rollback()
    finally:
        db_pool.putconn(conn)
