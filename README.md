# MindFlow AI — Smart Study & Task Architect

An AI-powered full-stack productivity and workflow management application built with **FastAPI**, **SQLAlchemy**, **Streamlit**, and the **Google Gemini API**. MindFlow AI transforms unstructured study notes and technical task dumps into concise executive summaries and prioritized, time-boxed action plans.

## Key Features
* **Structured AI Extraction:** Uses Gemini Structured Outputs (`Pydantic` schemas) to convert raw notes into deterministic JSON containing executive summaries, task breakdowns, priority levels (`High`, `Medium`, `Low`), and time estimates.
* **Fault-Tolerant AI Service:** Implements dynamic model discovery and automatic fallback handling to maintain availability during API traffic spikes.
* **RESTful Backend Architecture:** Modular FastAPI backend with SQLAlchemy ORM persistence and automatic OpenAPI documentation (`/docs`).
* **Interactive Analytics Dashboard:** Modern dark-mode Streamlit frontend featuring real-time KPI metrics, completion progress bars, priority filtering, and task state toggles.

## Tech Stack
* **Backend:** Python, FastAPI, Uvicorn, SQLAlchemy, Pydantic
* **AI Integration:** Google GenAI SDK (`gemini-3.8-flash` with dynamic fallback)
* **Frontend:** Streamlit, Custom CSS, Google Material Symbols
* **Database:** SQLite

## Local Setup & Installation
1.Install dependencies:
pip install -r requirements.txt

2.Configure Environment Variables:
GEMINI_API_KEY=your_gemini_api_key_here

3.Start the FastAPI Backend:
cd backend
python -m uvicorn main:app --reload

4.Launch the Streamlit Frontend (in a new terminal):
cd frontend
python -m streamlit run app.py
