from flask import Flask, request
import redis
from datetime import datetime
app = Flask(__name__)
r = redis.Redis(host='iamredis', port=6379, decode_responses=True)


@app.route("/")
def index():
    x = request.args.get("x")
    if x:
        if x == "YOUR-NUMBER":
            return "No no, you must replace 'YOUR-NUMBER' with some number like 2 or 123"
        try:
            x = int(x)
        except ValueError:
            return f"Wrong number: {x}\n"
        
        
        rez_sum = x+x
        msg = ""

        if is_redis_available(r) is True:
            r_answ = r.get(rez_sum)
            if r_answ:
                msg = f"First request: {r_answ}"
            else:
                r.set(rez_sum, datetime.strftime(datetime.now(), "%d.%b/%Y %H:%M:%S"))
                msg = "[INFO] Save date in redis DB.."
        else:
            msg = "[ERR] No connection to redis..."

        return f"Result: {x}+{x}={rez_sum}\n\n{msg}\n"
    return "Hi there\n\nYou can call this scrip by this URL http://127.0.0.1/?x=YOUR-NUMBER\n\n"


def is_redis_available(r):
    try:
        r.ping()
    except (redis.exceptions.ConnectionError, ConnectionRefusedError):
        return False
    return True



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
