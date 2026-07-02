def health_risk(bmi, age, symptom_count):

    score = 0

    if bmi >= 30:
        score += 2
    elif bmi >= 25:
        score += 1

    if age >= 60:
        score += 2
    elif age >= 40:
        score += 1

    if symptom_count >= 6:
        score += 2
    elif symptom_count >= 3:
        score += 1

    if score <= 2:
        return "Low"
    elif score <= 4:
        return "Medium"
    else:
        return "High"