from flask import Flask, render_template, request
import random
import csv
from faker import Faker

# -*- coding: utf-8 -*-
app = Flask(__name__)
fake = Faker('ko_KR')

names = []

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    match = random.randrange(50, 101)
    f = open('names.csv', "a+", encoding = 'utf-8')
    a = csv.writer(f)
    a.writerow([name1, name2])
    f.close
    return render_template('result.html', name1 = name1 , name2 = name2, match=match)

@app.route("/admin")
def admin():
    f = open('names.csv', 'r')
    rr = csv.reader(f)
    names = rr
    return render_template('admin.html', names = names)
@app.route("/ffaker")
def ffaker():
    name = fake.name()
    return render_template('ffaker.html', name = name)

app.run(host='0.0.0.0', port='8080', debug=True)