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

        // Display confidence level
        const confidenceElement = document.getElementById('confidence');
        confidenceElement.innerText = `Confidence Level: ${data.confidence}`; // Show confidence level
        
        // Apply color coding based on confidence level
        if (data.confidence === "High") {
            confidenceElement.className = "confidence high"; // Add high confidence class
        } else {
            confidenceElement.className = "confidence low"; // Add low confidence class
        }
    } else {
        document.getElementById('result').innerText = 'Error: Unable to get prediction.';
    }
});