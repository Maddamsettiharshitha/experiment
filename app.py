from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    # Redirect to /register if you want the user to see the form at the root URL
    return redirect(url_for("registration"))

@app.route("/register", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        # You can handle the form data here
        return redirect(url_for("success"))
    return render_template("register.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
