from flask import Flask, request, url_for, redirect
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def PogChamp():
    lul = request.form
    print(lul)
    return redirect("http://127.0.0.1:8081/view1", code=302)