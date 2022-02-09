"""
Flask
"""
import os
from flask import Flask  # Import the Flask class


# create an instace of this class. And storing it
# in a variable called "app"
# the first argument of the Flask class is the
# name of the application's module - our package.
#  __name__ is a build in py variable.
# Flask needs this so that knows where to look for
# template and static files


app = Flask(__name__)


@app.route("/")
# use rout decorator to tell Flask what URL
# should trigger the function that follows
def index():
    """
     function called index, which returns the string Hello World
     when we try to browse to the root directory, as indicated
     by the "/", then Flask triggers the index function underneath
    """
    return"Hello, world"


if __name__ == "__main__":
    # __main__ is the name of the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        # we are using os module from standard library to get IP enviroment
        # variable if it exists, but set a default varibale if it's not found
        port=int(os.environ.get("PORT", "5000")),
        # for port - 5000 common port used by flask
        debug=True)
# that will allow us to debug our code much easier
# during the development stage
# we want to run our app using the arguments that we've
# passing inside of this statement
