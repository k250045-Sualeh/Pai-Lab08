import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"data.csv", keep_default_na=False)

d5 = df[df['scenario'] == '05_AdVsRevenue'].copy()

d5['ad_spend'] = pd.to_numeric(d5['study_hours'])
d5['revenue'] = pd.to_numeric(d5['prep_course'])

sns.regplot(data=d5, x='ad_spend', y='revenue',
            marker='+', scatter_kws={'color': 'darkgreen'})
plt.title('Impact of Advertising Spend on Total Revenue')
plt.xlabel('Ad Spend ($)')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.show()