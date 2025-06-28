import pandas as pd
import statsmodels.api as sm

# Load your Excel data
df = pd.read_excel("Cleaned Data for heatmap.xlsx")

# Define dependent and independent variables
X = df[['Food_Year_interaction', 'Hygiene_Year_interaction']]
X = sm.add_constant(X)  # Adds an intercept term
y = df['Satisfection']  # Assuming this is the satisfaction column

# Fit the OLS regression model
model = sm.OLS(y, X).fit()

# Print the full summary
print(model.summary())

