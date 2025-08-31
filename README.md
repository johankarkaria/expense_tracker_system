# Expense Tracker System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/johankarkaria/expense_tracker_system.git
   cd expense_tracker_system
   ```
2.**Install dependencies:**:   
   ```commandline
    pip install -r requirement.txt
   ```
3.**Run the FastAPI server:**:   
   ```commandline
    uvicorn server:app --reload
   ```
4.**Run the Streamlit app:**:   
   ```commandline
    streamlit run app.py
   ```
