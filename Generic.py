# import random 

# class Table:
#     def __init__(self, table):
#         self.table = table
#     # self.numOfRows = numOfRows
#     # self.numOfColumns = numOfColumns
#     # self.rows = rows 
#     # self.columns = columns
from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home_page():
   return render_template('basic.html')

if __name__ == '__main__':
    #set debug to false if using in production environment
   app.run(app.run(debug = True, host='0.0.0.0'))