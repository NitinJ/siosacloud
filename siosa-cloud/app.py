import logging

from flask import Flask, request

FORMAT = "%(created)f - %(thread)d: [%(filename)s:%(lineno)s - %(funcName)s() " \
         "] %(message)s "
logging.basicConfig(filename='log.txt', filemode='a', format=FORMAT)

app = Flask(__name__)


@app.route("/license/get", methods=['GET'])
def get_license():
    return {"status": True, "details": {"key": "zbxc", "valid": True}}


if __name__ == "__main__":
    app.run()