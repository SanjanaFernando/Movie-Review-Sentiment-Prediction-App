import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
import tensorflow as tf

# Example: Creating a tokenizer
tokenizer = Tokenizer(num_words=5000)
texts = ["This movie is amazing!", "Worst film ever."]
tokenizer.fit_on_texts(texts)

# Save tokenizer
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("✅ tokenizer.pkl has been created successfully!")

# Load trained model
model = tf.keras.models.load_model("sentiment_model.h5")
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Compile the model
