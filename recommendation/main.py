from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import medium


app = Flask(__name__)
CORS(app)

# app = flask.Flask(__name__, template_folder='templates')


#API endpoint
@app.route('/recommendproperty', methods=['GET'])
def process_request():
    result_recommend=medium.recommend_Property(request.args.get('Property_ID'))

    return jsonify(result_recommend)




if __name__ == '__main__':
    app.run()
