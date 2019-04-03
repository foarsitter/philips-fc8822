import os
from functools import wraps

from dotenv.environ import getenv
from flask import Flask, request, redirect, render_template, Response


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """

    env_password = getenv('HTTP_PASSWORD', cast=str)
    env_username = getenv('HTTP_USERNAME', cast=str)

    return username == env_username and password == env_password


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@requires_auth
def index():
    if request.method == 'POST':
        command_str = "irsend SEND_ONCE fc8822 {}".format(request.form['button'])
        print(command_str)
        os.system(command_str)

        if request.is_xhr:
            return Response(status=200)

        return redirect('/')

    return render_template('app.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
