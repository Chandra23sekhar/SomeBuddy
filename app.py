from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import json 
import urllib.request
import BusinessLayer.chatbotBL as CBL


app = Flask(__name__)

#Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#Creating a database model
class User(db.Model):
    snNo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Integer)
    disease = db.Column(db.String[20])
db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/q1', methods=['GET', 'POST'])
def q1():
    if request.method == 'POST':
        ans = request.form.get('yes-opt')
        print(ans)
    return render_template('q1.html')

@app.route('/q2')
def q2():
    return render_template( 'ques2.html')

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

'''Chat Bot '''
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    return render_template('index.html', title="Chat-Bot ")

@app.route("/get", methods=['GET', 'POST'])
def get_bot_response():
    userText = request.args.get('msg')
    return str(CBL.chat_bow(userText.lower()))
'''End'''

if __name__ == '__main__':
    app.run(debug=True)