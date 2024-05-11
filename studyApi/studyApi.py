from flask import *
import os
import pymongo
from bson import json_util, ObjectId
import setupLog
import logging
import traceback


setupLog.setupLog()
logger = logging.getLogger('study.studyApi')

db_url = 'mongodb+srv://hirendrakoche1:nCfLGcYH3NEswK4M@hkstudy.jq02hf0.mongodb.net/?retryWrites=true&w=majority&appName=HKStudy'
client = pymongo.MongoClient(db_url)
db = client['HKMongoDB']
logger.info("Established DB connections.")

app = Flask(__name__)

@app.errorhandler(500)
def internal_error(error):
    return Response(traceback.format_exc(), status=500, mimetype="text/html")

@app.route('/')
def home():
    logger.info("Inside home function")
    return '<h1>Welcome<h1>'

@app.route("/api/v1/student", methods=['GET'])
def students():
    logger.info("Inside students function")
    try:
        data = json_util.dumps(db.students.find())
        logger.debug(f"Student data => {data}")
        return Response(data, mimetype='application/json')
    except Exception as e:
        logger.exception(e)
        return internal_error(e)
    finally:
        logger.info("Exit students function")
    
@app.route('/api/v1/student/<id>', methods=['GET'])
def student(id):
    logger.info("Inside student function")
    try:
        data = json_util.dumps(db.students.find({'_id': ObjectId(id)}))
        logger.debug(f"Student data => {data}")
        return Response(data, mimetype='application/json')
    except Exception as e:
        logger.exception(e)
        return internal_error(e)
    finally:
        logger.info("Exit student function")
    
@app.route('/api/v1/student', methods = ['POST'])
def createStudent():
    logger.info("Inside createStudent function")
    try:
        student = request.json
        logger.debug(f"Request Body => {student}")
        db.students.insert_one(student)
        logger.info("Record created in DB")
        return Response("Record created")
    except Exception as e:
        logger.exception(e)
        return internal_error(e)
    finally:
        logger.info("Exit createStudent function")

@app.route('/api/v1/student/<id>', methods = ['PUT'])
def updateStudent(id):
    logger.info("Inside updateStudent function")
    try:
        query = {"_id": ObjectId(id)}
        logger.debug(f"DB query => {query}")
        student = request.json
        logger.debug(f"Request body => {student}")
        db.students.update_one(query, {"$set": student})
        logger.info("Record updated in DB")
        res = Response(json_util.dumps({"Message": "Success"}))
        res.content_type = "application/json"
        res.content_encoding = "utf-8"
        res.mimetype = "application/json"
        res.add_etag()
        logger.info(f"Response => {res}")
        return res
    except Exception as e:
        logger.exception(e)
        return internal_error(e)
    finally:
        logger.info("Exit updateStudent function")

if __name__ == '__main__':
    logger.info("Starting server")
    port = int(os.environ.get("PORT", 443))
    app.run(debug=True, host='0.0.0.0', port=port, ssl_context="adhoc")