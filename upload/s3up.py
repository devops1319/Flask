
from flask import Flask, render_template, request
import boto3
app = Flask(__name__)
from werkzeug.utils import secure_filename
ACCESS_KEY = 'AKIAYOTRUKBAV6ESOUUN'
SECRET_KEY = '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'


s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

BUCKET_NAME='sepocbucket'

@app.route('/')  
def home():
    return render_template("storage.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "

    return render_template("storage.html",msg =msg)




if __name__ == "__main__":
    
    app.run(debug=True)

