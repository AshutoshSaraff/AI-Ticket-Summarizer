# AI Ticket Intelligence System

## Overview

AI-powered support ticket analysis system that automatically extracts key insights from customer support requests using Google's Gemini API.

## Features

- Ticket Summarization
- Priority Classification
- Category Detection
- Platform Identification
- AI-Powered Investigation Recommendations
- Structured JSON Processing

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Object-Oriented Programming (OOP)
- JSON

## Architecture

User
↓
Streamlit UI
↓
Ticket Processor
↓
Gemini API
↓
Structured Analysis
↓
Result Dashboard

## Sample Workflow

1. User submits support ticket.
2. AI analyzes issue.
3. System extracts:
   - Summary
   - Priority
   - Category
   - Platform
   - Investigation Steps
4. Results displayed in dashboard.

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Analysis Result

![Analysis Result](screenshots/analysis-result.png)

## Installation

pip install -r requirements.txt

streamlit run frontend.py