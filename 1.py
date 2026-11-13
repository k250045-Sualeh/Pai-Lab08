import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"data.csv", keep_default_na=False)

d1 = df[df['scenario'] == '01_StudyVsScore']

sns.scatterplot(data=d1, x='study_hours', y='exam_score',
                hue='prep_course', style='prep_course', s=100)

plt.title('Study Hours vs. Exam Score by Prep')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()