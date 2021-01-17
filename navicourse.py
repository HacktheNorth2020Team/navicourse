from flask import Flask, render_template, url_for, request, flash, \
     redirect, abort, session
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm
from sqlalchemy import create_engine
from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy.dialects.postgresql import UUID
import uuid
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)

# Read the dataset
ds = pd.read_csv(os.path.join("csv course files", "Udacity.csv"))
# Vectorizer, deletes non-important words (e.g. the, a, and)
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(ds['description'])

# Cosine Similarities, compares each entry with another with a score
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
results = {}
for key in results:
    print(results[key])

# Sort by similarity
for idx, row in ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], ds['id'][i], ds['title'][i]) for i in similar_indices]
    results[row['id']] = similar_items[1:]

# Return item name
def item(id):
    row = ds.loc[id]
    return row['title']
    # return 
    # ds.loc[ds['id'] == id]['description'].tolist()[0].split(' - ')[0]

# Recommend items based on similarity
def recommend(item_id, num):
    print("Recommending " + str(num) + " products similar to " + item(item_id) + "...")
    print("-------")
    recs = results[item_id][:num]
    for rec in recs:
        print("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
    return recs


class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    rating = db.Column(db.String())
    link = db.Column(db.String())
    source = db.Column(db.String())

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String())

class Ratings(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    user_id = db.Column(db.BigInteger)
    course_id = db.Column(db.BigInteger)
    rating = db.Column(db.Float)

class CoursesInProgress(db.Model):
    __tablename__ = 'courses_in_progress'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    user_id = db.Column(db.BigInteger)
    course_id = db.Column(db.BigInteger)


@app.route("/")
def home():
    print(Courses.query.filter_by(source='Udacity').all()[1])
    recs = Courses.query.filter_by(source='Udacity').all()
    return render_template("index.html", recs=recs)


@app.route("/about")
def about():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login/index.html")


@app.route("/register")
def register():
    return render_template("register/index.html")
