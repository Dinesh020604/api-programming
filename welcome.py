from flask import Flask, jsonify, request 

app = Flask(__name__) 
  
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 
@app.route('/home/<hello>', methods = ['GET']) 
def disp(hello): 
  
    return jsonify({'data': hello}) 
  
if __name__ == '__main__': 
  
    app.run(debug = True) 
