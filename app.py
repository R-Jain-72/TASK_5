from flask import Flask, render_template, request

app = Flask(__name__)

# Create a dictionary of keywords and responses.
keyword_responses = {
    "Flask": "A micro web framework written in Python.",
    "Django": " Lil bit better than Flask b(assume b to be thumbs up)",
    "Backend": "Better than frontend :)",
    "Frontend": "insert rick roll",
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        keyword = request.form["keyword"]
        response = keyword_responses.get(keyword)

        if response is not None:
            return render_template("search_results.html", keyword=keyword, response=response)
        else:
            return render_template("search_results.html", keyword=keyword, response="No response found.")

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
