import requests
import boto.sqs
from boto.sqs.message import RawMessage
import json


from flask import Flask, jsonify, abort, make_response, request

application = Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
application.debug=True

@application.route('/', methods=['GET'])
def welcome():
    return jsonify(richie="Loves little Daphne")

@application.route('/sign_up', methods=['POST'])
def sign_up():
    if not request.json or 'to' not in request.json \
            or 'body' not in request.json:
        abort(400)
    email = {
        'to': request.json['to'],
        'body': request.json['body'],
        'subject': request.json.get('subject', "Mailgun Test"),
        'from': request.json.get('from', "Test <test@balancedpayments.com>"),
    }
    try:
        write_to_que(email)
    except Exception, e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"email": email}), 201


def write_to_que(data):
    conn = boto.sqs.connect_to_region("us-east-1")
    my_queue = conn.get_queue('email_queue')
    # Put the message in the queue
    m = RawMessage()
    m.set_body(json.dumps(data))
    status = my_queue.write(m)

if __name__ == '__main__':
    application.run(host='0.0.0.0')