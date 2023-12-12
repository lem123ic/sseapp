document.addEventListener("DOMContentLoaded", function () {
    // Check if the user's name is stored in localStorage
    var storedName = localStorage.getItem("userName");

    // Get the form and welcome message elements
    var form = document.getElementById("travelCardForm");
    var welcomeMessage = document.getElementById("welcomeMessage");
    var userNameSpan = document.getElementById("userName");

    // If the user's name is stored, display the welcome message
    if (storedName) {
        form.style.display = "none"; // Hide the form
        welcomeMessage.style.display = "block"; // Show the welcome message
        userNameSpan.textContent = storedName; // Display the user's name in the welcome message
    } else {
        form.style.display = "block"; // Show the form
        welcomeMessage.style.display = "none"; // Hide the welcome message
    }

    // Add a submit event listener to the form
    form.addEventListener("submit", function (event) {
        // Get the entered name from the form
        var enteredName = document.getElementById("name").value;

        // Store the name in localStorage
        localStorage.setItem("userName", enteredName);
    });
});

