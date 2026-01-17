import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

# Page configuration
st.set_page_config(page_title="Health Insurance Premium Predictor", page_icon="🏥", layout="wide")

# Title and description
st.title("🏥 Health Insurance Premium Predictor")
st.markdown("Enter your details below to predict your insurance premium category")

# Sidebar for input fields
with st.sidebar:
    st.header("📋 Personal Information")
    
    age = st.number_input("Age", min_value=1, max_value=100, value=30, step=1)
    weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0, step=0.1)
    height = st.number_input("Height (meters)", min_value=0.5, value=1.75, step=0.01)
    income_lpa = st.number_input("Annual Income (in lakhs)", min_value=0.0, value=5.0, step=0.5)
    
    st.header("🏢 Location & Lifestyle")
    smoker_option = st.selectbox("Are you a smoker?", ["No", "Yes"])
    smoker = smoker_option == "Yes"
    
    city = st.selectbox("City", [
        "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", 
        "Hyderabad", "Pune", "Jaipur", "Chandigarh", "Other"
    ])
    
    occupation = st.selectbox("Occupation", [
        "retired", "freelancer", "goverment_job", "student", 
        "business_owner", "private_job", "unemployed"
    ])

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Calculated Metrics")
    
    # Calculate and display BMI
    if height > 0:
        bmi = weight / (height ** 2)
        st.metric("BMI", f"{bmi:.2f}")
        
        # BMI category
        if bmi < 18.5:
            bmi_status = "Underweight"
            bmi_color = "🟦"
        elif bmi < 25:
            bmi_status = "Normal"
            bmi_color = "🟩"
        elif bmi < 30:
            bmi_status = "Overweight"
            bmi_color = "🟨"
        else:
            bmi_status = "Obese"
            bmi_color = "🟥"
        
        st.write(f"{bmi_color} Status: **{bmi_status}**")

with col2:
    st.subheader("📝 Summary")
    st.write(f"**Age:** {age} years")
    st.write(f"**Weight:** {weight} kg")
    st.write(f"**Height:** {height} m")
    st.write(f"**Income:** {income_lpa} lakhs per annum")
    st.write(f"**Smoker:** {smoker_option}")
    st.write(f"**City:** {city}")
    st.write(f"**Occupation:** {occupation.replace('_', ' ').title()}")

# Predict button
st.markdown("---")
if st.button("🔮 Predict Premium Category", type="primary", use_container_width=True):
    try:
        # Prepare input data
        input_data = {
            "age": int(age),  # Ensure age is int
            "weight": float(weight),
            "height": float(height),
            "income_lpa": float(income_lpa),
            "smoker": smoker,
            "city": city,
            "occupation": occupation
        }
        
        # Show loading spinner
        with st.spinner("🔍 Analyzing your data and predicting..."):
            response = requests.post(API_URL, json=input_data, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            predicted_category = result.get('predicted_category', 'N/A')
            
            st.success("✅ Prediction Complete!")
            st.markdown("### 🎯 Predicted Premium Category")
            
            # Display result in a prominent box
            st.info(f"**{predicted_category.upper()}**")
            
            # Display full response in expander
            with st.expander("📋 View Full Response"):
                st.json(result)
        else:
            st.error(f"❌ Error: API returned status code {response.status_code}")
            st.json(response.json() if response.content else "No error details available")
    
    except requests.exceptions.ConnectionError:
        st.error("❌ **Connection Error**: Could not connect to the API. Please make sure the FastAPI server is running on http://localhost:8000")
        st.info("💡 **Tip**: Run `uvicorn app:app --reload` in a separate terminal to start the API server.")
    
    except requests.exceptions.Timeout:
        st.error("❌ **Timeout**: The request took too long to complete.")
    
    except Exception as e:
        st.error(f"❌ **Error**: {str(e)}")
        st.exception(e)

# Footer
st.markdown("---")
st.markdown("💡 **Note**: Make sure the FastAPI backend is running before making predictions.")