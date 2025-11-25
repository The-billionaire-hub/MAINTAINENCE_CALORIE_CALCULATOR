import math

# --- Activity Factors ---
ACTIVITY_FACTORS = {
    "sedentary": 1.2,          # No exercise, mostly sitting
    "lightly_active": 1.375,   # 2–3 light workouts/week
    "moderately_active": 1.55, # 3–5 workouts/week (Default)
    "very_active": 1.725,      # Intense training, manual job
    "super_active": 1.9        # Athlete-level training
}

def calculate_bmr(weight_kg: float, height_cm: float, age: int, gender: str) -> float:
    """
    Calculates the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor formula.

    Formula: 10 * W(kg) + 6.25 * H(cm) - 5 * A + S
    S = +5 for Men, -161 for Women

    Args:
        weight_kg (float): Weight in kilograms.
        height_cm (float): Height in centimeters.
        age (int): Age in years.
        gender (str): Must be 'male' or 'female'.

    Returns:
        float: The calculated BMR in calories/day.
    """
    if gender.lower() not in ['male', 'female']:
        raise ValueError("Gender must be 'male' or 'female'.")

    base_bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age)

    if gender.lower() == 'male':
        # BMR for Men: + 5
        bmr = base_bmr + 5
    else:
        # BMR for Women: - 161
        bmr = base_bmr - 161

    return bmr

def calculate_tdee(bmr: float, activity_level: str) -> float:
    """
    Calculates the Total Daily Energy Expenditure (TDEE) or Maintenance Calories.

    Formula: BMR * Activity Factor

    Args:
        bmr (float): Basal Metabolic Rate.
        activity_level (str): One of the keys from ACTIVITY_FACTORS 
                              (e.g., 'moderately_active').

    Returns:
        float: The calculated TDEE (Maintenance Calories) in calories/day.
    """
    activity_level = activity_level.lower().replace(" ", "_")
    
    if activity_level not in ACTIVITY_FACTORS:
        raise ValueError(f"Invalid activity level. Choose from: {', '.join(ACTIVITY_FACTORS.keys())}")
    
    activity_factor = ACTIVITY_FACTORS[activity_level]
    
    tdee = bmr * activity_factor
    
    return tdee

# --- Example Usage based on your request ---
if __name__ == "__main__":
    
    # Example Inputs
    age = 20
    height_cm = 165
    weight_kg = 53
    gender = "male" # Change to "female" for the other formula
    activity_level = "lightly_active" # Factor 1.375
    
    print("--- Maintenance Calorie Calculator (Mifflin-St Jeor) ---")
    print(f"Inputs: {gender.capitalize()}, {age} years, {height_cm} cm, {weight_kg} kg, {activity_level.replace('_', ' ').capitalize()}")

    try:
        # Step 1: Calculate BMR
        bmr_result = calculate_bmr(weight_kg, height_cm, age, gender)
        print(f"\n1. Basal Metabolic Rate (BMR): {round(bmr_result, 2)} kcal/day")

        # Step 2: Calculate TDEE (Maintenance Calories)
        tdee_result = calculate_tdee(bmr_result, activity_level)
        print(f"2. Maintenance Calories (TDEE): {math.ceil(tdee_result)} kcal/day")
        
    except ValueError as e:
        print(f"\nError: {e}")
