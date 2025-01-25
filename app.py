from flask import Flask, render_template, request, jsonify
import asyncio
from chatbot import get_patient_summary

# Assuming the necessary imports and functions from your existing code are already here.
# import csv, logging, etc.

app = Flask(__name__)

# Flask route for displaying the form and handling the patient summary request
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_patient_summary', methods=['POST'])
async def get_patient_summary_route():
    patient_id = request.form['patient_id']
    
    # Use the existing `get_patient_summary` function to get the summary
    result = await get_patient_summary(patient_id)
    
    if "error" in result:
        return jsonify({"error": result["error"]})
    
    # Return the patient details and summary as JSON
    return jsonify({
        "patient_details": result["patient_details"],
        "summary": result["summary"]
    })

if __name__ == "__main__":
    app.run(debug=True)
