from flask import Flask, request, jsonify
from ldap3 import Server, Connection, ALL

app = Flask(__name__)

@app.route("/")
def index():
    return "Serveur Flask opérationnel!"

@app.route("/auth_ldap", methods=["POST"])
def auth_ldap():
   # 1. Récupérer les données envoyées par le client

   data = request.get_json()

   username = data.get("username")
   password = data.get("password")

   # 2. Vérifier que les champs existent

   if not username or not password :
      return jsonify({"error":"username et password requis"}), 400

   # 3. Configuration bonne route LDAP

   LDAP_SERVER = "ldap://localhost:389"
   BASE_DN = "dc=giga-factory,dc=local"
   USER_DN = f"uid={username},ou=People,{BASE_DN}"

   try:
       server = Server(LDAP_SERVER, get_info=ALL)
       conn = Connection(server, user=USER_DN, password=password, auto_bind=True)

       return jsonify({"status":"success", "message":"Authentification LDAP reussie"}), 200

   except Exception:
       return jsonify({"status":"fail", "message":"Echec authentification LDAP"}), 401

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)
