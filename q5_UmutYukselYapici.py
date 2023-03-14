import pandas as pd

df = pd.read_csv(r'C:\Users\The Machine\Desktop\Data\Questionnaire\country_vaccination_stats.csv')

df['daily_vaccinations']  = df['daily_vaccinations'].fillna(
          df['country'].map(df.groupby('country')['daily_vaccinations'].min()))
df["daily_vaccinations"] =df["daily_vaccinations"].fillna(0)

print(df.groupby('country')['daily_vaccinations'].median().nlargest(3))
