# Russ Hendy - Personal Website

A simple, lightweight personal website powered by **Vue.js** (Frontend) and **FastAPI** (Backend).

## 📦 Stack

- **Frontend**: Vue 3 + Vite
- **Backend**: FastAPI (Python)
- **Deployment Strategy**: Ready for AWS Amplify (Frontend) / AWS Lambda or App Runner (Backend).

## 🚀 Running Locally

### 1. Backend (FastAPI)

Prerequisite: Python 3.9+ installed.

```bash
cd backend
# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

The backend runs on `http://127.0.0.1:8000`.

### 2. Frontend (Vue.js)

Prerequisite: Node.js and Yarn installed.

```bash
cd frontend

# Install dependencies
yarn install

# Run development server
yarn dev
```

The frontend runs on `http://localhost:5173`.

## 🛠 Project Structure

- `frontend/`: Vue application.
- `backend/`: Python FastAPI application.

Note: Docker has been removed to simplify the development and deployment workflow for this specific use case.
