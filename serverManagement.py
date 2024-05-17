import pymongo
import pandas as pd
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

@st.cache_resource
def init_connection():
    uri = st.secrets["mongo"]
    print(uri["host"])
    return MongoClient(uri["host"], server_api=ServerApi('1'))

client = init_connection()


def get_user_data():
    db = client.Inventory
    items = db.Users.find()
    items = list(items)
    return items

def register_user(mail, name, password, id):
    db = client.Inventory
    collection = db["Users"]
    user_data = {"mail": mail, "name": name, "password": password, "id": id, "admin": False}
    collection.insert_one(user_data)

def find_user_data(mail):
    db = client.Inventory
    collection = db["Users"]
    user_data = collection.find_one({"mail": mail})
    return user_data

def get_company_name():
    db = client.Inventory
    collection = db["CompanyName"]
    projection = {"_id": 0}
    company_name = collection.find({}, projection)
    company_name = list(company_name)
    return company_name


