from db.database import fetch_data, modify_data

class FoodModel:
    @staticmethod
    def create_food(data):
        query = '''
            INSERT INTO food (food_type, food_calories)
            VALUES (%s, %s)
        '''
        params = (data['food_type'], data['food_calories'])
        modify_data(query, params)

    @staticmethod
    def get_all_foods():
        query = '''
            SELECT fid, food_type, food_calories
            FROM food
            ORDER BY fid ASC
        '''
        return fetch_data(query)

    @staticmethod
    def delete_food(fid):
        query = '''
            DELETE FROM food
            WHERE fid = %s
        '''
        modify_data(query, (fid,))
