const typingText = document.getElementById('typing-text');
const text = 'feel connected';
let index = 0;
let isTyping = true;

function type() {
    if (index < text.length) {
        typingText.textContent += text[index];
        index++;
        setTimeout(type, 50); // Adjust typing speed as needed
    } else {
        isTyping = false;
        setTimeout(deleteText, 1000); // Add a short pause before deleting
    }
}

function deleteText() {
    if (index > 0) {
        typingText.textContent = text.substring(0, index - 1);
        index--;
        setTimeout(deleteText, 50);
    } else {
        isTyping = true;
        setTimeout(type, 1000); // Add a short pause before typing again
    }
}

type();