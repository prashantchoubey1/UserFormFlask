from flask import Flask, render_template, request
import sqlite3
import logging

logging.basicConfig(filename='record.log', level=logging.DEBUG)
app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template("home.html")

@app.route("/")
def fill_form():
    return render_template("index.html")
    
@app.route('/add_record',methods = ['POST', 'GET'])
def add_record():
   if request.method == 'POST':
      try:
        first_name1 = request.form.get("fname")
        last_name1 = request.form.get("lname")
        email1 = request.form.get("email")
        password1 = request.form.get("pass")
         
        with sqlite3.connect("flask_db.sqlite") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO UserData (email,first_name,last_name,password) VALUES (?,?,?,?)",
                        (email1,first_name1,last_name1,password1) )
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      finally:
         return render_template("result.html",msg = msg)
         con.close()

if __name__ == '__main__':
  app.run(debug=True)