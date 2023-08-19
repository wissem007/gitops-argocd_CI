import socket
from uuid import getnode as get_mac
from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

# Get device details
def get_device_details():
    hostname = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    MAC_address = get_mac()
    MAC_address = (':'.join(("%012X" % MAC_address)[i:i+2] for i in range(0, 12, 2))).replace(":", "-")
    return hostname, ip, MAC_address

@app.route("/details")
def details():
    hostname, ip, mac = get_device_details()
    return render_template("details.html", hostname=hostname, ip=ip, mac=mac)

@app.route("/health")
def health():
    return jsonify(status="up")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Vérifiez les informations d'identification ici (par exemple, dans une base de données)
        if username == "votre_nom_utilisateur" and password == "votre_mot_de_passe":
            return "Connexion réussie!"
        else:
            return "Échec de la connexion. Veuillez vérifier vos informations d'identification."
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
