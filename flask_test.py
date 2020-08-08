from flask import Flask, render_template


app = Flask(__name__,
            static_url_path='',
            static_folder='app/static',
            template_folder='app/templates')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    # Debug = true will allow for updates to be pushed without restarting flask.
    app.run(debug=True)