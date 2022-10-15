# pylint: disable=C0303
# pylint: disable=C0301
# pylint: disable=C0116
# pylint: disable=C0103
# pylint: disable=C0114
from flask import Flask  
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__, static_url_path='/static')

# a route to display our html page gotten from [react-chat-widget](https://github.com/mrbot-ai/rasa-webchat)
@app.route("/")
def index():  
    return render_template('index.html')

# run the application
if __name__ == "__main__":  
    app.run(host="0.0.0.0", debug=True)
