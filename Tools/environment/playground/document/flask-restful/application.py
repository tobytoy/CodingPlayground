from flask import Flask, request
from flask_restful import Api
from common import middleware
from resources import hello


app = Flask(__name__)
app.wsgi_app = middleware.printMiddleware(app.wsgi_app)

api = Api(app)
api.add_resource(hello.User, "/hello/user/<string:name>")
api.add_resource(hello.Users, "/hello/users")

###############################
##     Handling the logs
@app.route("/logs", methods=['GET'])
def logsGet():
    log_type = request.values.get('log_type')
    log_text = request.values.get('log_text')
    if log_type == 'info':
        app.logger.info(log_text)
    elif log_type == 'warning':
        app.logger.warning(log_text)
    elif log_type == 'error':
        app.logger.error(log_text)
    else:
        return {
                'message': 'the log type not exist!'
            }, 403
    return {
            'message': 'Done.'
        }, 200


#####################################
##     Check The Network Connect
@app.route("/", methods=['GET', 'POSE'])
def rootHome():
    return {
            'message': 'Welcome.'
        }, 200

if __name__ == "__main__":    
    app.run(host = '127.0.0.1', port = 5000)
