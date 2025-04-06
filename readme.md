# 🎬 Movie Review Sentiment Prediction App

This is a **web application** that predicts the sentiment of movie reviews using a **FastAPI** backend and a **Vite** frontend.

---

## 🚀 Prerequisites

Before getting started, make sure you have the following installed:

✅ Python **3.7 or higher**  
✅ Node.js **14 or higher**  
✅ pip (Python package installer)

---

## 🛠️ Setup Instructions

Follow these steps to set up the application on your local machine:

### 1️⃣ Clone the Repository

Clone the repository and navigate into the project directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

### 2️⃣ Set Up the Backend (FastAPI)

#### 📌 Step 1: Create a Virtual Environment

Create a virtual environment for the backend:

```bash
python -m venv .venv
```

#### 📌 Step 2: Activate the Virtual Environment

- **On Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 📌 Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install fastapi uvicorn pydantic
```

#### 📌 Step 4: Install TensorFlow

To install TensorFlow in the virtual environment:

```bash
pip install tensorflow
```

#### 📌 Step 5: Run the FastAPI Server

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

✅ The backend server will be running at **`http://127.0.0.1:8000`**.

---

### 3️⃣ Set Up the Frontend (Vite)

#### 📌 Step 1: Navigate to the Frontend Directory

If your frontend is in a separate directory (e.g., `my-vite-app`), navigate to that directory:

```bash
cd my-vite-app
```

#### 📌 Step 2: Install Frontend Dependencies

Install the required Node.js packages:

```bash
npm install
```

#### 📌 Step 3: Run the Vite Development Server

Start the Vite development server:

```bash
npm run dev
```

✅ The frontend will be running at **`http://localhost:5173`**.

---

## 🎥 Usage

1️⃣ Open your browser and go to **`http://localhost:5173`**.  
2️⃣ Enter a **movie review** in the text area.  
3️⃣ Click **"Predict Sentiment"** to see the prediction and confidence level.  

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🎖️ Acknowledgments

- 🚀 **FastAPI** for the backend framework.
- ⚡ **Vite** for the frontend development.
- 🧠 **TensorFlow** for the machine learning model.

---

💡 Happy Coding! 🎬✨

