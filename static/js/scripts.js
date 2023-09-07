// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    var checkoutButton = document.querySelector('input[type="submit"]');
    if (checkoutButton) {
        checkoutButton.addEventListener('click', function() {
            return confirm('Are you sure you want to proceed?');
        });
    }
});
