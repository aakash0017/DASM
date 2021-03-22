
from flask import Flask, render_template, request, redirect, url_for
from sol import solution

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

  


@app.route('/chatbot', methods=['POST'])
def return_name():
    res1=request.form['res1']
    res2=request.form['res_2']
    con=res1+' '+res2
    a=solution(con)
    f=open("sol.txt","w")
    f.write(a)

if __name__ == '__main__':
        app.run(debug=True)
