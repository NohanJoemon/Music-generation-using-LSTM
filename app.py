from flask import Flask, render_template, request, send_file
import predictor
import os

app = Flask(__name__)

# set paths to upload folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
wpath = os.path.join(APP_ROOT,"static/weights.80.hdf5")
path_char_to_index = os.path.join(APP_ROOT,"static/char_to_index.json")
mpath = os.path.join(APP_ROOT,"tmp/music.mid")

@app.route("/", methods=["GET","POST"])
def predict():
    pred=None
    selected=None
    if request.method  == "POST":
        seq_length = int(request.form["seqlength"])
        predictor.predict(seq_length,wpath,path_char_to_index,mpath)
        pred=1
        selected=[seq_length]
        return render_template("index.html",pred=pred, selected=selected)
        
    return render_template("index.html",pred=pred, selected=selected)

@app.route("/download", methods=["GET","POST"])
def download():
    return send_file(mpath, as_attachment=True)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)