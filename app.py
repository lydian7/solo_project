from flask import Flask, render_template
from controllers.branch_controller import branches_blueprint

app = Flask(__name__)

app.register_blueprint(branches_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
