from flask import Flask
import redis
#flask app with redis pratice
app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

@app.route('/')
def hello():
    redis_client.incr('hits')
    counter = str(redis_client.get('hits'))
    
    return "Welcome to this webpage! This webpage has been viewed " + counter + " time(s)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
