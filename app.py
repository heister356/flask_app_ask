import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/get_data', methods = ['GET'])
def get_all_data():
    with open('data.json') as f:
      data = json.load(f)
    return jsonify({'message': 'success', 'data':data, 'status_code':200})
    
      


@app.route('/paginated_data', methods=['POST'])
def paginated_data():
    with open('data.json') as f:
        data = json.load(f)
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    if page.isdigit() and per_page.isdigit():
            page = int(page)
            per_page = int(per_page)
            return jsonify({ 'data' : data[(page - 1) * per_page:page * per_page],
                            'page' : page})
    else:
            return jsonify({'error': 'Invalid page or per_page values'}), 400



if __name__ == "__main__":
    app.run(debug=True)