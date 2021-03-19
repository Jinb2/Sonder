from flask import render_template, url_for, flash, redirect, session
from vibing import app
from recommendation.popular_recommendation import PopularRecommendation
from data.spotify import spotify_scraper
from vibing.forms import GenreForm


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/started")
def started():
    return render_template('started.html')


@app.route("/about")
def about():
    return render_template('about.html')


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
    artist_tracks = []
    images = []
    for artist in recommendations:
        tracks, album_images = spotify_scraper.getTopTracks(artist)
        for i in range(len(tracks)):
            artist_tracks.append(tracks[i])
            images.append(album_images[i])
    length = len(artist_tracks)
    return render_template('results.html',  artist_tracks=artist_tracks, images=images, length=length, recommendations=recommendations)
