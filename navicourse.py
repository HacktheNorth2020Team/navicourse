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
import json
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

# Sort by similarity
for idx, row in ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], ds['id'][i], ds['title'][i]) for i in similar_indices]
    results[row['id']] = similar_items[1:]

# Return item name
def item(id):
    row = ds.loc[id]
    return row['title']

# Recommend items based on similarity
def recommend(item_id, num):
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

def AddUser(session, u_id, nm):
    new_user = Users(user_id=u_id,
                     name=nm)
    session.add(new_user)

def GetUser(session, u_id):
    users = session.query.filter_by(user_id=u_id).first()
    return list(map(lambda user: {'user_id': user.user_id,
                                  'name': user.name},
                    users))

def AddRating(session, u_id, c_id, rt):
    new_rating = Ratings(user_id=u_id,
                         course_id=c_id,
                         rating=rt)
    session.add(new_rating)

def GetRating(session, u_id, c_id):
    ratings = session.query.filter_by(user_id=u_id) \
                           .filter_by(course_id=c_id).first()
    return list(map(lambda rating: {'user_id': rating.user_id,
                                    'course_id': rating.course_id,
                                    'rating': rating.rating},
                    ratings))

def AddCourseInProgress(session, u_id, c_id):
    newCIP = CoursesInProgress(user_id=u_id,
                               course_id=c_id)
    session.add(newCIP)

def GetCourseInProgress(session, u_id):
    CIPs = session.query.filter_by(user_id=u_id).all()
    return list(map(lambda CIP: {'user_id': CIP.user_id,
                                 'course_id': CIP.course_id},
                    CIPS))

@app.route("/")
def home():
    print(Courses.query.filter_by(source='Udacity').all()[1])	    values = query(-1, '')
    recs = recommend(2,5)	    return render_template("index.html", recs=values['recs'], user_id=values['user_id'])
    return render_template("index.html", recs=recs)	


@app.route("/about")	
def about():	
    return render_template("index.html")	



@app.route("/login")	@app.route("/", methods=['POST'])
def login():	def login():
    return render_template("login/index.html")	    data = json.loads(request.form['data'])

    user_id = data['id']

    name = data['name']
@app.route("/register")	    values = query(user_id, name)
def register():	    if values == None:
    return render_template("register/index.html")	        #AddUser(session, user_id, name)
        #return render_template("initialize/index.html", user_id=user_id, name=name)
        return render_template("index.html", recs=values['recs'], user_id=values['user_id'])
    return render_template("index.html", recs=values['recs'], user_id=values['user_id'])

@app.route("/initialize")
def initialize():
    return render_template("initialize/index.html")

def query(user_id, name):
    user = Users.query.get(user_id)
    if user == None:
        return None
    print(Courses.query.filter_by(source='Udacity').all()[1])
    recs = recommend(2,5)
    values = {
        'recs': recs,
        'user': user,
        'user_id': user_id
    }
    return values