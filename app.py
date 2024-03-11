import json
from flask import Flask, jsonify, request

app = Flask(__name__)

def load_data():
    with open('data.json') as f:
        data = json.load(f)
    return data


@app.route('/get_data', methods=['GET'])
def get_all_data():
    data = load_data()
    return jsonify({'message': 'success', 'data': data, 'status_code': 200})


@app.route('/paginated_data', methods=['POST'])
def paginated_data():
    data = load_data()
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    if page.isdigit() and per_page.isdigit():
        page = int(page)
        per_page = int(per_page)
        return jsonify({'data': data[(page - 1) * per_page:page * per_page], 'page': page})
    else:
        return jsonify({'error': 'Invalid page or per_page values'}), 400


@app.route('/add_data', methods=['POST'])
def add_data():
    data = load_data()
    new_data = request.json
    data.append(new_data)
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify({'message': 'data sent successfully', 'data': data}), 201


@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    data = load_data()
    user_id = request.args.get('id')
    for item in data:
        if item['id'] == user_id:
            return jsonify({'data': item, 'message': 'success'})
    return jsonify({'message': 'not found'}), 404

from flask import jsonify, request

@app.route('/update_name/<string:user_id>', methods=['PATCH'])
def update_name(user_id):
    data = load_data()
    name = request.args.get('name')
    for item in data:
        if item['id'] == user_id:
            item['name'] = name
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
            return jsonify({'message': 'success'}), 200
    return jsonify({'message': 'not found'}), 404



@app.route('/remove_data', methods=['DELETE'])
def remove_data():
    data = load_data()
    list_id = request.args.get('id')
    for item in data:
        if item['id'] == list_id:
            data.remove(item)
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
            return jsonify(data), 200
        return jsonify({'error':'no matching id'}), 400


if __name__ == "__main__":
    app.run(debug=True)
