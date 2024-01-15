# -*- coding: utf-8 -*-

from Match_Function import findMatch as fM
import webbrowser
import fetchAndPrint as fp
import dictionaryGen as dG
from flask import Flask, render_template, request #things we need
from sqlite3 import connect
conn = connect('DCMB_Faculty_V5.db')
curs = conn.cursor()
app = Flask(__name__) #initializes flask?


webbrowser.open_new_tab('http://127.0.0.1:5000/')
@app.route('/',methods=['GET','POST']) #designates what path(url) to take
def DCMBSS():
    if request.method=='GET':
        return render_template('DCMBSS.html')
@app.route('/answersDCMB',methods=['GET','POST'])#this path is taken after hitting submit button. Path is designated in html template
def answersDCMB():
    if request.method=='POST':
        studentDict = dict(request.form)
        for key,value in studentDict.items():
            if len(value) == 1:
                studentDict[key] = value[0]
            elif len(value) > 1:
                studentDict[key] = set(value)
            else:
                pass
    surveyPurpose=request.form['Purpose']

    if len(request.form)<11:
        return render_template('Answers.html')
    else:
        next
    if surveyPurpose=='rotation':
        rotateDict=dG.OpenGradDict(curs)
        absoluteDict=rotateDict
    elif surveyPurpose=='prelim':
        prelimDict=dG.PrelimDict(curs)
        absoluteDict=prelimDict
    else:
        thesisDict=dG.ThesisDict(curs)
        absoluteDict=thesisDict
    email, score = fM(studentDict, absoluteDict)
    matches = fp.fetchProfile(curs, email)
    prof1 = f'Match #1 is Dr. {matches[email[0]][0]} {matches[email[0]][1]}. Email: {email[0]}'
    des1 = f'Lab Profile: {matches[email[0]][2]}'
    prof2 = f'Match #2 is Dr. {matches[email[1]][0]} {matches[email[1]][1]}. Email: {email[1]}'
    des2 = f'Lab Profile: {matches[email[1]][2]}'
    prof3 = f'Match #3 is Dr. {matches[email[2]][0]} {matches[email[2]][1]}. Email: {email[2]}'
    des3 = f'Lab Profile: {matches[email[2]][2]}'
    prof4 = f'Match #4 is Dr. {matches[email[3]][0]} {matches[email[3]][1]}. Email: {email[3]}'
    des4 = f'Lab Profile: {matches[email[3]][2]}'
    prof5 = f'Match #5 is Dr. {matches[email[4]][0]} {matches[email[4]][1]}. Email: {email[4]}'
    des5 = f'Lab Profile: {matches[email[4]][2]}'
    
    return render_template('answersDCMB.html', fProf1=prof1, fProf2=prof2, fProf3=prof3, fProf4=prof4, fProf5=prof5, fDes1=des1, fDes2=des2, fDes3=des3, fDes4=des4, fDes5=des5)



if __name__== "__main__":
    app.run()