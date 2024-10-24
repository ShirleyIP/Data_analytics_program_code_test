# Game Data Analysis

## Overview
This project analyzes game data to enhance understanding of player performance. The analysis includes data cleaning, categorization of scores, and various visualizations to assess player engagement across different levels and time periods.

## Contents
- [Requirements](#requirements)
- [Data Preparation](#data-preparation)
- [Key Analysis Steps](#key-analysis-steps)
- [Visualizations](#visualizations)
- [Query Function](#query-function)
- [Example Usage](#example-usage)
- [Conclusion](#conclusion)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Requirements
To run this project, you need the following Python libraries:
- `pandas`
- `matplotlib`
- `seaborn`

You can install these libraries using pip:

```bash
pip install pandas matplotlib seaborn
```

## Data Preparation
1. **Load CSV File**: The data is loaded from `game_data.csv`.
2. **Clean Data**: Missing values are removed to ensure accurate analysis.
3. **Categorize Scores**: Scores are categorized into 'Low', 'Medium', and 'High' based on predefined thresholds.

## Key Analysis Steps
1. **Average Scores by Level**: The average score for each level is calculated and displayed.
2. **Overall Average Score**: The average score of players across all levels is computed.
3. **Highest Scoring Level**: Identification of the level with the highest average score.
4. **High Category Players**: Count of unique players who scored in the 'High' category.
5. **Total Scores per Player**: Calculation of total scores for each player.
6. **Consistent High Scorers**: Identification of players with scores consistently above 70.

## Visualizations
The analysis includes several visualizations to better understand the data:
- **Bar Chart**: Displays the average score by level.
- **Pie Chart**: Shows the distribution of score categories.
- **Box Plot**: Illustrates score distributions across different levels.
- **Line Chart**: Tracks average score trends over time.
- **Bar Plot**: Represents total scores per player.

## Query Function
A function is provided to query the highest score achieved by a specific player, along with the corresponding level. Users can input a player ID to retrieve this information.

## Example Usage
To use the query function, run the script and input a valid player ID when prompted:

```python
Enter Player ID to query: 123
```

## Conclusion
This project provides a comprehensive analysis of player performance data, offering insights into engagement and trends. The visualizations and data categorization help in identifying key areas for improvement.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
Thanks to the contributors and libraries that made this analysis possible.
