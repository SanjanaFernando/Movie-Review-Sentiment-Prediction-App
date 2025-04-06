from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from pydantic import BaseModel  # Import BaseModel from Pydantic
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load trained model
model = tf.keras.models.load_model("sentiment_model.h5")

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
    sequence = tokenizer.texts_to_sequences([request.review])
    padded = pad_sequences(sequence, maxlen=200)
    prediction = model.predict(padded)[0][0]

    # Convert prediction to a standard float
    prediction_score = float(prediction)  # Convert numpy.float32 to float

    # Determine sentiment and confidence level
    if prediction_score > 0.65:
        sentiment = "Good Movie"
        confidence = abs(prediction_score - 0.65)  # Confidence level for good movie
    else:
        sentiment = "Bad Movie"
        confidence = abs(prediction_score - 0.65)  # Confidence level for bad movie

    return {
        "review": request.review,
        "prediction": sentiment,
        "score": prediction_score,  # Use the converted float here
        "confidence": confidence
    }