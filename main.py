from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, flash, jsonify, session, redirect, Markup
import sqlite3
import datetime
import os
import random

app = Flask(__name__)
app.config.from_object(__name__)

file = r'books.csv'
df = pd.read_csv(file, error_bad_lines=False)

df1 = df.sort_values(by="average_rating", ascending=False).head(20)

print(df1)

def getRandomBook():
	book = df['title'].sample(n=1)
	print(book.values[0])
	return book.values[0]

@app.route("/")
def home():
	top20 = df1['title'].unique().tolist()
	book = getRandomBook()
	return render_template("home.html", top20=top20, book=book)

if __name__ == "__main__":
	app.run()