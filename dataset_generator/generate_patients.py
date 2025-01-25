import csv
import random
from faker import Faker

# Initialize Faker with Indian locale
fake = Faker('en_IN')

# Generate random realistic conditions, medications, and departments
conditions = [
    "Hypertension", "Diabetes", "Asthma", "Chronic Kidney Disease",
    "Coronary Artery Disease", "Stroke", "Arthritis", "Depression"
]
medications = [
    "Metformin", "Lisinopril", "Ramipril", "Clopidogrel", "Aspirin",
    "Statins", "Beta Blockers", "Inhalers", "Physiotherapy", "Dietary Changes"
]
departments = [
    "Endocrinology", "Cardiology", "Neurology", "Orthopedics",
    "Psychiatry", "Pulmonology", "Nephrology", "Dermatology"
]

# Helper function to generate random patient data
def generate_patient_data(patient_id):
    name = fake.name()
    age = random.randint(18, 80)
    gender = random.choice(["Male", "Female"])
    department = random.choice(departments)
    condition = random.sample(conditions, random.randint(1, 2))
    medication = random.sample(medications, random.randint(1, 2))
    last_visit = fake.date_between(start_date="-2y", end_date="today")
    diagnosis_history = ", ".join(condition)
    treatment_history = ", ".join(medication)
    
    return {
        "PatientID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Department": department,
        "DiagnosisHistory": diagnosis_history,
        "TreatmentHistory": treatment_history,
        "Conditions": ", ".join(condition),
        "Medications": ", ".join(medication),
        "LastVisit": last_visit.strftime("%Y-%m-%d")
    }

# Generate 10,000 records
records = [generate_patient_data(i + 1) for i in range(10000)]

# Write to CSV
output_file = "patients_large.csv"
fieldnames = [
    "PatientID", "Name", "Age", "Gender", "Department", 
    "DiagnosisHistory", "TreatmentHistory", "Conditions", 
    "Medications", "LastVisit"
]

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(f"{len(records)} patient records written to {output_file}.")
