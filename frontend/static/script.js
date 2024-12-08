document.getElementById('send-button').addEventListener('click', function() {
    var userQuery = document.getElementById('user-query').value;

    if (userQuery) {
        document.getElementById('response-container').innerHTML += `<p><strong>You:</strong> ${userQuery}</p>`;

        fetch('http://127.0.0.1:5000/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                query: userQuery,
                token: 'user-token-placeholder',
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response-container').innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;

            var container = document.getElementById('response-container');
            container.scrollTop = container.scrollHeight;
        })
        .catch(error => {
            document.getElementById('response-container').innerHTML += `<p><strong>Error:</strong> ${error}</p>`;
        });

        document.getElementById('user-query').value = '';
    }
});
