from flask import Flask, render_template

from controllers.transaction_controller import transactions_blueprint
# change from tasks to spend        
app = Flask(__name__)

app.register_blueprint(transactions_blueprint)
# Again change from tasks

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)