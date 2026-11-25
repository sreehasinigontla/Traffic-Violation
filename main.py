
# Traffic Violation Penalty Calculator

# Sample Fine Rules (Illustrative Only)
fine_rules = {
    "overspeeding": {
        "two_wheeler": 1000,
        "car": 1500,
        "commercial": 2000,
        "points": 2
    },

    "signal_jump": {
        "two_wheeler": 1000,
        "car": 1000,
        "commercial": 1500,
        "points": 3
    },

    "no_helmet": {
        "two_wheeler": 500,
        "car": 0,
        "commercial": 0,
        "points": 1
    },

    "no_seatbelt": {
        "two_wheeler": 0,
        "car": 500,
        "commercial": 500,
        "points": 1
    },

    "drunk_driving": {
        "two_wheeler": 5000,
        "car": 5000,
        "commercial": 10000,
        "points": 5
    },

    "dangerous_driving": {
        "two_wheeler": 5000,
        "car": 5000,
        "commercial": 10000,
        "points": 5
    }
}

# Vehicle categories
vehicles = ["two_wheeler", "car", "commercial"]

# Serious offences requiring review
serious_offences = [
    "drunk_driving",
    "dangerous_driving"
]

# Disqualification threshold (sample)
DISQUALIFICATION_POINTS = 10


# Function to calculate penalty
def calculate_penalty(vehicle, offence, repeated):

    base_fine = fine_rules[offence][vehicle]

    if repeated:
        fine = base_fine * 2
    else:
        fine = base_fine

    points = fine_rules[offence]["points"]

    return fine, points


# Function to check disqualification conditions
def check_disqualification(violations, total_points):

    reasons = []

    for violation in violations:

        if violation["offence"] in serious_offences:
            reasons.append(
                "Serious offence: " + violation["offence"]
            )

    if total_points >= DISQUALIFICATION_POINTS:
        reasons.append(
            "Total violation points reached the threshold"
        )

    return reasons


# Main program
print("==========================================")
print("     TRAFFIC VIOLATION PENALTY CALCULATOR")
print("==========================================")

print("\nVehicle Categories:")
print("1. Two Wheeler")
print("2. Car")
print("3. Commercial Vehicle")

vehicle_options = {
    "1": "two_wheeler",
    "2": "car",
    "3": "commercial"
}

while True:

    choice = input("\nSelect vehicle category (1-3): ")

    if choice in vehicle_options:
        vehicle = vehicle_options[choice]
        break

    print("Invalid vehicle category. Try again.")


# Number of violations
while True:

    try:
        n = int(input("Enter number of violations: "))

        if n > 0:
            break

        print("Enter at least one violation.")

    except ValueError:
        print("Enter a valid whole number.")


violations = []
total_fine = 0
total_points = 0

# Available offences
offence_list = list(fine_rules.keys())

# Process each violation
for i in range(n):

    print("\n---------- Violation", i + 1, "----------")

    print("Available Offences:")

    for j in range(len(offence_list)):
        print(j + 1, ".", offence_list[j])

    while True:

        try:
            offence_choice = int(
                input("Select offence number: ")
            )

            if 1 <= offence_choice <= len(offence_list):
                offence = offence_list[offence_choice - 1]
                break

            print("Invalid offence selection.")

        except ValueError:
            print("Enter a valid number.")

    # Check whether offence is repeated
    while True:

        repeated = input(
            "Is this a repeat offence? (yes/no): "
        ).lower()

        if repeated in ["yes", "no"]:
            break

        print("Enter yes or no.")

    is_repeated = repeated == "yes"

    # Calculate penalty
    fine, points = calculate_penalty(
        vehicle, offence, is_repeated
    )

    violation = {
        "offence": offence,
        "repeated": is_repeated,
        "fine": fine,
        "points": points
    }

    violations.append(violation)

    total_fine += fine
    total_points += points

    print("Fine Amount: Rs.", fine)
    print("Violation Points:", points)


# Check disqualification
disqualification_reasons = check_disqualification(
    violations, total_points
)


# Final Report
print("\n==========================================")
print("             FINAL PENALTY REPORT")
print("==========================================")

print("Vehicle Category:", vehicle)

print("\nViolation Details:")

for i in range(len(violations)):

    v = violations[i]

    print("\nViolation:", i + 1)
    print("Offence:", v["offence"])
    print("Repeat Offence:", v["repeated"])
    print("Penalty: Rs.", v["fine"])
    print("Points:", v["points"])


print("\n------------------------------------------")
print("Total Violations:", len(violations))
print("Total Penalty: Rs.", total_fine)
print("Total Violation Points:", total_points)

print("\n========== DISQUALIFICATION STATUS ==========")

if len(disqualification_reasons) > 0:

    print("DISQUALIFICATION REVIEW REQUIRED")

    for reason in disqualification_reasons:
        print("-", reason)

else:

    print("No sample disqualification condition triggered.")


print("\nTraffic Penalty Calculation Completed!")
