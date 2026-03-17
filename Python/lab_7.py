# -------------------------------
# HOSPITAL MANAGEMENT SYSTEM
# -------------------------------

# Global list to store patient records
patients = []


# -------------------------------
# BMI Calculation
# -------------------------------
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


# -------------------------------
# Blood Pressure Classification
# -------------------------------
def classify_bp(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif (120 <= systolic <= 139) or (80 <= diastolic <= 89):
        return "Prehypertension"
    else:
        return "Hypertension"


# -------------------------------
# Diabetes Risk Classification
# -------------------------------
def classify_diabetes(sugar):
    if sugar < 100:
        return "Normal"
    elif 100 <= sugar <= 125:
        return "Prediabetic"
    else:
        return "Diabetic"


# -------------------------------
# Overall Risk Calculation
# -------------------------------
def calculate_overall_risk(bmi_category, bp_category, diabetes_category, age):
    if bmi_category == "Obese" and bp_category == "Hypertension":
        return "High"
    elif diabetes_category == "Diabetic" or age > 60:
        return "Moderate"
    else:
        return "Low"


# -------------------------------
# Consultation Fee Calculation
# -------------------------------
def calculate_fee(risk):
    if risk == "Low":
        return 500
    elif risk == "Moderate":
        return 1000
    else:
        return 2000


# -------------------------------
# Register Patient
# -------------------------------
def register_patient():
    print("\n--- Register New Patient ---")
    
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (m): "))
    systolic = int(input("Enter Systolic BP: "))
    diastolic = int(input("Enter Diastolic BP: "))
    sugar = float(input("Enter Fasting Blood Sugar: "))

    bmi = calculate_bmi(weight, height)
    bmi_category = classify_bmi(bmi)
    bp_category = classify_bp(systolic, diastolic)
    diabetes_category = classify_diabetes(sugar)
    overall_risk = calculate_overall_risk(bmi_category, bp_category, diabetes_category, age)
    fee = calculate_fee(overall_risk)

    patient = {
        "Name": name,
        "Age": age,
        "BMI": bmi,
        "BMI Category": bmi_category,
        "BP Category": bp_category,
        "Diabetes Category": diabetes_category,
        "Risk": overall_risk,
        "Fee": fee
    }

    patients.append(patient)
    print("\nPatient Registered Successfully!\n")


# -------------------------------
# Display All Patients
# -------------------------------
def display_patients():
    if not patients:
        print("\nNo patients registered yet.")
        return

    print("\n--- Patient Records ---")
    for i, p in enumerate(patients, start=1):
        print(f"\nPatient {i}")
        for key, value in p.items():
            print(f"{key}: {value}")

# -------------------------------
# Hospital Summary Statistics
# -------------------------------
def hospital_summary():
    if not patients:
        print("\nNo data available.")
        return

    total_patients = len(patients)
    total_fee = sum(p["Fee"] for p in patients)
    avg_bmi = sum(p["BMI"] for p in patients) / total_patients

    high_risk = sum(1 for p in patients if p["Risk"] == "High")
    moderate_risk = sum(1 for p in patients if p["Risk"] == "Moderate")
    low_risk = sum(1 for p in patients if p["Risk"] == "Low")

    print("\n--- Hospital Summary ---")
    print("Total Patients:", total_patients)
    print("Average BMI:", round(avg_bmi, 2))
    print("Total Consultation Revenue: ₹", total_fee)
    print("High Risk Patients:", high_risk)
    print("Moderate Risk Patients:", moderate_risk)
    print("Low Risk Patients:", low_risk)


# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("\n====== HOSPITAL MENU ======")
        print("1. Register Patient")
        print("2. Display All Patients")
        print("3. Hospital Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient()
        elif choice == "2":
            display_patients()
        elif choice == "3":
            hospital_summary()
        elif choice == "4":
            print("Exiting Program...")
            break
        else:
            print("Invalid choice! Try again.")


# Run Program
main()