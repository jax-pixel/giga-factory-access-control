from flask import Flask, request, jsonify
from ldap3 import Server, Connection, ALL

app = Flask(__name__)

LDAP_SERVER = "ldap://localhost"
BASE_DN = "dc=giga-factory,dc=local"

@app.route("/")
def index():
    return "Serveur Flask opérationnel!"

@app.route("/check_badge", methods=["POST"])
def check_badge():
   # 1. Récupérer les données envoyées par le client

   data = request.get_json()

   badge = data.get("badgenumber")

   # 2. Vérifier que les champs existent

   if not badge :
      return jsonify({"access":False, "message":"badge non lu"}), 400

   # 3. Configuration bonne route LDAP

   server = Server(LDAP_SERVER, get_info=ALL)
   conn = Connection(server, auto_bind=True)

   search_base = f"ou=People,{BASE_DN}"
   search_filter = f"(employeeNumber={badge})"

   conn.search(
       search_base=search_base,
       search_filter=search_filter,
       attributes=["uid"]
   )

   if conn.entries:
       return jsonify({"access":"True"})

   else:
       return jsonify({"access":"False"})

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
