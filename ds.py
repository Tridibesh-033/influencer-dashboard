import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# 1. Influencers data
influencers = []
platforms = ['Instagram', 'YouTube', 'Twitter']
categories = ['Fitness', 'Nutrition', 'Lifestyle']

for i in range(1, 21):
    influencers.append({
        'ID': i,
        'name': fake.name(),
        'category': random.choice(categories),
        'gender': random.choice(['Male', 'Female']),
        'follower_count': random.randint(5000, 100000),
        'platform': random.choice(platforms)
    })

df_influencers = pd.DataFrame(influencers)
df_influencers.to_csv('influencers.csv', index=False)

# 2. Posts data
posts = []
for i in range(1, 51):
    influencer_id = random.randint(1, 20)
    posts.append({
        'influencer_id': influencer_id,
        'platform': random.choice(platforms),
        'date': fake.date_between('-60d', 'today'),
        'URL': fake.url(),
        'caption': fake.sentence(),
        'reach': random.randint(1000, 50000),
        'likes': random.randint(100, 10000),
        'comments': random.randint(5, 500)
    })

df_posts = pd.DataFrame(posts)
df_posts.to_csv('posts.csv', index=False)

# 3. Tracking data
tracking = []
products = ['Protein Powder', 'Multivitamin', 'Gainer']

for i in range(1, 101):
    influencer_id = random.randint(1, 20)
    orders = random.randint(0, 30)
    revenue = orders * random.randint(500, 1500)
    tracking.append({
        'source': 'influencer_campaign',
        'campaign': 'July_Campaign',
        'influencer_id': influencer_id,
        'user_id': fake.uuid4(),
        'product': random.choice(products),
        'date': fake.date_between('-60d', 'today'),
        'orders': orders,
        'revenue': revenue
    })

df_tracking = pd.DataFrame(tracking)
df_tracking.to_csv('tracking_data.csv', index=False)

# 4. Payouts data
payouts = []
for influencer_id in df_influencers['ID']:
    basis = random.choice(['post', 'order'])
    rate = random.randint(1000, 5000) if basis == 'post' else random.randint(100, 500)
    orders = random.randint(0, 30) if basis == 'order' else None
    total_payout = rate * orders if basis == 'order' else rate
    payouts.append({
        'influencer_id': influencer_id,
        'basis': basis,
        'rate': rate,
        'orders': orders,
        'total_payout': total_payout
    })

df_payouts = pd.DataFrame(payouts)
df_payouts.to_csv('payouts.csv', index=False)



