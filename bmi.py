import streamlit as st
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="BMI Calculator", layout="wide")

st.title("BMI Calculator")

# 1. Inputs: Ask for Name, Age, Weight, Height
with st.sidebar:
    st.header("User Information")
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=2, max_value=120, value=25)
    gender = st.radio("Gender", ["Male", "Female"])

# Main layout columns
col_input, col_result = st.columns([1, 1])

with col_input:
    st.subheader("Metrics")
    height_cm = st.number_input("Height (cm)", min_value=50.0, value=170.0)
    weight_kg = st.number_input("Weight (kg)", min_value=10.0, value=70.0)
    
    calculate = st.button("Calculate")

# 2. Logic and Output
if calculate and name:
    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m ** 2), 1)
    
    # Determine Category
    if bmi < 18.5:
        category, color = "Underweight", "blue"
    elif 18.5 <= bmi < 25:
        category, color = "Normal", "green"
    elif 25 <= bmi < 30:
        category, color = "Overweight", "yellow"
    else:
        category, color = "Obese", "red"

    with col_result:
        st.subheader("Result")
        # Personal greeting as requested
        st.info(f"{name}, your age is {age}. With a weight of {weight_kg}kg and height of {height_cm}cm:")
        
        # 3. Create the Gauge Chart (Exactly like the image)
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = bmi,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': f"BMI = {bmi} ({category})", 'font': {'size': 24, 'color': color}},
            gauge = {
                'axis': {'range': [10, 40], 'tickwidth': 1},
                'bar': {'color': "black"}, # The needle/bar
                'steps': [
                    {'range': [10, 18.5], 'color': "cyan"},
                    {'range': [18.5, 25], 'color': "green"},
                    {'range': [25, 30], 'color': "yellow"},
                    {'range': [30, 40], 'color': "red"}
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': bmi
                }
            }
        ))
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

elif calculate and not name:
    st.error("Please enter your name in the sidebar first!")