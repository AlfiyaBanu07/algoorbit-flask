from flask import Flask, render_template, abort, redirect, request, jsonify

app = Flask(__name__)

# Fix Jinja2 conflicts with CSS selectors such as {#navWrap}
app.jinja_env.comment_start_string = '{!--'
app.jinja_env.comment_end_string = '--}'


# "/" now redirects to "/home" so the address bar shows /home
@app.route('/')
def root():
    return redirect('/home', code=301)


@app.route('/home')
def home():
    return render_template('index.html')


# ---------------------------------------------------------------
# Form handlers (the pages post to these with fetch)
# ---------------------------------------------------------------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form.to_dict()
        # TODO: send email / save to database using `data`
        return jsonify(success=True)          # contact.html expects JSON
    return render_template('contact.html')


@app.route('/apply', methods=['POST'])
def apply():
    data = request.form.to_dict()
    resume = request.files.get('resume')      # check the input's name in careers.html
    # TODO: send email / save to database using `data` and `resume`
    return jsonify(success=True)              # careers.html only checks res.ok


@app.route('/schedule', methods=['POST'])
def schedule():
    data = request.form.to_dict()
    # TODO: send email / save to database using `data`
    return jsonify(success=True)              # consultancy.html only checks res.ok


# ---------------------------------------------------------------
# Main website pages
# ---------------------------------------------------------------
ALLOWED_PAGES = [
    'about',
    'careers',
    'consultancy',
     'our-work',
    'products',
    'training',
    'training-corporate',
    'training-institution',
    'training-learner',
    'privacy',
    'terms',
]


@app.route('/<page>')
def pages(page):

    if page in ALLOWED_PAGES:
        return render_template(f'{page}.html')

    # Redirect old .html URLs to clean URLs
    if page.endswith('.html'):
        clean_page = page[:-5]
        if clean_page in ALLOWED_PAGES or clean_page == 'contact':
            return redirect(f'/{clean_page}', code=301)
        if clean_page == 'index':
            return redirect('/home', code=301)
        if clean_page == 'privacy-policy':
            return redirect('/privacy', code=301)

    abort(404)


# ---------------------------------------------------------------
# Works pages
# ---------------------------------------------------------------
ALLOWED_WORKS = [
    'vrtx',
    'luminae',
    'bramhari',
    'hopeforward',
    'swiftcart',
    'gym',
    'novabuild',
    'voyex',
    'hospital',
    'annapoorna',
]


@app.route('/works/<page>')
def works(page):

    if page in ALLOWED_WORKS:
        return render_template(f'works/{page}.html')

    if page.endswith('.html'):
        clean_page = page[:-5]
        if clean_page in ALLOWED_WORKS:
            return redirect(f'/works/{clean_page}', code=301)

    abort(404)


if __name__ == '__main__':
    app.run(debug=True, port=5001)