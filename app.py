from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()
# /login [GET, POST]
# /register [GET, POST]
# /logout [GET ? POST ?? DELETE]
#
# /profile (/user, /me) [GET, PUT(PATCH), DELETE]
#       ?  /favouties [GET, POST, DELETE, PATCH]
#       ??  /favouties/<favourite_id> [DELETE]
#       ?  /search_history [GET, DELETE]
#
# /items [GET, POST]
# /items/<item_id> [GET, DELETE]
# /leasers [GET]
# /leasers/<leaser_id> [GET]
#
# /contracts [GET, POST]
# /contracts/<contract_id> [GET, PATCH/PUT]
#
# /search [GET, (POST)]
#
# /complain [POST]
# /compare [GET, PUT/PATCH]


