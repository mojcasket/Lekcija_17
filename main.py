from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Index():
    name = "Mojca"
    current_year = "2020"

    cities = { "Vienna", "Maribor", "Ljubljana"}
    return render_template( "Index.html", name=name, current_year=current_year, cities=cities )

@app.route("/About")
def About():
    return render_template( "About.html" )

@app.route("/Portfolio")
def Portfolio():
    return render_template( "Portfolio.html" )

if __name__ == '__main__':
    app.run()

