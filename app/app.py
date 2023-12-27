from flask import Flask, request, jsonify
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy import MetaData, Table, Column, Integer, String

from flask_sqlalchemy import SQLAlchemy

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

metadata_obj = MetaData()

app = Flask(__name__)

if __name__ == "__main__":

    app.run()