from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)

@main.route('/community')
def community():
    return render_template('community.html')

@main.route('/hackathon')
def hackathon():
    return render_template('hackathon.html')

@main.route('/founder')
def founder():
    return render_template('founder.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')

    # Basic chatbot logic
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "what is code craft haven?": "Code Craft Haven is a community and platform for developers to learn, grow, and connect.",
        "tell me about the hackathon": "Our upcoming hackathon is a day event where developers can collaborate and build innovative projects.",
        # Add more responses as needed
    }

    response = responses.get(user_message.lower(), "I'm sorry, I don't understand that. Can you try asking something else?")
    return jsonify({"response": response})
