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
            'professor': ['now I work on airflow']
        }

class TopoHebdo(Resource):

    def get(self):
        message = """
        Hello Jon, Chris and Julien. This dummy Api is currently hosted on an Azure virtual machine I launched.
        The Api is really basic but what is really important is that I applied all the best industrialization practices I learnt at Axa.

        After almost one year at Axa I would like to share what I learned with the rest of the team. Does a training mid-october sound like a good idea?

        Cheers,

        Diego.

        """

        return {
            'Message': [message],
            'Topics I would like to tackle': ['Working on linux', "Small github recap" ,'Best practices in deployment using Jenkins',  'Scheduling on linux using Airflow']
        }

# Create routes
api.add_resource(Participants, '/participants')

# Create routes
api.add_resource(Professor, '/professor')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)