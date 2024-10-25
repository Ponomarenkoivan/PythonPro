
from flask import Flask, request

app = Flask(__name__)
# /login [GET, POST]
# /register [GET, POST]
# /logout [GET ? POST ?? DELETE]
#
# /profile (/user, /me) [GET, PUT(PATCH), DELETE]
#       ?  /favouties [GET, POST, DELETE, PATCH]
#       ??  /favouties/<favourite_id> [DELETE]
#       не додавав, вважаю непотрібним /search_history [GET, DELETE]
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('/logout', methods=['GET', 'POST', 'DELETE'])
def logout():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    if request.method == 'DELETE':
        return 'DELETE'


@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('/items/<items_id>', methods=['GET', 'DELETE'])
def item_details(items_id):
    if request.method == 'GET':
        return f'GET {items_id}'
    if request.method == 'DELETE':
        return f'DELETE {items_id}'


@app.route('/leasers', methods=['GET'])
def leasers():
    if request.method == 'GET':
        return 'GET'


@app.route('/leasers/<leasers_id>', methods=['GET'])
def leaser_details(leasers_id):
    if request.method == 'GET':
        return f'GET {leasers_id}'


@app.route('/profile', methods=['GET'])
def profile():
    if request.method == 'GET':
        return 'GET'


@app.route('/profile/<user>', methods=['GET'])
def profile_details(user):
    if request.method == 'GET':
        return f'GET {user}'
    if request.method == 'PATCH':
        return f'PATCH {user}'
    if request.method == 'DELETE':
        return f'DELETE {user}'


@app.route('/profile/user/<me>', methods=['GET'])
def profile_user(me):
    if request.method == 'GET':
        return f'GET {me}'
    if request.method == 'PATCH':
        return f'PATCH {me}'
    if request.method == 'DELETE':
        return f'DELETE {me}'


@app.route('/profile/user/me/<favouties>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def profile_user_me(favouties):
    if request.method == 'GET':
        return f'GET {favouties}'
    if request.method == 'POST':
        return f'POST {favouties}'
    if request.method == 'PATCH':
        return f'PATCH {favouties}'
    if request.method == 'DELETE':
        return f'DELETE {favouties}'


@app.route('/profile/user/me/favouties/<favourite_id>', methods=['DELETE'])
def profile_user_favourite(favourite_id):
    if request.method == 'DELETE':
        return f'DELETE {favourite_id}'


@app.route('/contracts', methods=['GET', 'POST'])
def contracts():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('/contracts/<contract_id>', methods=['GET', 'PATCH'])
def contract_details(contract_id):
    if request.method == 'GET':
        return f'GET {contract_id}'
    if request.method == 'PATCH':
        return f'PATCH {contract_id}'


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('/complain', methods=['POST'])
def complain():
    if request.method == 'POST':
        return 'POST'

@app.route('/compare', methods=['GET', 'PATCH'])
def compare():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'PATCH':
        return 'PATCH'






if __name__ == '__main__':
    app.run(debug=True)