This project was developed for the IIT Kanpur Hackathon (CredTech).
It focuses on analyzing stock market data (Infosys, TCS) and financial news to:

Predict stock trading volume using machine learning

Perform financial sentiment analysis on news articles

Build a dashboard for interactive visualization

Project Structure
Hackathon.ipynb - Main notebook for data preprocessing and ML models
clean_stock_data.csv - Stock price dataset (Infosys and TCS)
dashboard.py - Streamlit dashboard for visualization
requirements.txt - Python dependencies
README.md - Project documentation

Features

Predicts stock trading volume using ML models

Sentiment analysis of financial news (positive, neutral, negative)

Interactive dashboard to visualize trends and predictions

Uses scikit-learn, Pandas, Streamlit, and NLP techniques

Installation
Clone the repository and install dependencies:
git clone <your-repo-link>
cd <repo-folder>
pip install -r requirements.txt

Usage

Run Jupyter Notebook (ML Training and Analysis)
jupyter notebook Hackathon.ipynb

Launch the Dashboard
streamlit run dashboard.py

This will start a local server, and you can open the interactive dashboard in your browser.

Example Workflows

ML Notebook (Hackathon.ipynb):
Load clean_stock_data.csv
Train models to predict Volume
Evaluate accuracy and visualize results

Dashboard (dashboard.py):
Explore stock trends
Compare Infosys vs TCS data
Display predictions and sentiment results

Requirements
All dependencies are listed in requirements.txt

Install them with:
pip install -r requirements.txt

Team and Acknowledgment
Built as part of IIT Kanpur CredTech Hackathon.
Special thanks to mentors and organizers.
