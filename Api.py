# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Participants(Resource):
    def get(self):
        return {
            'partcipants': ['Jonathan', 'Nicolas', 'Jerome', 'Julien', 'Elise', 'Christophe', 'Joelle', 'Farah', 'Felix', 'Alex', 'Roxane', 'Marc']
        }

class Professor(Resource):
    def get(self):
        return {
            'professor': ['Moi moi et toi et qqun et toiiiii']
        }

# Create routes
api.add_resource(Participants, '/participants')

# Create routes
api.add_resource(Professor, '/professor')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)