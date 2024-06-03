# StellarCandidateSelector

StellarCandidateSelector is a sophisticated candidate selection algorithm that leverages multi-criteria analysis and machine learning to identify top software engineering candidates. This tool features flexible filtering, score adjustment, and detailed visualizations to streamline the recruitment process.

## Features

- **Flexible Filtering**:
  - Configure criteria and weights via JSON.
  - Filter candidates based on minimum experience and required skills.
- **Machine Learning Integration**:
  - Adjust candidate scores using a linear regression model.
- **Visualization**:
  - Bar chart representation of candidate final scores.
- **Detailed Logging**:
  - Comprehensive logging of the selection process.

## Technologies Used

- **Python**: The application is written in Python.
- **Pandas**: Utilized for data manipulation and analysis.
- **scikit-learn**: Used for implementing the machine learning model.
- **Matplotlib**: For visualizing candidate scores.

- <img width="1912" alt="Screenshot 2024-06-03 at 3 29 43 PM" src="https://github.com/shuddha2021/stellar-candidate-selector/assets/81951239/ca4d17bb-2b2a-469b-876b-15e61162d395">

## Core Logic

- **Flexible Filtering**:
  - Loads selection criteria from a JSON file.
  - Filters candidates based on minimum experience and required skills.
- **Skill Match Score Calculation**:
  - Calculates a skill match score considering required and preferred skills.
- **Machine Learning Score Adjustment**:
  - Uses a linear regression model to adjust candidate scores.
- **Final Score Calculation**:
  - Combines experience, skill match score, and adjusted score with configurable weights.
- **Visualization**:
  - Plots a bar chart of the candidates' final scores for easy comparison.

## Project Structure

The project consists of the following main files:

- `main.py`: Contains the implementation of the candidate selection logic, including filtering, score calculation, and visualization.
- `criteria.json`: Defines the selection criteria and weights for the candidate evaluation process.
- `requirements.txt`: Lists the project's dependencies.

## Getting Started

To get started with this project:

1. Clone the repository.
   ```bash
   git clone https://github.com/yourusername/stellar-candidate-selector.git

 2. Navigate to the project directory.
    cd stellar-candidate-selector
 3. Install the required packages.
    pip install -r requirements.txt
 4. Run the application.
    python main.py

## Why This Project Is Useful

 This project serves as a practical example of implementing a sophisticated candidate selection algorithm using Python. It demonstrates various concepts such as data manipulation with Pandas, machine learning model integration with scikit-learn, and data visualization with Matplotlib in a real-world scenario.

## Contributing

Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License 
