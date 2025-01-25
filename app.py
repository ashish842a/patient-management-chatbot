import csv
from groq import AsyncGroq
from dotenv import load_dotenv
import os
import logging
import asyncio

# Load environment variables from .env file
load_dotenv()

# Fetch the secret API key from environment variable
secret_key = os.getenv('groq_api_key')

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Ensure the API key is available
if not secret_key:
    logging.error("Groq API key not found. Please set it in the .env file.")
    exit(1)

# Function to get LLM response
async def get_llm_response(query, chunks):
    """Generate response from LLM using Groq."""
    try:
        logging.debug("Generating LLM response using Groq.")
        client = AsyncGroq(api_key=secret_key)
        combined_text = "\n".join(chunks)
        chat_completion = await client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a medical assistant. You can only provide answers based strictly on the medical content provided in the document. If the question is outside of the document's content, respond with: 'I am a medical assistant. I don't know about this topic. Please ask a medical question.'" },
                {"role": "user", "content": f"Answer the following based on the text:\n{combined_text}\nQuestion: {query}"}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=2048,
            top_p=1,
            stream=False
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        logging.exception("LLM response generation with Groq failed.")
        raise e

# Function to fetch patient data by ID from CSV
def get_patient_by_id(patient_id, csv_file='patients.csv'):
    """Fetch patient details by patient ID from a CSV file."""
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["PatientID"] == str(patient_id):
                    return row
        return None
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return None

# Main function to get concise patient history
async def get_patient_summary(patient_id, csv_file='patients.csv'):
    """Fetch the patient's summary from their medical records."""
    patient_record = get_patient_by_id(patient_id, csv_file)
    
    if not patient_record:
        return {"error": "Patient not found"}
    
    # Prepare the history text to send to LLM
    full_history = (
        f"Diagnosis History: {patient_record['DiagnosisHistory']}. "
        f"Treatment History: {patient_record['TreatmentHistory']}."
    )
    
    # Call LLM to get concise summary
    summary = await get_llm_response("Summarize the patient's diagnosis and treatment history.", [full_history])
    
    return {
        "patient_details": patient_record,
        "summary": summary
    }

# Test the function
async def test_patient_summary():
    # Test with a valid patient ID
    result = await get_patient_summary("1")
    print(result)

    # Test with an invalid patient ID
    result_invalid = await get_patient_summary("999")
    print(result_invalid)

# Run the test
if __name__ == "__main__":
    asyncio.run(test_patient_summary())
