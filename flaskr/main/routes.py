import pandas as pd
import json

from bson import json_util
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from flaskr.db.mongodb import Mongo
from flaskr.settings import MONGODB_CONN_STR

server = Blueprint('server', __name__)


@server.route('/')
def index():
    return render_template('index.html')

@server.route('/upload')
def upload():
   return render_template('upload_file.html')


@server.route('/upload_file', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        df = pd.read_csv(f.filename)
        payload = json.loads(df.to_json(orient='records'))
        

        mongo_client = Mongo(MONGODB_CONN_STR)
        mongo_client.create_database('test_database', 'matt_test', json.loads(json_util.dumps(payload)))
        
        return payload


# if __name__ == '__main__':
#    app.run(debug = True)
