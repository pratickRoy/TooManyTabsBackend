from final_model import cluster

from flask import Flask, request, jsonify

app = Flask('tmt')
@app.route('/classify', methods=['POST'])
def classify():
    d = request.json
    resp = cluster(d.get('data'), clusters=d.get('nclusters'))
    return jsonify(resp)

app.run(debug=True)
