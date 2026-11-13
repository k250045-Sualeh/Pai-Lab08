import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"data.csv", keep_default_na=False)

d3 = df[df['scenario'] == '03_SalaryDiff']

sns.boxplot(data=d3, x='prep_course', y='exam_score',
            order=['Entry', 'Mid', 'Senior'], palette='Set2')
plt.title('Salary Spread Across Experience Levels')
plt.xlabel('Experience Level')
plt.ylabel('Salary ($)')
plt.show()