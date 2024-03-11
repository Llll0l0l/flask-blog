from flask import Flask, render_template
import requests

app = Flask(__name__)

r = requests.get('https://api.npoint.io/674f5423f73deab1e9a7')
posts = r.json()


values = []
# make a list of the values in the list of dictionaries
for p in posts:
    values.append(tuple(p.values()))


values = tuple(values)

# route for the root directory
@app.route('/')
def home():
    return render_template('index.html', posts=values )


#route for the about directory
@app.route('/about')
def about():
    return render_template('about.html')


#route for the post directory
@app.route('/post')
def post():
    return render_template('post.html')


#route for the about directory
@app.route('/contact')
def contact():
    return render_template('contact.html')

# route for each individual post
@app.route('/post/<int:id>')
def show_post(id):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == id:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)