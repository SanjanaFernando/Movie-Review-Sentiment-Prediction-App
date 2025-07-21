from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from pydantic import BaseModel  # Import BaseModel from Pydantic
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load trained model
model = tf.keras.models.load_model("sentiment_model (1).h5")

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can specify specific origins if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define the ReviewRequest model
class ReviewRequest(BaseModel):
    review: str  # Expecting a string field named 'review'

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/predict/")
async def predict_sentiment(request: ReviewRequest):
    # Tokenize and pad the review
    sequence = tokenizer.texts_to_sequences([request.review])
    padded_sequence = pad_sequences(sequence, maxlen=200)
    
    # Make prediction
    prediction = model.predict(padded_sequence)
    
    # Determine sentiment
    sentiment = "Good Movie" if prediction[0][0] > 0.5 else "Bad Movie"
    
    # Calculate confidence level
    confidence = abs(prediction[0][0] - 0.5)  # Confidence level based on distance from 0.5
    confidence_level = "High" if confidence > 0.05 else "Low"  # Confidence level threshold

    return {
        "review": request.review,
        "prediction": sentiment,
        "score": float(prediction[0][0]),  # Convert to standard float
        "confidence": confidence_level  # Return the confidence level as "High" or "Low"
    }