
# A very simple Flask Hello World app for you to get started with...
from functools import cache
from flask import Flask, render_template

app = Flask(__name__, template_folder=".")

grid = [
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/818410514_480x360.png", "label": "Jump Up MMO", "link": "818410514", "description": "Nutze die Maus um dich zu bewegen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/755207880_480x360.png", "label": "Isometri Micro", "link": "755207880", "description": "WASD zum Bewegen und Leertaste zum Springen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/888326329_480x360.png", "label": "The Age of Ruin", "link": "888326329", "description": "Intruktionen im Spiel."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/881913043_480x360.png", "label": "Minecraft Klon (Nicht fertig)", "link": "881913043", "description": "WASDQE zum bewegen und Maus zum umschauen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/798423836_480x360.png", "label": "Dungeon Exploration", "link": "798423836", "description": "WASD zum Bewegen, Linksklick zum angreifen und E zum Öffnen von Türen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/713980536_480x360.png", "label": "Raycaster Maze++", "link": "713980536", "description": "Pfeiltasten zum Umschauen und WASD zum Bewegen. Suche das Ende des Labyrinths!"},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/810073635_480x360.png", "label": "Simple Towerdefense", "link": "810073635", "description": "Plaziere Türme um die Wellen von Gegnern zu überleben."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/588678779_480x360.png", "label": "Simple Towerdefense HACK", "link": "588678779", "description": "Plaziere Türme, um die Wellen von Gegnern zu überleben."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/630735602_480x360.png", "label": "Dungeon Run", "link": "630735602", "description": "WASD zum Bewegen und Leertaste zum Angreifen. Besiege Gegner für bessere Waffen und Geld!"},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/546460593_480x360.png", "label": "Move it!", "link": "546460593", "description": "Bewege deine Maus um nicht zu fallen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/533914574_480x360.png", "label": "Rock The Universe", "link": "533914574", "description": "Pfeiltasten zum Bewegen und angreifen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/507035127_480x360.png", "label": "Rock The Galaxy reloaded", "link": "507035127", "description": "Bewege deine Maus zum Bewegen, Maustaste zum Angreifen und X zum Öffnen des Shops."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/610729525_480x360.png", "label": "Adventure FORTRESS", "link": "610729525", "description": "WASD zum Bewegen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/531453398_480x360.png", "label": "Flag Hunt", "link": "531453398", "description": "WASD zum Bewegen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/396478607_480x360.png", "label": "Ball 3D", "link": "396478607", "description": "Pfeiltasten und Leertaste zum Bewegen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/403682025_480x360.png", "label": "Ball 3D 2", "link": "403682025", "description": "Pfeiltasten und Leertaste zum Bewegen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/405298192_480x360.png", "label": "Ball 3D 3", "link": "405298192", "description": "Pfeiltasten und Leertaste zum Bewegen."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/1017717920_480x360.png", "label": "Improved Simple Towerdefense", "link": "1017717920", "description": "Plaziere Türme um die Wellen von Gegnern zu überleben."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/1047118561_480x360.png", "label": "Imitators Online", "link": "1047118561", "description": "You need to imitate the drawing you are shown by retracing it with your mouse cursor or finger. You will get a score based on accuracy and if you want, you can send your try to the server as a possible highscore which would be shown to everyone else who tries the drawing."]

@cache
def get_data(pid):
    return list(filter(lambda x: x["link"] == pid, grid))[0]

@app.route('/')
def home():
    return render_template("home.html", images_and_labels=grid)

@app.route('/<pid>/')
def project(pid):
    data = get_data(pid)
    return render_template("project.html", data=data)

