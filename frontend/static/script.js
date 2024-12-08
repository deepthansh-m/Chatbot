document.getElementById('send-button').addEventListener('click', function() {
    var userQuery = document.getElementById('user-query').value;

    if (userQuery) {
        // Display the user's query in the conversation history
        document.getElementById('response-container').innerHTML += `<p><strong>You:</strong> ${userQuery}</p>`;

        // Send POST request to the Flask API
        fetch('http://127.0.0.1:5000/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                query: userQuery,
                token: 'user-token-placeholder',  // Token as you set in the request
            })
        })
        .then(response => response.json())
        .then(data => {
            // Display the bot's response in the conversation history
            document.getElementById('response-container').innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;

            // Scroll to the bottom to show the latest messages
            var container = document.getElementById('response-container');
            container.scrollTop = container.scrollHeight;
        })
        .catch(error => {
            document.getElementById('response-container').innerHTML += `<p><strong>Error:</strong> ${error}</p>`;
        });

        // Clear the input field after sending the query
        document.getElementById('user-query').value = '';
    }
});
