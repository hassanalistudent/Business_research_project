import pandas as pd
import statsmodels.api as sm

# Assuming df is your DataFrame and already contains the interaction terms
# Example columns: 'Satisfaction', 'Food_Year_interaction', 'Hygiene_Year_interaction'

# Define the dependent and independent variables
X = df[['Food_Year_interaction', 'Hygiene_Year_interaction']]
X = sm.add_constant(X)  # Adds the intercept term
y = df['Satisfaction']

# Fit the OLS model
model = sm.OLS(y, X).fit()

# Print the summary
print(model.summary())
