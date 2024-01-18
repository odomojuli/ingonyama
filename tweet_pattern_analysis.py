import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generating a more realistic set of synthetic tweet timestamps to mimic the described pattern:
# Tweeting during commute, at lunch break, commuting home, and intermittently until bed.

def generate_synthetic_data():
    np.random.seed(42)  # For reproducible results

    # Creating base timestamps for a month
    base_timestamps = pd.date_range(start='2024-01-01', end='2024-01-31', freq='H').to_series()

    # Defining typical activity periods (in hours): morning commute, lunch, evening commute, evening
    morning_commute = (base_timestamps.dt.hour >= 7) & (base_timestamps.dt.hour <= 9)
    lunch_time = base_timestamps.dt.hour == 12
    evening_commute = (base_timestamps.dt.hour >= 17) & (base_timestamps.dt.hour <= 19)
    evening = (base_timestamps.dt.hour >= 20) & (base_timestamps.dt.hour <= 23)

    # Combining all periods
    active_periods = base_timestamps[morning_commute | lunch_time | evening_commute | evening]

    # Randomly selecting timestamps within these periods to simulate tweeting activity
    # Adjust the number of samples as needed
    return active_periods.sample(n=150)  # Assuming around 150 tweets in a month

# Generating the synthetic data
sampled_timestamps_realistic = generate_synthetic_data()

# Creating a DataFrame
df_synthetic_realistic = pd.DataFrame({'Timestamp': sampled_timestamps_realistic})

# Extracting the hour from each timestamp
df_synthetic_realistic['Hour'] = df_synthetic_realistic['Timestamp'].dt.hour

# Grouping by hour and counting tweets
hourly_distribution_realistic = df_synthetic_realistic.groupby('Hour').size()

# Ensure all hours are represented in the data
hourly_distribution_realistic_full = hourly_distribution_realistic.reindex(range(24), fill_value=0)

# Plotting the realistic hourly distribution as a bar chart
plt.figure(figsize=(12, 6))
plt.bar(hourly_distribution_realistic_full.index, hourly_distribution_realistic_full.values, color='teal')

plt.title('Realistic Synthetic Hourly Distribution of Tweets (Patterned Behavior)')
plt.xlabel('Hour of the Day (00:00 to 23:59 EST)')
plt.ylabel('Number of Tweets (Synthetic Data)')
plt.xticks(range(24))  # Ensure all hours are shown
plt.grid(axis='y')
plt.show()

