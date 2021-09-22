# app.py

from flask import Flask, jsonify, render_template
from flask.helpers import make_response
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/api/demo/')
def api_demo():
    f = open('./visweb/tmp.json',) 
    data = json.load(f)
    ans = []
    for key in data:
        ans += [{"tot":data[key][0],"info" : data[key][2],"mask":data[key][1],"desc" : data[key][3]}]
    f.close()
    return jsonify(ans)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
