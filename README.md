## 📊 Influencer Marketing Performance Dashboard
This project is a Streamlit dashboard to analyze influencer marketing campaign performance for HealthKart brands.
An interactive dashboard that simulates influencer marketing performance by generating synthetic data using Faker, and visualizes ROI/ROAS insights using Streamlit and Plotly.

##  Objective
To track campaign performance, calculate ROAS, and gain insights on top-performing influencers using simulated data.

## 🚀 Features
- Synthetic dataset generation for:
    - Influencers (with platform, category, followers)
    - Social media posts (likes, comments, reach)
    - Sales tracking (orders, revenue)
    - Payout calculations (post-based or order-based)

- ROAS (Return on Ad Spend) and Incremental ROAS calculations
- Interactive filtering by platform and category
- Visual comparisons: Revenue vs Payout
- Exportable ROI table (.csv)

- Highlights:
  - Top & bottom performers
  - Best-performing influencer persona by gender and category

<img width="955" height="502" alt="image" src="https://github.com/user-attachments/assets/f76e3d16-a8d5-4f21-a5c9-be88d4643c67" />

## 🛠️ Tech Stack
- Python
- Streamlit – UI & dashboard
- Pandas, NumPy – Data manipulation
- Faker – Fake data generation
- Plotly Express – Visualizations

## 📁 Dataset Files
- influencers.csv – Influencer details
- posts.csv – Social media post metrics
- tracking_data.csv – Sales & revenue from campaigns
- payouts.csv – Influencer compensation info

## 🧠 Core Logic
- ROAS = Revenue / Cost
- Incremental ROAS = (Campaign Revenue - Baseline Revenue) / Cost

The dashboard identifies high-performing influencers and helps track campaign profitability.

##  **How to Run**
1. Clone the repository:
   git clone https://github.com/Tridibesh-033/influencer-dashboard.git
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   streamlit run dashboard.py

## **Live Demo**
   https://influencer-dashboard-vwuktmypbancekbkfsfkqx.streamlit.app/

## 📌 Sample Insights
- Top 3 influencers by ROAS
- Influencers with lowest ROAS
- Best performer persona (e.g., Female - Nutrition)
   
###  **Conclusion**
This dashboard helps businesses make better marketing decisions by identifying effective influencers and optimizing payouts.

## 📬 Contact
- Tridibesh Debnath
- 📧 tridibeshdebnath@gmail.com
- 🌐 LinkedIn: https://www.linkedin.com/in/tridibesh-debnath-46b37924a/
