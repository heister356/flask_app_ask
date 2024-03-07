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


@app.route('/add_data', methods = ['POST'])
def add_data():
    with open('data.json') as f:
        data = json.load(f)
    new_data = request.json
    data.append(new_data)
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify({'message': 'data send successfully', 'data': data})




@app.route('/fetch_data', methods = ['GET'])
def fetch_data():
    with open('data.json') as f:
        data = json.load(f)
    id = request.args.get('id')
    for i in data:
        if i['id'] == id:
            return jsonify({'data': i,'message':'success'})
    return jsonify({'message':'not found'}), 404
            
    

if __name__ == "__main__":
    app.run(debug=True)
    