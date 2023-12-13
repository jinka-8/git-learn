from flask import Flask, request, Response
import requests
import redis
from handle import get_contacts_count
#changes
#changes--2
app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

@app.route('/')
def hello():
    redis_client.incr('hits')
    counter = str(redis_client.get('hits'))
    
    return "Welcome to this webpage! This webpage has been viewed " + counter + " time(s)"
#hunter api returns how many contacts have in hunter 
#hunter contacts count
@app.route('/hunter')
def hunter():
    data = request.form.to_dict()

    url = f"https://api.hunter.io/v2/email-count?domain={data.get('domain')}"
    data1 = get_contacts_count(url)

    return {
        'domain_name':data.get('domain'),
        'contacts_count':data1
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
