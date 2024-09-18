document.getElementById("complaint-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Get form data
    const formData = new FormData(this);

    // Send data to the server using AJAX
    fetch('/index.submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle response from the server (e.g., show a success message)
        console.log(data);
    })
    .catch(error => {
        // Handle errors
        console.error(error);
    });
});


const submitBugButton = document.getElementById('submit-bug');
const bugComment = document.getElementById('bug-comment');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');

submitBugButton.addEventListener('click', () => {
    const comment = bugComment.value;
    const name = nameInput.value;
    const email = emailInput.value;

    if (name.trim() === '' || email.trim() === '' || comment.trim() === '') {
        alert('Please fill in all required fields.');
        return;
    }

    // Submit the comment to your backend (e.g., using AJAX)
    console.log('Bug report submitted:', { name, email, comment });
});

const submitFraudButton = document.getElementById('submit-fraud');
const fraudComment = document.getElementById('fraud-comment');

submitFraudButton.addEventListener('click', () => {
    const comment = fraudComment.value;
    const name = nameInput.value;
    const email = emailInput.value;

    if (name.trim() === '' || email.trim() === '' || comment.trim() === '') {
        alert('Please fill in all required fields.');
        return;
    }

    // Submit the comment to your backend (e.g., using AJAX)
    console.log('Fraud report submitted:', { name, email, comment });
});

const submitTechnicalButton = document.getElementById('submit-technical');
const technicalComment = document.getElementById('technical-comment');

submitTechnicalButton.addEventListener('click', () => {
    const comment = technicalComment.value;
    const name = nameInput.value;
    const email = emailInput.value;

    if (name.trim() === '' || email.trim() === '' || comment.trim() === '') {
        alert('Please fill in all required fields.');
        return;
    }

    // Submit the comment to your backend (e.g., using AJAX)
    console.log('Technical problem report submitted:', { name, email, comment });
});

const accordionItems = document.querySelectorAll('.accordion > div');

accordionItems.forEach(item => {
    const header = item.querySelector('h2');
    const content = item.querySelector('.collapse');

    header.addEventListener('click', () => {
        content.classList.toggle('hidden');
    });
});

