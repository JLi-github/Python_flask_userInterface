# -*- coding: utf-8 -*-


from flask import Flask, render_template, redirect, request
import webbrowser
app = Flask(__name__, template_folder='templates')
webbrowser.open_new_tab('http://127.0.0.1:5000/')
@app.route('/')
def DCMBSS():
    # this is a comment, just like in Python
    # note that the function name and the route argument
    # do not need to be the same.
    return render_template('DCMBSS.html')

if __name__ == '__main__':
    app.run(debug=True)



if __name__== "__main__":
    app.run()