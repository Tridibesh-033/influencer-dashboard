import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def calculate_roas(revenue, cost):
    if cost == 0:
        return np.nan
    return revenue / cost

def calculate_incremental_roas(campaign_revenue, baseline_revenue, cost):
    incremental_revenue = campaign_revenue - baseline_revenue
    if cost == 0:
        return np.nan
    return incremental_revenue / cost


# Load data
df_influencers = pd.read_csv('influencers.csv')
df_posts = pd.read_csv('posts.csv')
df_tracking = pd.read_csv('tracking_data.csv')
df_payouts = pd.read_csv('payouts.csv')

st.title("Influencer Campaign Performance Dashboard")

# Sidebar filters
platform = st.sidebar.selectbox("Select Platform", ['All'] + df_influencers['platform'].unique().tolist())
category = st.sidebar.selectbox("Select Category", ['All'] + df_influencers['category'].unique().tolist())

# Filter data
if platform != 'All':
    df_influencers = df_influencers[df_influencers['platform'] == platform]
if category != 'All':
    df_influencers = df_influencers[df_influencers['category'] == category]

# Campaign Performance
st.header("Campaign Performance")
campaign_perf = df_tracking.groupby('influencer_id')[['orders', 'revenue']].sum().reset_index()
st.dataframe(campaign_perf.merge(df_influencers, left_on='influencer_id', right_on='ID')[['name', 'orders', 'revenue']])

# ROAS Calculation
st.header("ROAS & Incremental ROAS")
payouts = df_payouts[['influencer_id', 'total_payout']]
roi_df = campaign_perf.merge(payouts, on='influencer_id')
roi_df['ROAS'] = roi_df.apply(lambda x: calculate_roas(x['revenue'], x['total_payout']), axis=1)
roi_df['Incremental_ROAS'] = roi_df.apply(lambda x: calculate_incremental_roas(x['revenue'], x['revenue']*0.8, x['total_payout']), axis=1)

st.dataframe(roi_df[['influencer_id', 'ROAS', 'Incremental_ROAS']])

# Top Influencers
st.header("Top Influencers by ROAS")
top_influencers = roi_df.sort_values(by='ROAS', ascending=False).head(5)
st.table(top_influencers.merge(df_influencers, left_on='influencer_id', right_on='ID')[['name', 'ROAS']])

# Payout Tracking
st.header("Payout Tracking")
st.dataframe(df_payouts)

# Visualizations
st.header("Revenue vs Payouts")
fig = px.bar(roi_df, x='influencer_id', y=['revenue', 'total_payout'], barmode='group')
st.plotly_chart(fig)

# Export option
st.download_button("Download ROI Data", roi_df.to_csv(index=False), file_name="roi_data.csv", mime="text/csv")

#------------------------------------------------

print("Top 3 influencers by ROAS")
print()
top_3_influencers = roi_df.sort_values(by='ROAS', ascending=False).head(3)
top_3_influencers = top_3_influencers.merge(df_influencers, left_on='influencer_id', right_on='ID')[['name', 'category', 'platform', 'ROAS']]
print(top_3_influencers)
print()

print("Influencers with lowest ROI")
print()
bottom_3_influencers = roi_df.sort_values(by='ROAS', ascending=True).head(3)
bottom_3_influencers = bottom_3_influencers.merge(df_influencers, left_on='influencer_id', right_on='ID')[['name', 'category', 'platform', 'ROAS']]
print(bottom_3_influencers)
print()

print("Group by gender and category to find average ROAS")
print()
persona_roas = roi_df.merge(df_influencers, left_on='influencer_id', right_on='ID')
best_persona = persona_roas.groupby(['gender', 'category'])['ROAS'].mean().reset_index().sort_values(by='ROAS', ascending=False).head(1)
print(best_persona)
