document.querySelector('.registration-form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Thank you for registering! We will contact you soon.');
});

document.querySelector('.contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Your message has been sent! We will get back to you shortly.');
});

// Get elements
const chatbotButton = document.getElementById('chatbot-button');
const chatbotBox = document.getElementById('chatbot-box');
const chatbotClose = document.getElementById('chatbot-close');
const chatbotInput = document.getElementById('chatbot-input');
const chatbotSend = document.getElementById('chatbot-send');
const chatbotMessages = document.getElementById('chatbot-messages');

// Show/hide chatbot when button is clicked
chatbotButton.addEventListener('click', function() {
    // Toggle the chatbot visibility
    if (chatbotBox.classList.contains('hidden')) {
        chatbotBox.classList.remove('hidden');
        chatbotBox.classList.add('visible');
    } else {
        chatbotBox.classList.add('hidden');
        chatbotBox.classList.remove('visible');
    }
});

// Close chatbot when the close button is clicked
chatbotClose.addEventListener('click', function() {
    chatbotBox.classList.add('hidden');
    chatbotBox.classList.remove('visible');
});

// Handle sending messages
chatbotSend.addEventListener('click', function() {
    sendMessage();
});

// Also handle pressing 'Enter' to send a message
chatbotInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Function to send and display a message
function sendMessage() {
    const message = chatbotInput.value.trim();
    
    if (message !== "") {
        // Create a new message element
        const messageElement = document.createElement('p');
        messageElement.textContent = message;
        
        // Append the message to the chatbot messages area
        chatbotMessages.appendChild(messageElement);
        
        // Clear the input field
        chatbotInput.value = '';
        
        // Scroll to the bottom of the messages
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }
}

const words = ["VISUALIZE", "INNOVATE", "COLLABORATE", "CODE", "SHOWCASE"];
const element = document.getElementById('typewriter');
let wordIndex = 0;
let charIndex = 0;
let currentWord = '';
let isDeleting = false;

function type() {
    // If word is not yet fully typed out
    if (charIndex < words[wordIndex].length) {
        currentWord += words[wordIndex].charAt(charIndex);
        charIndex++;
        element.textContent = currentWord;
        setTimeout(type, 200); // Typing speed
    } else {
        // Move to next word after some delay
        setTimeout(() => {
            // Erase the current word before moving to the next
            erase();
        }, 1000);
    }
}

function erase() {
    if (charIndex > 0) {
        currentWord = currentWord.slice(0, -1); // Remove one character at a time
        charIndex--;
        element.textContent = currentWord;
        setTimeout(erase, 100); // Erasing speed
    } else {
        // Move to the next word
        wordIndex = (wordIndex + 1) % words.length; // Loop back to the start
        type();
    }
}

// Start typing on page load
document.addEventListener('DOMContentLoaded', function () {
    type();
});

const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

