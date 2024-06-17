from flask import Flask, render_template, url_for, request, redirect
import os
import csv

app = Flask(__name__)


@app.route('/')#standard homepage
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as records:
            for k,v in data.items():
                records.write(f'{k}:{v}\n\n')


def write_to_csv(data):
    with open('database2.csv', newline = '', mode ='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter= ',', quotechar= '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods =['POST','GET'] )
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')

'''
@app.route('/index.html')#standard homepage
def home_page_2():
    return render_template('index.html')  #looks for template folder and creates based off of html file@app.route('/user/<username>')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contacts.html')
def contacts():
    return render_template('contacts.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route("/hello")  #provides the website branch
def hello_world():  #returns individual function for the page
    return "<center><p>Hello,<br><b>World!</b></p></center>"  #builds the html file based off of what text u put in

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {(username)}'

@app.route('/experiment/<username>')
def jinja_explorer(username=None):
    #using an html file with {{}} to combine python with html in order to dynamically change the site
    return render_template('jjabrams.html', name = username)
'''