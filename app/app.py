from flask import Flask, render_template
import forms

app = Flask(__name__)

@app.route('/')
def index():
    commment_form = forms.CommentForm
    return render_template('index.html', form = commment_form)


if __name__ == '__main__':
    app.run(debug=True)
