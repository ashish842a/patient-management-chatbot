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
    "Amoxicillin", "Ibuprofen", "Paracetamol", "Insulin", "Losartan"
]
departments = [
    "Endocrinology", "Cardiology", "Neurology", "Orthopedics",
    "Psychiatry", "Pulmonology", "Nephrology", "Dermatology",
    "Ophthalmology", "Gastroenterology", "Pediatrics"
]
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
allergies = ["None", "Peanuts", "Shellfish", "Penicillin", "Dust", "Pollen", "Dairy"]
appointment_frequencies = ["Monthly", "Quarterly", "Annually"]
insurance_types = ["Private", "Government", "None"]
prescriptions = [
    "Amoxicillin 500mg", "Clopidogrel 75mg", "Metformin 500mg", "Ibuprofen 400mg",
    "Ramipril 10mg", "Insulin (Novorapid) 10 units", "Aspirin 100mg", "Statins 40mg"
]
doctor_notes = [
    "Patient advised to monitor blood sugar levels daily.",
    "Scheduled for a follow-up in three months.",
    "Refer to cardiologist for further evaluation.",
    "Instructed to reduce salt intake in diet."
]
past_medical_history = [
    "Appendectomy", "Gallbladder Removal", "Knee Surgery", "No significant past medical history",
    "Asthma childhood", "Tonsillectomy"
]
family_history = [
    "Father had heart disease", "Mother had diabetes", "No significant family history",
    "Brother had hypertension", "Father had stroke"
]
vitals = [
    "BP: 120/80", "BP: 130/90", "Temperature: 98.6°F", "Weight: 70kg", "Height: 5'9\""
]

# Helper function to generate random patient data
def generate_patient_data(patient_id):
    name = fake.name()
    age = random.randint(18, 80)
    gender = random.choice(["Male", "Female"])
    department = random.choice(departments)
    condition = random.sample(conditions, random.randint(1, 3))
    medication = random.sample(medications, random.randint(1, 3))
    prescription = random.choice(prescriptions)
    last_visit = fake.date_between(start_date="-2y", end_date="today")
    diagnosis_history = ", ".join(condition)
    treatment_history = ", ".join(medication)
    emergency_contact = fake.phone_number()
    blood_group = random.choice(blood_groups)
    allergy = random.choice(allergies)
    address = fake.address().replace("\n", ", ")
    appointment_frequency = random.choice(appointment_frequencies)
    ongoing_treatment = random.choice(["Yes", "No"])
    insurance = random.choice(insurance_types)
    doctor_note = random.choice(doctor_notes)
    past_history = random.choice(past_medical_history)
    family_history_info = random.choice(family_history)
    vitals_info = random.choice(vitals)
    
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
        "Prescription": prescription,
        "LastVisit": last_visit.strftime("%Y-%m-%d"),
        "EmergencyContact": emergency_contact,
        "BloodGroup": blood_group,
        "Allergies": allergy,
        "Address": address,
        "AppointmentFrequency": appointment_frequency,
        "OngoingTreatment": ongoing_treatment,
        "Insurance": insurance,
        "DoctorNotes": doctor_note,
        "PastMedicalHistory": past_history,
        "FamilyHistory": family_history_info,
        "Vitals": vitals_info
    }

# Generate 10,0000000  or 1CR records
records = [generate_patient_data(i + 1) for i in range(10000000)]

# Write to CSV
output_file = r"D:\my_work\Doctor\Patient_management_system\Dataset\patients_record_1cr_dataset.csv"
fieldnames = [
    "PatientID", "Name", "Age", "Gender", "Department",
    "DiagnosisHistory", "TreatmentHistory", "Conditions", "Medications", "Prescription",
    "LastVisit", "EmergencyContact", "BloodGroup", "Allergies", "Address",
    "AppointmentFrequency", "OngoingTreatment", "Insurance", "DoctorNotes",
    "PastMedicalHistory", "FamilyHistory", "Vitals"
]

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(f"{len(records)} detailed patient records written to {output_file}.")
