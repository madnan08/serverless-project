from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://admin:madnan08@database-1.ctgasa8q401c.us-east-1.rds.amazonaws.com:1433/database-1'
db = SQLAlchemy(app)

from app import routes
