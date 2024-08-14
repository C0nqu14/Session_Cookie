from flask import Flask, redirect, request, url_for, session, make_response, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "keysecret"

@app.route("/")
def home():
    user = session.get('username')
    return render_template("index.html", user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        session['username'] = username
        response = make_response(redirect(url_for('home')))
        response.set_cookie(
            "cookieset",
            username,
            secure=True,
            httponly=True,
            samesite='Lax',
            max_age=3600
        )
        return response
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    response = make_response(redirect(url_for('home')))
    response.set_cookie(
        "cookieset",
        "",
        expires=0,
        secure=True,
        httponly=True,
        samesite='Lax'
    )
    return response

@app.route("/setcookie")
def setcookie():
    cookie_value = request.cookies.get("cookieset")
    if cookie_value:
        return "cookie setado!"
    else:
        return "Cookie vázio"

@app.route("/getcookie")
def getcookie():
    cookie_value = request.cookies.get("cookieset")
    if cookie_value:
        return f"Valor do cookie: {cookie_value}"
    else:
        return "Cookie não encontrado"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4444)
