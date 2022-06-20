from flask import Flask, render_template, request
import predictor
import os

app = Flask(__name__)

# set paths to upload folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
wpath = os.path.join(APP_ROOT,"static/weights.80.hdf5")
path_char_to_index = os.path.join(APP_ROOT,"static/char_to_index.json")
mpath = os.path.join(APP_ROOT,"static/tmp/music.mid")

@app.route("/", methods=["GET","POST"])
def predict():
    pred=None
    selected=None
    writepath=None
    if request.method  == "POST":
        seq_length = int(request.form["seqlength"])
        writepath = predictor.predict(seq_length,wpath,path_char_to_index,mpath)
        pred=1
        selected=[seq_length]
    print(writepath)
    return render_template("index.html",pred=pred, selected=selected,writepath=mpath)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)