document.getElementById('sentimentForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const inputText = document.getElementById('text').value;
    const apiUrl = 'https://004bragwql.execute-api.us-east-1.amazonaws.com/prod';  // Your API Gateway URL

    if (!inputText.trim()) {
        document.getElementById('result').innerText = 'Please enter some text.';
        document.getElementById('result').classList.add('error');
        return;
    }

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': '/',  // Optional, matching Postman
                'X-Api-Key': 'QE4NLKQjnR5mU1pqzwYah7XoKE23XSG58sIB4MUw'
            },
            body: JSON.stringify({ text: inputText })  // Ensure the body is sent as JSON
        });

        if (!response.ok) {
            throw new Error(`Network response error: ${response.statusText} (status: ${response.status})`);
        }

        const result = await response.json();

        // Display the result (sentiment and confidence)
        document.getElementById('result').innerText = `Sentiment: ${result.Sentiment}, Confidence: ${result.Confidence}%`;
        document.getElementById('result').classList.add('success');
        document.getElementById('result').classList.remove('error');
    } catch (error) {
        // Handle any errors
        document.getElementById('result').innerText = 'Error processing your request.';
        document.getElementById('result').classList.add('error');
        document.getElementById('result').classList.remove('success');
        console.error('Error:', error);
    }
});
