from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)
app.secret_key = "devkey"  # temporary for prac


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"].strip()

        if not query:
            return render_template("search.html", error="Please enter a search term.")

        try:
            page = wikipedia.page(query, autosuggest=False)
            return render_template(
                "results.html",
                page_title=page.title,
                summary=page.summary,
                url=page.url
            )

        except wikipedia.exceptions.DisambiguationError as e:
            return render_template("search.html", options=e.options)

        except wikipedia.exceptions.PageError:
            return render_template("search.html", error="No page found.")

    return render_template("search.html")


if __name__ == "__main__":
    app.run()