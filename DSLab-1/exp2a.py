import requests
import pandas as pd

# GitHub API URL
url = "https://api.github.com/repos/pandas-dev/pandas/issues"

# Send request
response = requests.get(url)

# Check whether request was successful
response.raise_for_status()

# Convert JSON response to Python object
issues = response.json()

# Convert list of issues into DataFrame
df_issues = pd.DataFrame(issues)

# Display required columns
print(df_issues[["id", "title", "state", "created_at"]].head())