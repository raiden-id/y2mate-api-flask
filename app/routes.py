from app import app
from app.controllers import last_data,search_data

@app.route('/')
def home():
        return "hai, konan is here!"

@app.route('/api/data/<string:data>')
def get_data_from_k(data):
    return last_data(data)

@app.route('/api/search/<string:query>')
def get_data_search(query):
	return search_data(query)

