from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    email = "ychen@nmhschool.org"
    phone = "857-654-8955"
    github = "https://github.com/Kimberlychne/my_work"
    return render_template("contact.html", email=email, phone=phone, github=github)

@app.route("/about")
def about():
    author = "Kimberly"
    favorite_language = "Python"
    interests = "Web Development", "Game Development"
    is_student = True
    return render_template("about.html", 
                           author=author,
                           favorite_language=favorite_language,
                           interests=interests,
                           is_student=is_student
                            )
if __name__ =="__main__":
    app.run(debug=True)
