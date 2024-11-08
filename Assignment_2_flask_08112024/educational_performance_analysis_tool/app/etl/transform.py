import pandas as pd

def validate_and_transform(data):
 data = data.dropna()  # Remove missing values
 data['score'] = data['score'].astype(float)
 data['grade'] = data['score'].apply(assign_grade)
 return data

def assign_grade(score):
 if score >= 90: return 'A'
 elif score >= 80: return 'B'
 elif score >= 70: return 'C'
 elif score >= 60: return 'D'
 else: return 'F'
