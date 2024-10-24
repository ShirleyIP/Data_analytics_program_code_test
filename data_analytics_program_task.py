import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load csv file
df = pd.read_csv('game_data.csv')

# display original dataframe
print('Original DataFrame:')
print(df)

# clean data by remove missing values
df_cleaned = df.dropna()

# create score_category colunmn
def categorize_score(score):
    if score < 50:
        return 'Low'
    elif 50 <= score < 80:
        return 'Medium'
    else:
        return 'High'

df_cleaned['score_category'] = df_cleaned['score'].apply(categorize_score)

# group data by level & cal avg score for each level
average_scores = df_cleaned.groupby('level')['score'].mean().reset_index()
average_scores['score'] = average_scores['score'].map('{:.2f}'.format)

# display results
print("\nCleaned DataFrame with Score Category:")
print(df_cleaned)

print("\nAverage Scores by Level:")
print(average_scores)

# Calculate the average score of players across all levels
average_score_across_all_levels = df_cleaned['score'].mean()
print(f'What is the average score of players across all levels? \nAnswer: {average_score_across_all_levels:.2f}')

# Identify which level has the highest average score
level_has_the_highest_average_score = average_scores['score'].idxmax()
print(f'Which level has the highest average score? \nAnswer: {level_has_the_highest_average_score}')

# Count how many players scored in the 'High' category
player_scored_in_high_category = df_cleaned[df_cleaned['score_category'] == 'High']['player_id'].nunique()
print(f"How many players scored in the 'High' category? \nAnswer: {player_scored_in_high_category}")

# Calculate total scores per player
total_scores = df_cleaned.groupby('player_id')['score'].sum().reset_index()
total_scores['score'] = total_scores['score'].map('{:.2f}'.format)  # Format total scores to 2 decimal places
print("\nTotal Scores per Player:")
print(total_scores)

# Identify players with consistent high scores (e.g., scores > 70)
consistent_high_scorers = df_cleaned[df_cleaned['score'] > 70].groupby('player_id').size()
print("\nPlayers with Consistent High Scores (scores > 70):")
print(consistent_high_scorers)

# Score trends over time (assuming 'timestamp' is in a proper datetime format)
df_cleaned['date'] = pd.to_datetime(df_cleaned['timestamp']).dt.date
score_trends = df_cleaned.groupby('date')['score'].mean().reset_index()
# score_trends['score'] = score_trends['score'].map('{:.2f}'.format)  # Format score trends to 2 decimal places
print("\nScore Trends Over Time:")
print(score_trends)

# Statistical summary of scores
score_statistics = df_cleaned['score'].describe()
print("\nStatistical Summary of Scores:")
print(score_statistics[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']].apply(lambda x: f"{x:.2f}"))


# Function to query highest score for a specific player
def query_player_highest_score(player_id):
    # Filter the cleaned DataFrame to get records for the specific player
    player_records = df_cleaned[df_cleaned['player_id'] == player_id]
    
    # Check if the player has any records
    if player_records.empty:
        return f"No records found for player ID {player_id}."
    
    # Find the highest score and corresponding level
    highest_score = player_records['score'].max()
    level_achieved = player_records[player_records['score'] == highest_score]['level'].values[0]
    
    return highest_score, level_achieved

# Input player ID from terminal
player_id_to_query = int(input("Enter Player ID to query: "))  # Convert input to integer

# Example usage of the function
result = query_player_highest_score(player_id_to_query)

# Output the result
if isinstance(result, tuple):
    highest_score, level_achieved = result
    print(f"Player ID: {player_id_to_query}\nHighest Score: {highest_score}\nLevel Achieved: {level_achieved}")
else:
    print(result)


# Set a consistent figure size
fig_size = (10, 6)

# Define the color palette
colors = {
    'bar': '#1C3F72',  # Dark Blue
    'pie': ['#FF6B6B', '#FF9A8B', '#FFB3E6'],  # Coral Red, Peach, Soft Pink
    'box': {'boxes': '#FF9A8B', 'whiskers': '#1C3F72'},  # Peach for boxes, Dark Blue for whiskers
    'line': '#FF6B6B',  # Coral Red
    'bar plot': '#A0DFF7'   # Light Blue
}

# Create a bar chart that shows the average score for each level
average_scores = df_cleaned.groupby('level')['score'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
average_scores.plot(x='level', y='score', kind='bar', ax=ax, legend=False, color=colors['bar'])
ax.set_title('Average Score by Level', fontsize=14)
ax.set_xlabel('Level', fontsize=10)
ax.set_ylabel('Average Score', fontsize=10)
ax.bar_label(ax.containers[0])  # Add data labels on bars
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Create a pie chart that displays the distribution of score categories ('Low', 'Medium', 'High').
distribution_of_score_categories = df_cleaned['score_category'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
distribution_of_score_categories.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax, colors=colors['pie'])
ax.set_title('Distribution of Score Categories', fontsize=16)
ax.set_ylabel('')  # Hide the y-label for a cleaner look
plt.show()

# Visualization: Box plot of scores by level
fig, ax = plt.subplots(figsize=(10, 6))
df_cleaned.boxplot(column='score', by='level', ax=ax, boxprops=dict(color=colors['box']['boxes']), 
                   whiskerprops=dict(color=colors['box']['whiskers']))
ax.set_title('Score Distribution by Level', fontsize=14)
plt.suptitle('')  # Suppress the default title
ax.set_xlabel('Level', fontsize=10)
ax.set_ylabel('Score', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization: Line chart for average score over time
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(score_trends['date'], score_trends['score'], marker='o', color=colors['line'], linewidth=2)
ax.set_title('Average Score Over Time', fontsize=14)
ax.set_xlabel('Date', fontsize=10)
ax.set_ylabel('Average Score', fontsize=10)
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Visualization: Bar plot for Total Scores per Player
total_scores = df_cleaned.groupby('player_id')['score'].sum().reset_index()
fig, ax = plt.subplots(figsize=fig_size)
sns.barplot(data=total_scores, x='player_id', y='score', palette=[colors['bar plot']])
ax.set_title('Total Scores per Player', fontsize=14)
ax.set_xlabel('Player ID', fontsize=10)
ax.set_ylabel('Total Score', fontsize=10)
plt.xticks(rotation=45)
plt.show()
