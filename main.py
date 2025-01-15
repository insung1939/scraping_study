from flask import Flask, render_template
app = Flask("JObScrapper")

@app.route("/") # decorator
def home():
    return render_template("home.html")

@app.route('/search')
def hello():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(port=5001)  # 5001 또는 다른 사용 가능한 포트를 지정