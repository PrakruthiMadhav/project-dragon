from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/verify/operation', methods=['GET'])
def verify():
    return jsonify({"health": "All systems operational"})

if __name__ == '__main__':
    app.run(debug=True)
