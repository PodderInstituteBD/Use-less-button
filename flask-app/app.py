from flask import Flask, render_template

# Flask অ্যাপ তৈরি
app = Flask(__name__)

# হোম রাউট
@app.route('/')
def home():
    return render_template("index.html")

# অ্যাপ রান করানো (local server)
if __name__ == '__main__':
    app.run(debug=True)
