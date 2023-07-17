from flask import Flask
app = Flask(__name__)

@app.route('/')
def app_home():
    return 'Python Flask application on OpenShift!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)