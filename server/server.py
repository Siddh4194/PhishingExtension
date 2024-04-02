from flask import Flask, redirect, url_for, request,jsonify
from main import main
from main import get_prediction_from_url

app = Flask(__name__)




# Creating the checkPhishing request endpoint for the detection
@app.route("/CheckPhishing", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        state =  get_prediction_from_url(request.json['url'])
        print(state)
        return jsonify({"result": state})
        # return redirect(url_for('success', name=user))
    else: 
        url = request.args['url']
        resp = Flask.response_class((url)) 
        print(main(url))
        print(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

# created the uui for the user
@app.route("/", methods=['GET'])
def check():
    if request.method == 'GET':
        print('request detected')
        user = request.args.get('nm', '')  # Get the value of 'nm' from the query parameters
        return f"Hello You entered to the world of phishing detection, {user}!"
    
if __name__ == '__main__':
    app.run(debug=True)
