import subprocess
import sqlite3
from flask import Flask,request,render_template,redirect
import os
# import requests
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return redirect('http://127.0.0.1:5000/home')

@app.route('/')
def home():
    return redirect('http://127.0.0.1:5000/home')

@app.route('/home')
def my_form():
    return render_template('home.html')

@app.route('/home', methods=['POST'])
def my_form_post():
    company = request.form['input1']
    street = request.form['input2']
    postcode = request.form['input3']

    if request.method == 'POST':
        if company!='':
           with open('company.txt', 'a') as f:
                f.write(str(company)+"\n")
        if street != '':
           with open('street.txt', 'a') as f:
               f.write(str(street)+"\n")
        if postcode != '':
           with open('postcode.txt', 'a') as f:
               f.write(str(postcode)+"\n")
    # return render_template('home.html', find=find,near=near)
    return redirect('http://127.0.0.1:5000/home')


@app.route('/run')
def run():
    """
    Run spider in another process and store items in file. Simply issue command:

    > scrapy crawl dmoz -o "output.json"

    wait for  this command to finish, and read output.json to client.
    """

    # p = subprocess.Popen(...)
    # """
    # A None value indicates that the process hasn't terminated yet.
    # """
    # poll = p.poll()
    # if poll == None:


    spider_name = "moz"
    if(os.stat('company.txt').st_size != 0 and os.stat('street.txt').st_size != 0 and os.stat('postcode.txt').st_size != 0):
        subprocess.check_output(['scrapy', 'crawl', spider_name])
        with open('company.txt', "w"):
            pass
        with open('street.txt', "w"):
            pass
        with open('postcode.txt', "w"):
            pass
    else:
        print('file empty')

    return redirect('http://127.0.0.1:5000/view')


    # with open("output.json") as items_file:
    #     return items_file.read()

# @app.route("/view")
# def view():
#     con = sqlite3.connect("searchdetail.db")
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.execute("select * from detail")
#     rows = cur.fetchall()
#     return render_template("index.html",rows = rows)

if __name__ == '__main__':
    app.run(debug=True)