from flask import Flask, render_template
from aws_service import AWSService
import json

app=Flask(__name__, template_folder='public')

@app.route("/")
def index():
    data = AWSService().getS3Usage()
    return render_template('index.html', title='S3 Usage', data=data)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    