document.getElementById('send-button').onclick = function() {
    var userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== "") {
        addMessage(userInput, 'user-message');
        document.getElementById('user-input').value = '';
        setTimeout(() => {
            addMessage(getBotResponse(userInput), 'bot-message');
        }, 1000);
    }
};

function addMessage(message, className) {
    var chatBox = document.getElementById('chat-box');
    var messageDiv = document.createElement('div');
    messageDiv.className = 'chat-message ' + className;
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; 
}

function getBotResponse(userInput) {

    if (userInput.toLowerCase().includes("hello")) {
        return "Hi there! How can I assist you?";
    } else if (userInput.toLowerCase().includes("how are you")) {
        return "I'm just a bot, but thanks for asking!";
    } else {
        return "Sorry, I didn't understand that.";
    }
}



const stars = document.querySelectorAll('.star');
const feedbackMessage = document.getElementById('feedback-message');

stars.forEach(star => {
    star.addEventListener('click', () => {
        const ratingValue = star.getAttribute('data-value');
        
        stars.forEach(s => s.classList.remove('selected'));
        
        for (let i = 0; i < ratingValue; i++) {
            stars[i].classList.add('selected');
        }

        feedbackMessage.textContent = `Você avaliou com ${ratingValue} estrela(s)!`;
    });
});
