from flask import render_template, url_for, flash, redirect, session
from vibing import app
from recommendation.popular_recommendation import PopularRecommendation
from vibing.forms import GenreForm


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/started")
def started():
    return render_template('started.html')


@app.route("/popular_recommendation", methods=['GET', 'POST'])
def popular_recommendation():
    form = GenreForm()
    if form.validate_on_submit():
        data = './data/dataset/popular.csv'
        genre = form.genre.data
        tags = []
        tags.append(genre)
        popular = PopularRecommendation()
        session["recommendations"] = popular.popular_recommend(
            data=data, tags=tags)
        return redirect(url_for('results'))
    return render_template('popular_recommendation.html', form=form)


@app.route("/results", methods=['GET', 'POST'])
def results():
    recommendations = session.get("recommendations")
    return render_template('results.html', recommendations=recommendations)
