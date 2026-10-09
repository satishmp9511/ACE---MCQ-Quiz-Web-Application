# ACE - MCQ Quiz Web Application

A lightweight, error-proof MCQ Quiz application built using **FastAPI**, **Jinja2 Templates**, and **Custom Glassmorphism CSS**.

## Features

- **Dynamic Question Loading:** Reads questions directly from `QW.txt`.
- **Robust Navigation:** Navigate through questions with safe boundary checking (`w < 50`) to prevent app crashes.
- **Answer Validation:** Instant feedback on submitted answers.
- **Mobile-Responsive Design:** Glassmorphism Dark UI optimized for both Desktop and Mobile devices.

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** HTML5, CSS3 (Glassmorphism & Responsive Media Queries), Jinja2
- **Deployment:** Vercel

## Project Structure

```text
├── main.py              # FastAPI backend routes & file parsing logic
├── index.html           # Main UI Template
├── style.css            # Dark Glassmorphism & Responsive styling
├── QW.txt               # Question bank text file
├── vercel.json          # Vercel deployment configuration
├── requirements.txt     # Python project dependencies
└── README.md            # Project documentation

git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
pip install -r requirements.txt
uvicorn main:app --reload
