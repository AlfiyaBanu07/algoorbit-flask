
from flask import Flask, render_template, abort, redirect

app = Flask(__name__)

# Fix Jinja2 conflicts with CSS selectors such as {#navWrap}
app.jinja_env.comment_start_string = '{!--'
app.jinja_env.comment_end_string = '--}'


# Homepage
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


# Main website pages
@app.route('/<page>')
def pages(page):

    allowed_pages = [
        'about',
        'careers',
        'consultancy',
        'contact',
        'our-work',
        'products',
        'training',
        'training-corporate',
        'training-institution',
        'training-learner'
    ]

    if page in allowed_pages:
        return render_template(f'{page}.html')

    # Redirect old .html URLs to clean URLs
    if page.endswith('.html'):
        clean_page = page[:-5]
        if clean_page in allowed_pages:
            return redirect(f'/{clean_page}', code=301)
        if clean_page == 'index':
            return redirect('/home', code=301)

    abort(404)


# Works pages
@app.route('/works/<page>')
def works(page):

    allowed_works = [
        'vrtx',
        'luminae',
        'bramhari',
        'hopeforward',
        'swiftcart',
        'gym',
        'novabuild',
        'voyex',
        'hospital',
        'annapoorna'
    ]

    if page in allowed_works:
        return render_template(f'works/{page}.html')

    if page.endswith('.html'):
        clean_page = page[:-5]
        if clean_page in allowed_works:
            return redirect(f'/works/{clean_page}', code=301)

    abort(404)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
