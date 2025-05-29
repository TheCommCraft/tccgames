
from functools import cache
from os import getenv
from hmac import compare_digest
from flask import Flask, render_template, request, jsonify
import requests

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
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/1047118561_480x360.png", "label": "Imitators Online", "link": "1047118561", "description": "Du musst die gezeigten Formen nachmalen. Du erhältst dafür eine Bewertung und kannst diese, wenn du willst, an den Server senden, damit er eventuell als Bestversuch aufgefasst wird."},
    {"url": "https://cdn2.scratch.mit.edu/get_image/project/824262326_480x360.png", "label": "Cubic Crossover", "link": "824262326", "description": "Male Levels, die man als Platformer spielen kann. Diese können auch hochgeladen werden (Kommentare befinden sich bei https://scratch.mit.edu/projects/824262326/ ) und du kannst auch fremde Level spielen. Die Steuerung erfolgt über WASD oder Pfeiltasten."}
]

alert_key = getenv("ALERT_KEY")
resend_key = getenv("RESEND_KEY")

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

@app.get("/alert/")
def alert_screen():
    return render_template("alert.html")

@app.post("/alert/")
def send_alert():
    if not compare_digest(request.form.get("key"), alert_key):
        return jsonify({"success": False})
    resp = requests.post("https://willroll.thecommcraft.de/send_email/", data={
        "subject": f"Alert: {request.form.get('alert_name', 'alert_name')}",
        "sender": "tccalert@rsnd.thecommcraft.de",
        "receiver": "tcc@thecommcraft.de",
        "htmlcontent": f"ALERT!!!\n{request.form.get('alert', 'alert')}",
        "apikey": resend_key
    }).text
    return jsonify({"success": True, "response": resp})
