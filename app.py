from flask import Flask, render_template

# from controllers.spend_controller import tasks_blueprint      UNCOMMENT 
# change from tasks to spend        
app = Flask(__name__)

# app.register_blueprint(tasks_blueprint)   UNCOMMENT 
# Again change from tasks

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)