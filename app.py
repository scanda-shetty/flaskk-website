import io
import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  data = get_static_json("static/files/marvel.json")['projects']
  return render_template('home.html', projects=data)

@app.route('/', methods=['POST'])
def search():
    query = request.form.get('search')
    data = get_static_json("static/files/marvel.json")['projects']
    results = []
    for project in data:
        if query.lower() in project['name'].lower():
            results.append(project)
    return render_template('home.html', results=results, query=query)

@app.route('/<string:name>')
def project(name):
  data = get_static_json("static/files/marvel.json")['projects']
  for project in data:
        if project['name'] == name:
            return render_template('project.html', project=project)
  return 'Entry not found'

@app.route('/movies')
def timeline():
  data = get_static_json("static/files/marvel.json")['projects']
  return render_template('movie.html', projects=data)

@app.route('/characters')
def character():
  data = get_static_json("static/files/char.json")['characters']
  return render_template('character.html', characters=data)

@app.route('/reading')
def projects():
  data = get_static_json("static/files/marvel.json")['projects']
  return render_template('reading.html', projects=data)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

def get_static_file(path):
  site_root = os.path.realpath(os.path.dirname(__file__))
  return os.path.join(site_root, path)

def get_static_json(path):
  return json.load(open(get_static_file(path)))


if __name__ == "__main__":
  print("running py app")
  app.run(host="0.0.0.0", debug=True)
