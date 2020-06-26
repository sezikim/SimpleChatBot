from flask_restful import Resource,reqparse,abort

GreetMessage = ['Hi', 'Hello' 'hi', 'hello']

HyunJunInfo = {
	'name':'HyunJun',
	'location':'Suwon',
	'live':'Suwon',
	'located':'Suwon',
	'age':'20s',
	'old':'20s',
	'university':'Ajou',
	'gender':'Male'
}

def abort_if_info_doesnt_exist(info_index):
	if info_index not in HyunJunInfo:
		abort(404, message="Sorry, I dont know.")

parser = reqparse.RequestParser()
parser.add_argument('sentence', required=True, type=str, help='sentence is needed')

class HyunJunBot(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sentence', required=True, type=str, help='sentence is needed')
        args = parser.parse_args()
        if args['sentence'] in GreetMessage:
        	return {'answer': 'Hello', 'question': args['sentence']}

        for match in args['sentence'].split():
        	if match in HyunJunInfo:
        		return {'answer': HyunJunInfo[match], 'question': args['sentence']}
        abort_if_info_doesnt_exist(args['sentence'])

from flask import Flask
from flask_restful import Api

app = Flask('HyunJun Chatbot')
api = Api(app)
api.add_resource(HyunJunBot, '/chatbot')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
