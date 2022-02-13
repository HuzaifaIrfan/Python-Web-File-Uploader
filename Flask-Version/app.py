from flask import render_template, request, make_response, jsonify,Flask



# from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/')
def upload_file():
   return render_template('upload_video.html')

@app.route("/upload-video", methods=["GET", "POST"])
def upload_video():

    if request.method == "POST":

        file = request.files["file"]

        print("File uploaded")
        print(file)

        res = make_response(jsonify({"message": "File uploaded"}), 200)

        return res

    return render_template("upload_video.html")


	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)