from flask import Flask, request, render_template_string

app = Flask(__name__)

comments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form['comment']
        comments.append(comment)
    
    return render_template_string('''
    <!doctype html>
    <html>
    <head>
        <title>Comment Box</title>
    </head>
    <body>
        <h1>Leave a Comment</h1>
        <form method="POST">
            <textarea name="comment"></textarea><br>
            <input type="submit" value="Submit">
        </form>
        <h2>Comments</h2>
        <ul>
            {% for comment in comments %}
                <li>{{ comment | safe }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    ''', comments=comments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
