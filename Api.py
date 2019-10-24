# Import framework
from flask import Flask, request
from flask_restful import Resource, Api
from Squared import Squared_Function
from user import User

# Instantiate the app
app = Flask(__name__)
api = Api(app)


class Info(Resource):
    def get(self):
        return {
            'Message': ["Welcome on the Diego API!!!!"],
            "Available endpoints": ["/participants", "/squared?number=XXXX", "/authentificate?username=XXXX&password=XXXXXXX"]
        }

class Participants(Resource):
    def get(self):
        return {
            'participants': ['Kikou', 'Nicolas', 'Jerome', 'Julien', 'Elise', 'Christophe - who invited him? Urgh. That guy.', 'Joelle', 'Farah', 'Felix', 'Alex', 'Roxane', 'Marc']
        }



class Squared(Resource):
    def get(self):
        number=float(request.args.get('number'))
        squared_result=Squared_Function(number)
        return {
            'squared number': [str(squared_result)]
        }


class Authentificate(Resource):
    def get(self):
        username=request.args.get('username')
        password = request.args.get('password')
        LoggingUser=User(username, password)
        return {
            'authentification status': [LoggingUser.authentificate()]
        }



# Create routes
api.add_resource(Info, '/') #To test locally: http://localhost:5000/

# Create routes
api.add_resource(Participants, '/participants') #To test locally: http://localhost:5000/participants

# Create routes
api.add_resource(Squared, '/squared')   #To test locally: http://localhost:5000/squared?number=5

# Create routes
api.add_resource(Authentificate, '/authentificate')   #To test locally: http://localhost:5000/authentificate?username=Diego&password=Agilytic123

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)