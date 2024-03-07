import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_data', methods = ['GET'])
def get_all_data():
    with open('data.json') as f:
      data = json.load(f)
    return jsonify({'message': 'success', 'data':data, 'status_code':200})
    
      
  
if __name__== '__main__':
    app.run(debug=True)
    
    
