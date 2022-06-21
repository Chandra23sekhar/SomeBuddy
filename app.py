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
    q_no = db.Column(db.String[3])
db.create_all()

nmm = ""

@app.route('/', methods=['GET', 'POST'])
def home():
    # if request.method == 'POST':
    #     nm = request.form.get('buddy_name')
    #     nmm = nm
    #     return render_template('home.html')
    return render_template('home.html')
    

@app.route('/q1', methods=['GET', 'POST'])
def q1():
    if request.method == 'POST':
        ans = request.form.get('yes-opt')
        new_row = User(score=ans, q_no = 'q1')
        db.session.add(new_row)
        db.session.commit()
    return render_template('ques1.html')

@app.route('/q2', methods=['GET', 'POST'])
def q2():
    if request.method == 'POST':
        ans = request.form.get('yes-opt')
        print(ans)
        new_row = User(score=ans, q_no = 'q2')
        db.session.add(new_row)
        db.session.commit()
    return render_template('ques2.html')

@app.route('/q3', methods=['GET', 'POST'])
def q3():
    if request.method == 'POST':
        ans = request.form.get('yes-opt')
        print(ans)
        new_row = User(score=ans, q_no = 'q3')
        db.session.add(new_row)
        db.session.commit()
    return render_template('ques3.html')

@app.route('/q4', methods=['GET', 'POST'])
def q4():
    if request.method == 'POST':
        ans = request.form.get('yes-opt')
        print(ans)
        new_row = User(score=ans, q_no = 'q4')
        db.session.add(new_row)
        db.session.commit()
    return render_template('ques4.html')

@app.route('/q5', methods=['GET', 'POST'])
def q5():
    if request.method == 'POST':
        ans = request.form.get('yes-opt')
        print(ans)
        new_row = User(score=ans, q_no = 'q5')
        db.session.add(new_row)
        db.session.commit()
    return render_template('ques5.html')

@app.route('/q6', methods=['GET', 'POST'])
def q6():
    if request.method == 'POST':
        ans = request.form.get('yes-opt')
        print(ans)
        new_row = User(score=ans, q_no = 'q6')
        db.session.add(new_row)
        db.session.commit()
    return render_template('ques6.html')

@app.route('/q7', methods=['GET', 'POST'])
def q7():
    if request.method == 'POST':
        ans = request.form.get('yes-opt')
        print(ans)
        new_row = User(score=ans, q_no = 'q7')
        db.session.add(new_row)
        db.session.commit()
    return render_template('ques7.html')

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

'''Chat Bot '''
@app.route('/home', methods=['GET', 'POST'])
def chatbot():
    # if request.method == 'POST':
    #     return render_template('index.html', title="Chat-Bot", buddy_name=nm)
    return render_template('index.html', title='Chat Bot', buddy_name='SomeBuddy')


@app.route("/get", methods=['GET', 'POST'])
def get_bot_response():
    userText = request.args.get('msg')
    return str(CBL.chat_bow(userText.lower()))
'''End'''

@app.route('/result', methods=['GET', 'POST'])
def result():
    l = []
    ll = User.query.filter(User.score).all()
    for ele in ll:
        l.append(ele.score)
    
    a = calc(l)
    return render_template('result.html', my_pred=a)


def calc(l):
   
    pred = []
    dictionary = {0:'PTSD', 1:'Bpd', 2:'Bipolar Disorder', 4:'Anxiety', 5:'Depression', 6:'Schizophrenia'}
    pred.append(( int(l[0]) + int(l[3]) + int(l[4]))*0.66) #ptsd
    pred.append((int(l[2]) + int(l[4]))*0.5) #bpd
    pred.append((l[0] + l[2] + l[3] + l[4])*(1/4)) #bipr
    pred.append((l[4] + l[2])*(0.5)) #anx
    pred.append( l[0] + l[4] *(0.5)) #dep
    pred.append((l[0] + l[2] + l[3] + l[4])*(1/5)) #sch
    m_ele = max(pred)
    index = pred.index(m_ele)
    return dictionary[index]


if __name__ == '__main__':
    app.run(debug=True)