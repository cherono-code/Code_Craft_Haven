from flask import Blueprint, flash, render_template, request, jsonify, redirect, url_for, current_app
import requests
from .forms import ContactForm  # Import the ContactForm class from forms.py
from google.cloud import firestore

# Define the main blueprint
main = Blueprint('main', __name__)

# Helper function to verify reCAPTCHA
def verify_recaptcha(response_token):
    payload = {
        'secret': current_app.config['RECAPTCHA_PRIVATE_KEY'],  # private key
        'response': response_token
    }
    # Send request to Google reCAPTCHA API
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    result = response.json()
    return result.get('success', False)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/community')
def community():
    return render_template('community.html')

@main.route('/hackathon')
def hackathon():
    return render_template('hackathon.html')

@main.route('/mentor')
def mentor():
    return render_template('mentor.html')

@main.route('/founder')
def founder():
    return render_template('founder.html')

# Updated contact route using Flask-WTF form
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        recaptcha_response = form.recaptcha.data  # reCAPTCHA response

        # Verify reCAPTCHA
        if verify_recaptcha(recaptcha_response):
            # Process contact form submission (e.g., save to database or send email)
            return "Message Sent!"  # Or redirect to a success page
        else:
            flash("reCAPTCHA verification failed. Please try again.", "danger")
            return redirect(url_for('main.contact'))

    return render_template('contact.html', form=form)

@main.route('/signup')
def signup():
    return render_template('signup.html')

@main.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "what is code craft haven?": "Code Craft Haven is a community and platform for developers to learn, grow, and connect.",
        "tell me about the hackathon": "Our upcoming hackathon is a day event where developers can collaborate and build innovative projects.",
        "how can i join a group": "You can join a group by signing up on our platform and exploring community groups that match your interests."
    }
    response = responses.get(user_message.lower(), "I'm sorry, I don't understand that. Can you try asking something else?")
    return jsonify({"response": response})

# Simplified registration route
@main.route('/submit_registration', methods=['POST'])
def submit_registration():
    try:
        # Get the reCAPTCHA response token from the form
        recaptcha_response = request.form['g-recaptcha-response']

        # Verify reCAPTCHA
        if not verify_recaptcha(recaptcha_response):
            flash("reCAPTCHA verification failed. Please try again.", "danger")
            return redirect(url_for('main.signup'))

        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        location = request.form.get('location')
        organization = request.form.get('organization')
        role = request.form.get('Role')
        other_role = request.form.get('otherRole') if role == 'Other' else None
        proficiency = request.form.get('proficiency')

        # Get Firestore client
        db = current_app.config['db']  # Firebase Firestore client

        # Structure the registration data
        registration_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'location': location,
            'organization': organization,
            'role': role,
            'other_role': other_role,
            'proficiency': proficiency,
            'timestamp': firestore.SERVER_TIMESTAMP
        }

        # Store the registration data in Firestore
        db.collection('registrations').add(registration_data)
        flash("Registration successful! Thank you for signing up.", "success")

        # Redirect or show a success message
        return redirect(url_for('main.registration_success'))

    except Exception as e:
        current_app.logger.error(f"Error saving registration: {e}")
        flash("An error occurred. Please try again later.", "danger")
        return redirect(url_for('main.signup'))

@main.route('/registration_success')
def registration_success():
    return "Thank you for registering! We’ll be in touch soon."
