# research_script.py
# Lightweight reproducible structure for the DeepThought research assignment.
# This script does not scrape paid sites. It shows how the scored CSV was structured.

import csv

WEIGHTS = {
    "Strong": 1.0,
    "Moderate": 0.5,
    "Weak": 0.0,
    "Fail": 0.0,
}

CRITERIA_WEIGHTS = {
    "C1": 10,
    "C2": 5,
    "C3": 25,
    "C4": 20,
    "C5": 20,
    "C6": 20,
}

def score_row(c1, c2, c3, c4, c5, c6):
    values = [c1, c2, c3, c4, c5, c6]
    total = 0
    for key, rating in zip(CRITERIA_WEIGHTS, values):
        total += CRITERIA_WEIGHTS[key] * WEIGHTS.get(rating, 0)
    return int(total)

def band(score):
    if score >= 80:
        return "A — Strong Federer"
    if score >= 60:
        return "B — Probable Federer"
    if score >= 40:
        return "C — Borderline"
    return "D — Not ICP"

print("Use this script structure to recalculate scores after manual verification.")
