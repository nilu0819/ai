from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'good morinings'

app.run(host='127.0.0.1')