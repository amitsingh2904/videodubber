 
 document.getElementById('dubbingForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Optional: Prevent default form submission

    let formData = new FormData(this);

    fetch('/process', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('progress').innerHTML = '';  // Clear progress
        document.getElementById('result').innerHTML = data;  // Show result
    })
    .catch(error => {
        document.getElementById('progress').innerHTML = '';  // Clear progress
        document.getElementById('result').innerHTML = "Error: " + error;
    });
});

