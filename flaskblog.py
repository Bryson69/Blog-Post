from flask import Flask , render_template, url_for
# "Import flask and render template ,
app = Flask(__name__)# app is a flask variable whihc is set to an instance ,Add flask variable,



# 
#  Add dictionary which represents a single blog post"
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'Forst Post Content',
        'date_posted': 'June 16 , 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'June 1 , 2020'
    }
]

#  Add an app route for the home and about page ,
@app.route("/")
@app.route("/home")
def home():
    return render_template ('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template ('about.html', title = 'About')

@app.route("/game")
def game():
    return render_template ('game.html')





if __name__ == '__main__':
    app.run(debug = True)