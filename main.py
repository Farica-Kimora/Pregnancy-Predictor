import random

# Simulate data for a hypothetical experiment
def generate_data(sample_size):
    data = []
    for _ in range(sample_size):
        age = random.randint(18, 40)
        menstrual_cycle_length = random.randint(25, 35)
        days_since_last_period = random.randint(1, menstrual_cycle_length)
        is_pregnant = random.choice([True, False])
        data.append((age, menstrual_cycle_length, days_since_last_period, is_pregnant))
    return data

# Analyze data (this is a basic example, not a real pregnancy prediction)
def analyze_data(data):
    predictions = []
    for entry in data:
        age, cycle_length, days_since_last_period, is_pregnant = entry
        # Include some basic rules for educational purposes (not based on actual medical criteria)
        prediction = age > 25 and days_since_last_period > cycle_length / 2
        predictions.append((entry, prediction))
    return predictions

# Example usage
sample_size = 50
simulated_data = generate_data(sample_size)
predictions = analyze_data(simulated_data)

# Display results
for entry, prediction in predictions:
    print(f"Age: {entry[0]}, Cycle Length: {entry[1]}, Days Since Last Period: {entry[2]}, Predicted Pregnancy: {prediction}")
