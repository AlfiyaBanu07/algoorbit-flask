
from flask import Flask, render_template, abort

app = Flask(__name__)

# Fix Jinja2 conflicts with CSS selectors such as {#navWrap}
app.jinja_env.comment_start_string = '{!--'
app.jinja_env.comment_end_string = '--}'


# Homepage
@app.route('/')
def home():
    return render_template('index.html')


# Main website pages
@app.route('/<page>')
def pages(page):

    allowed_pages = [
        'index.html',
        'about.html',
        'careers.html',
        'consultancy.html',
        'contact.html',
        'our-work.html',
        'products.html',
        'training.html',
        'training-corporate.html',
        'training-institution.html',
        'training-learner.html'
    ]

    if page in allowed_pages:
        return render_template(page)

    abort(404)


# Works pages
@app.route('/works/<page>')
def works(page):

    allowed_works = [
        'vrtx.html',
        'luminae.html',
        'bramhari.html',
        'hopeforward.html',
        'swiftcart.html',
        'gym.html',
        'novabuild.html',
        'voyex.html',
        'hospital.html',
        'annapoorna.html'
    ]

    if page in allowed_works:
        return render_template(f'works/{page}')

    abort(404)


# Run Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5001)
