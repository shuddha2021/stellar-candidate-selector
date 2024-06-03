import pandas as pd
import json
import logging
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample input data
candidates = [
    {"name": "John Doe", "experience": 5, "skills": ["Python", "Java", "SQL"], "score": 85},
    {"name": "Jane Smith", "experience": 3, "skills": ["Python", "JavaScript", "React"], "score": 90},
    {"name": "Bob Johnson", "experience": 8, "skills": ["Java", "C++", "Database Design"], "score": 92},
    {"name": "Alice Williams", "experience": 2, "skills": ["Python", "Django", "Docker"], "score": 88},
    {"name": "Tom Brown", "experience": 6, "skills": ["Java", "Spring", "AWS"], "score": 87},
]

# Convert the list of dictionaries to a pandas DataFrame
candidates_df = pd.DataFrame(candidates)

# Load selection criteria from JSON
criteria_json = '''
{
    "min_experience": 3,
    "required_skills": ["Python", "Java"],
    "preferred_skills": ["AWS", "React"],
    "experience_weight": 0.3,
    "skills_weight": 0.4,
    "score_weight": 0.3
}
'''
criteria = json.loads(criteria_json)

# Define the criteria for selecting the best candidate
min_experience = criteria["min_experience"]
required_skills = criteria["required_skills"]
preferred_skills = criteria["preferred_skills"]
weights = criteria["experience_weight"], criteria["skills_weight"], criteria["score_weight"]

# Filter candidates based on minimum experience and required skills
filtered_candidates = candidates_df[
    (candidates_df["experience"] >= min_experience) &
    (candidates_df["skills"].apply(lambda skills: all(skill in skills for skill in required_skills)))
].copy()  # Use .copy() to avoid SettingWithCopyWarning

# Calculate a skill match score
def skill_match_score(skills, required, preferred):
    score = sum(1 for skill in required if skill in skills) + 0.5 * sum(1 for skill in preferred if skill in skills)
    return score

# Add skill match score to candidates
filtered_candidates.loc[:, "skill_match_score"] = filtered_candidates["skills"].apply(
    lambda skills: skill_match_score(skills, required_skills, preferred_skills))

# Adjust scores using a simple machine learning model
X = filtered_candidates[["experience", "skill_match_score"]]
y = filtered_candidates["score"]
model = LinearRegression().fit(X, y)
filtered_candidates.loc[:, "adjusted_score"] = model.predict(X)

# Calculate the final score with weightage
filtered_candidates.loc[:, "final_score"] = (
    weights[0] * filtered_candidates["experience"] +
    weights[1] * filtered_candidates["skill_match_score"] +
    weights[2] * filtered_candidates["adjusted_score"]
)

# Sort the filtered candidates by final score in descending order
sorted_candidates = filtered_candidates.sort_values(by="final_score", ascending=False)

# Select the top candidate
best_candidate = sorted_candidates.iloc[0]

logging.info("Best Candidate:")
logging.info(best_candidate)

# Plot the candidates' scores
plt.figure(figsize=(10, 6))
plt.bar(sorted_candidates["name"], sorted_candidates["final_score"], color='skyblue')
plt.xlabel('Candidate')
plt.ylabel('Final Score')
plt.title('Candidates Final Scores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Best Candidate:")
print(best_candidate)
