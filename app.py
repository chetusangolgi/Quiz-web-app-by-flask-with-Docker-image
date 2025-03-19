from flask import Flask, render_template, request
from supabase import create_client, Client

count=0

app= Flask(__name__)

SUPABASE_URL = "https://ftepvxsjclqyzzdeiwdi.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ0ZXB2eHNqY2xxeXp6ZGVpd2RpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIzNjEwNjgsImV4cCI6MjA1NzkzNzA2OH0.daHwiK5wNXFLIiI8I6sawLHDyOHzeQTglVCNXOfc2zc"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

mail=""
name=""


#INDEX

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz1', methods=['POST'])
def quiz1():
    global name
    global mail
    name=request.form['name']
    mail=request.form['mail']
    return render_template('quiz1.html', name=name)

#1

@app.route('/quiz1/submit',methods=['POST'])
def submit1():
    selected_option = request.form.get('answer')  
    correct_answer = "B"  
    global count
    if selected_option == correct_answer:
        result = "Correct! "
        count+=1
    else:
        result = "Wrong answer! "

    return render_template('quiz1.html', result=result, correct_answer=correct_answer,name=name,submitted=True)

@app.route('/quiz2', methods=['POST'])
def quiz2():
    return render_template('quiz2.html', name=name)

#2

@app.route('/quiz2/submit',methods=['POST'])
def submit2():
    selected_option = request.form.get('answer')  
    correct_answer = "A"  
    global count
    if selected_option == correct_answer:
        result = "Correct! "
        count+=1
    else:
        result = "Wrong answer! "

    return render_template('quiz2.html', result=result, correct_answer=correct_answer,name=name,submitted=True)

@app.route('/quiz3', methods=['POST'])
def quiz3():
    return render_template('quiz3.html', name=name)

#3

@app.route('/quiz3/submit',methods=['POST'])
def submit3():
    selected_option = request.form.get('answer')  
    correct_answer = "D"  
    global count
    if selected_option == correct_answer:
        result = "Correct! "
        count+=1
    else:
        result = "Wrong answer! "

    return render_template('quiz3.html', result=result, correct_answer=correct_answer,name=name,submitted=True)

@app.route('/quiz4', methods=['POST'])
def quiz4():
    return render_template('quiz4.html', name=name)

#4

@app.route('/quiz4/submit',methods=['POST'])
def submit4():
    selected_option = request.form.get('answer')  
    correct_answer = "B"  
    global count
    if selected_option == correct_answer:
        result = "Correct! "
        count+=1
    else:
        result = "Wrong answer! "

    return render_template('quiz4.html', result=result, correct_answer=correct_answer,name=name,submitted=True)

@app.route('/quiz5', methods=['POST'])
def quiz5():
    return render_template('quiz5.html', name=name)

#5

@app.route('/quiz5/submit',methods=['POST'])
def submit5():
    selected_option = request.form.get('answer')  
    correct_answer = "C"  
    global count
    if selected_option == correct_answer:
        result = "Correct! "
        count+=1
    else:
        result = "Wrong answer! "

    return render_template('quiz5.html', result=result, correct_answer=correct_answer,name=name,submitted=True)

#RESULT

@app.route('/result', methods=['POST'])
def result():
    data = {
        "name": name,
        "result": count,
        "email":mail
    }
    supabase.table("quiz_results").insert(data).execute()
    return render_template('result.html', name=name,count=count)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)