from flask import Flask, render_template, url_for, request, redirect # THIS LAST ALLOWS US TO SEND AN HTML FILE AS WELL
import csv
app = Flask(__name__)

print(__name__)

@app.route("/")
def my_home(): # here this is a parameter
    return render_template('index.html') 

@app.route("/<string:page_name>") 
def html_page(page_name):
    return render_template(page_name) 

def write_to_file(data):
    with open('database.txt', mode='a') as database: # 'a' MODE MEANS APPEND WHICH ADDS TO THE END OF THE FILE
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2: 
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) # first param is which file to edit, after that the params are for configuration 
        csv_writer.writerow([email, subject, message]) # WE GIVE IT A LIST AND IT ADDS THEM
@app.route('/submit_form', methods=['POST', 'GET']) # GET MEANS BROWSER WANTS TO RECEIVE INFO FROM US AND POST MEANS TO SAVE IT
def login():
    if request.method == 'POST':
        data = request.form.to_dict() # to_dict() TRANSFORMS INTO A DICTIONARY
        write_to_csv(data)
        return redirect('/ThankYou.html' )
    else:
        return 'something went wrong'


# CSV ARE EXCEL FILES

# CSV = COMMA SEPARATED VALUES
# EACH COMMA IN THE FILE REPRESENT A NEW COLUmn




# @app.route("/favicon.ico") 
# def blog2():
#     return "Thsis is my dog"

# @app.route("/blog") #this wprks when we have a different we route
# def hello_world():
#     return "These are my thoughts on blogs"
"""
A FRAMEWORK IS USEFUL SINCE WE DON'T NEED
TO KNOW HOW SOMETHING ACTUALLY WORKS,
HERE WE HAVE THE @app.route DECORATOR 
WORKS WITHOUT OUR UNDERSTANDING
"""

# SINCE FAVICON IS IS ESSENTIAL, IT IS EASY TO IMPLEMENT IN THE FRAMEWORK