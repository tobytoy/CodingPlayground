from flask_restful import Resource, reqparse


hello_users = [{
    'name': 'toby',
    'email': 'toby@gmail',
    'password': '1234'
}]

class User (Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='Email is required')
    parser.add_argument('password', required=True, help='Password is required')

    def get(self, name):
        find = [item for item in hello_users if item['name'] == name]
        if len(find) == 0:
            return {
                'message': 'username not exist!'
            }, 403
        user = find[0]
        if not user:
            return {
                'message': 'username not exist!'
            }, 403
        return {
            'message': '',
            'user': user
        }

    def post(self, name):
        arg = self.parser.parse_args()
        user = {
            'name': name,
            'email': arg['email'],
            'password': arg['password']
        }
        global hello_users
        hello_users.append(user)
        return {
            'message': 'Insert user success',
            'user': user
        }
        

    def put(self, name):
        arg = self.parser.parse_args()
        find = [item for item in hello_users if item['name'] == name]
        if len(find) == 0:
            return {
                'message': 'username not exist!'
            }, 403
        user = find[0]
        user['email'] = arg['email']
        user['password'] = arg['password']
        return {
            'message': 'Update user success',
            'user': user
        }

    def delete(self, name):
        global hello_users
        hello_users = [item for item in hello_users if item['name'] != name]
        return {
            'message': 'Delete done!'
        }

class Users(Resource):
    def get(self):
        return {
            'message': '',
            'users': hello_users
        }

