from app.db.database import *


async def get_userdetail(params):
    query = """SELECT id, password FROM users WHERE email = %s;"""
    abc = await select_query(query, params)
    result = {}
    if abc:
        result['id'] = abc[0]
        result['password'] = abc[1]
    print('result',result)
    return result

async def add_user(params):
    query = """INSERT INTO users (name, email, password, phone, createdatetime) VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
      Returning id"""
    res = await insert_query(query, params)

    return res

