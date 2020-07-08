from config import *
from modelo import Cachorro

@app.route("/")
def inicio():
    return redirect("/listar_cachorros")


@app.route("/listar_cachorros")
def listar_cachorros():
    cachorros = db.session.query(Cachorro).all()
    cachorros_em_json = [x.json() for x in cachorros]
    return jsonify(cachorros_em_json)

app.run(debug=True)