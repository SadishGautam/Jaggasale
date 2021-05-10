from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import medium
import pandas as pd
import sqlite3


app = Flask(__name__)
CORS(app)

# app = flask.Flask(__name__, template_folder='templates')










#API endpoint
@app.route('/recommendproperty', methods=['GET'])
def process_request():


    result_recommend=medium.recommend_Property(request.args.get('Property_ID'))

    return jsonify(result_recommend)



@app.route('/property', methods=['GET'])
def process_requests():
    result_recommend=medium.get_Property(request.args.get('Property_ID'))
    return jsonify(result_recommend)



if __name__ == '__main__':

    conn = sqlite3.connect('../db.sqlite3', isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM jaggasale_item", conn)
    db_df.to_csv('realestate.csv', index=False)
    app.run()
