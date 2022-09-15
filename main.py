from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_session import Session
from moviedatabasemanager import MovieDatabaseManager
import os


app = Flask(__name__)

# WTforms configuration
app.config['SECRET_KEY'] = os.environ.get("secret_key")
# Boostrap configuration
Bootstrap(app)
# SQLalcheemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Session configuration
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    review = db.Column(db.String(80), unique=False, nullable=False)
    img_url = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<title %r>' % self.title


db.create_all()


class EditForm(FlaskForm):

    rating = StringField("Rating", validators=[DataRequired()], render_kw={"style": "width: 50ch"})
    review = StringField("Review", validators=[DataRequired()], render_kw={"style": "width: 50ch"})
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):

    movie_title = StringField("Movie Title", validators=[DataRequired()], render_kw={"style": "width: 50ch"})
    submit = SubmitField(label="Add Movie")


@app.route("/", methods=["GET"])
def home():

    all_movies = db.session.query(Movie).all()
    all_movies.sort(key=lambda movie_item: movie_item.rating, reverse=True)

    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():

    movie_title = request.args.get("movie_title")
    form = EditForm()

    if form.validate_on_submit():
        movie_update = Movie.query.filter_by(title=movie_title).first()
        movie_update.rating = form.rating.data
        movie_update.review = form.review.data
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():

    movie_title = request.args.get("movie_title")
    movie_to_delete = Movie.query.filter_by(title=movie_title).first()
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():

    form = AddForm()

    if form.validate_on_submit():
        session["movie_search_list"] = MovieDatabaseManager.getmovie(form.movie_title.data)

        return redirect(url_for("select"))

    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select():

    movie_search_list = session.get("movie_search_list", None)

    return render_template("select.html", movie_search_list=movie_search_list)


@app.route("/add-movie", methods=["GET", "POST"])
def add_movie():

    movie_search_list = session.get("movie_search_list", None)
    movie_selection_id = request.args.get("movie_id")

    for movie_item in movie_search_list:

        if int(movie_selection_id) == movie_item["id"]:

            new_movie = Movie(
                title=movie_item["title"],
                year=movie_item["release_date"][:4],
                description=movie_item["description"],
                rating=0,
                review=" ",
                img_url=movie_item["poster_path"]
            )

            db.session.add(new_movie)
            db.session.commit()

            return redirect(url_for('edit', movie_title=movie_item["title"]))


if __name__ == '__main__':
    app.run(debug=True)
