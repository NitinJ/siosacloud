import json
import logging

import redis as redis
from flask import Flask, request

FORMAT = "%(created)f - %(thread)d: [%(filename)s:%(lineno)s - %(funcName)s() " \
         "] %(message)s "
logging.basicConfig(filename='log.txt', filemode='a', format=FORMAT)

app = Flask(__name__)

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis_connection = redis.Redis(connection_pool=pool)
KEY_EXPIRY_AFTER_REGISTER = 90 * 86400  # 90 days


@app.route("/api/license/get", methods=['POST'])
def get_license():
    data = request.get_json()
    if not data or not data['key'] or not data['muid']:
        return {"status": False}
    key = data['key']
    muid = data['muid']

    key_details_str = redis_connection.get(key)
    if not key_details_str:
        # Invalid key.
        return {"status": False}

    key_details = json.loads(key_details_str)
    if not key_details['muid']:
        # Register machine
        data = {"muid": muid}
        redis_connection.set(key, json.dumps(data),
                             ex=KEY_EXPIRY_AFTER_REGISTER)
        return {"status": True, "valid": True}

    if key_details['muid'] == muid:
        return {"status": True, "valid": True}
    return {"status": True, "valid": False}


if __name__ == "__main__":
    app.run()
