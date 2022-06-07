#MAKING URL DYNAMIC

from flask import Flask,redirect, url_for

#Constructor of Flask Object

app=Flask(__name__)

#HOME PAGE

@app.route('/')
def home():
    return "WELCOME TO THE USERS "


#URL BUILDING WITH MARKS

@app.route('/success/<int:marks>')
def success(marks):
    return "Student is passed with marks "+str(marks)


@app.route('/failure/<int:marks>')
def failure(marks):
    return "Student is failed with marks "+str(marks)



#RESULT PAGE LOGIC FOR MAKING URLS DYNAMIC 
@app.route('/result/<int:score>')
def result(score):
    res=""
    if score>=40:
        res="success"
    else:
        res="failure"    

    #REDIRECT METHOD FOR GETING RETURN TO DESIREFD URL

    return redirect(url_for(res,marks=score))    

if __name__==('__main__'):
    app.run(debug=True)























