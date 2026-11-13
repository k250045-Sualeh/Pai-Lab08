import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"data.csv", keep_default_na=False)

d4 = df[df['scenario'] == '04_CustAgeDist'].copy()

d4['age'] = pd.to_numeric(d4['prep_course'])

sns.histplot(data=d4, x='age', hue='study_hours', bins=5, kde=True)
plt.title('Customer Age Distribution by Gender')
plt.xlabel('Age')
plt.ylabel('Customer Count')
plt.show()