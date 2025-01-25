import csv
import random
from faker import Faker

# Initialize Faker with Indian locale
fake = Faker('en_IN')

# Generate random realistic conditions, medications, and departments
conditions = [
    "Hypertension", "Diabetes", "Asthma", "Chronic Kidney Disease",
    "Coronary Artery Disease", "Stroke", "Arthritis", "Depression",
    "Migraine", "Tuberculosis", "Liver Cirrhosis", "Glaucoma"
]
medications = [
    "Metformin", "Lisinopril", "Ramipril", "Clopidogrel", "Aspirin",
    "Statins", "Beta Blockers", "Inhalers", "Physiotherapy", "Dietary Changes",
    "Amoxicillin", "Ibuprofen", "Paracetamol", "Insulin"
]
departments = [
    "Endocrinology", "Cardiology", "Neurology", "Orthopedics",
    "Psychiatry", "Pulmonology", "Nephrology", "Dermatology",
    "Ophthalmology", "Gastroenterology", "Pediatrics"
]
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
allergies = ["None", "Peanuts", "Shellfish", "Penicillin", "Dust", "Pollen", "Dairy"]
appointment_frequencies = ["Monthly", "Quarterly", "Annually"]

# Helper function to generate random patient data
def generate_patient_data(patient_id):
    name = fake.name()
    age = random.randint(18, 80)
    gender = random.choice(["Male", "Female"])
    department = random.choice(departments)
    condition = random.sample(conditions, random.randint(1, 3))
    medication = random.sample(medications, random.randint(1, 3))
    last_visit = fake.date_between(start_date="-2y", end_date="today")
    diagnosis_history = ", ".join(condition)
    treatment_history = ", ".join(medication)
    emergency_contact = fake.phone_number()
    blood_group = random.choice(blood_groups)
    allergy = random.choice(allergies)
    address = fake.address().replace("\n", ", ")
    appointment_frequency = random.choice(appointment_frequencies)
    ongoing_treatment = random.choice(["Yes", "No"])
    
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
        "LastVisit": last_visit.strftime("%Y-%m-%d"),
        "EmergencyContact": emergency_contact,
        "BloodGroup": blood_group,
        "Allergies": allergy,
        "Address": address,
        "AppointmentFrequency": appointment_frequency,
        "OngoingTreatment": ongoing_treatment
    }

# Generate 10,000 records
records = [generate_patient_data(i + 1) for i in range(10000)]

# Write to CSV
output_file = "patients_detailed.csv"
fieldnames = [
    "PatientID", "Name", "Age", "Gender", "Department",
    "DiagnosisHistory", "TreatmentHistory", "Conditions",
    "Medications", "LastVisit", "EmergencyContact", "BloodGroup",
    "Allergies", "Address", "AppointmentFrequency", "OngoingTreatment"
]

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(f"{len(records)} detailed patient records written to {output_file}.")
