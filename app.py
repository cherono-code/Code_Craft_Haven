from flask import Flask, render_template, request
from app.routes import main

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(main)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    # Save registration details or send an email
    return "Registration Successful!"

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process contact form submission
    return "Message Sent!"

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)


