document.getElementById('predict-button').addEventListener('click', async () => {
    const review = document.getElementById('review').value;
    const response = await fetch('http://127.0.0.1:8000/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ review }),
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('result').innerText = `Prediction: ${data.prediction}, Score: ${data.score}`;

        // Display confidence with color coding
        const confidenceElement = document.getElementById('confidence');
        confidenceElement.innerText = `Confidence: ${data.confidence.toFixed(2)}`; // Show confidence value
        if (data.confidence < 0.1) {
            confidenceElement.style.color = 'blue'; // High confidence
        } else {
            confidenceElement.style.color = 'red'; // Low confidence
        }
    } else {
        document.getElementById('result').innerText = 'Error: Unable to get prediction.';
    }
});