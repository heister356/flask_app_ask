from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/getdata', methods = ['GET'])
def data_return():
    with open('data.json','r') as f:
      data = json.load(f)
      return jsonify({'message': 'success', 'data':data, 'status_code':200})
    
      
  
if __name__== '__main__':
    app.run(debug=True)