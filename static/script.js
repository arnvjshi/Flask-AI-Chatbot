document.getElementById('generateButton').addEventListener('click', () => {
    const promptInput = document.getElementById('promptInput').value;
    const responseDiv = document.getElementById('response');
    responseDiv.textContent = "Generating response...";

    fetch('/api/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: promptInput }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            responseDiv.textContent = `Error: ${data.error}`;
        } else {
            responseDiv.textContent = `ChatBot: ${data.response}`;
        }
    })
    .catch(error => {
        responseDiv.textContent = `Error: ${error}`;
    });
});
