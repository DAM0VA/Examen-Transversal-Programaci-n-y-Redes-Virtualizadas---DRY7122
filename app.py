from flask import Flask, request, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
 
app = Flask(__name__)
DB = "usuarios.db"
 
USUARIOS = {
    "Damova": "hola1234",
}
 
 
def init_db():
    """Crea la tabla e inserta los usuarios con la contrasena hasheada."""
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     nombre TEXT UNIQUE,
                     password_hash TEXT)""")
    for nombre, clave in USUARIOS.items():
        cur.execute("SELECT 1 FROM usuarios WHERE nombre = ?", (nombre,))
        if not cur.fetchone():
            hash_clave = generate_password_hash(clave)
            cur.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)",
                        (nombre, hash_clave))
    con.commit()
    con.close()
 
 
FORM = """
<!doctype html>
<html><head><meta charset="utf-8"><title>Login DRY7122</title></head>
<body style="font-family:sans-serif;max-width:400px;margin:60px auto">
  <h2>Login - Examen Transversal DRY7122</h2>
  <form method="post" action="/login">
    <p>Usuario:<br><input name="usuario" style="width:100%"></p>
    <p>Contrasena:<br><input name="clave" type="password" style="width:100%"></p>
    <button type="submit">Ingresar</button>
  </form>
  {% if mensaje %}<p><b>{{ mensaje }}</b></p>{% endif %}
</body></html>
"""
 
 
@app.route("/")
def index():
    return render_template_string(FORM, mensaje=None)
 
 
@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario", "")
    clave = request.form.get("clave", "")
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT password_hash FROM usuarios WHERE nombre = ?", (usuario,))
    fila = cur.fetchone()
    con.close()
    if fila and check_password_hash(fila[0], clave):
        mensaje = f"Acceso concedido. Bienvenido, {usuario}!"
    else:
        mensaje = "Usuario o contrasena incorrectos."
    return render_template_string(FORM, mensaje=mensaje)
 
 
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=7500, debug=True)
