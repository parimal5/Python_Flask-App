from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Welcome to My Simple Python Flask App!</h1><p>This app is used to practice build and deployment with Jenkins, Kubernetes, and Ansible.</p>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

