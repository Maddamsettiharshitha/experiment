document.getElementById('registerForm').addEventListener('submit', function(event) {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    if (!name || !email) {
        alert('Please fill out all fields');
        event.preventDefault(); // Prevent form submission if fields are empty
    } else {
        alert('Registration successful!');
    }
});
