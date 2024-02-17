import streamlit as st
import pandas as pd
from main import predict
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import boxcox

# Function to add background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.govexec.com/media/featured/wwt6.gif");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
    )

# Add the background image
add_bg_from_url()

st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDQaB3z7wmDwQmROUxci8vNh8_jrPNTrkgHAS2Yx3c5Q&s" alt="Logo" style="width: 300px; margin-bottom: 5px;">
    </div>""", unsafe_allow_html=True
)

# st.image("7.jpeg", width=300)
# Setup the layout
st.title('Garment Production Prediction CaseStudy')

# Input widgets for user input, they will appear on the main body, to the right of the images
department = st.selectbox('Department', options=['Gloves', 'T-Shirt', 'Sweatshirt'])
quarter = st.selectbox('Quarter', options=['Quarter1', 'Quarter2', 'Quarter3', 'Quarter4'])
no_of_workers = st.number_input('Number of Workers', min_value=25, max_value=100, value=25)
defects_day = st.number_input('Unproductive days per month', min_value=1, max_value=10, value=5)

# Predict button
if st.button('Predict'):
    # Prepare the input data in the format expected by your predict function
    input_data = {
        'department': [department],
        'quarter': [quarter],
        'no_of_workers': [no_of_workers],
        'defects_day': [defects_day],
    }
    input_df = pd.DataFrame(input_data)

    # Call the predict function
    prediction = predict(input_df)  # Ensure your predict function is compatible with this input format
    
    # Apply Box-Cox transformation to prediction if necessary
    # In this example, I'm assuming prediction is a single value, if it's an array, loop through it
    prediction_bc, _ = boxcox([prediction])

    # Display the transformed prediction
    st.write(f'Predicted Total Production (Box-Cox transformed): {prediction_bc}')

    # Calculate R^2 and MSE
    # Assuming you have ground truth values for comparison
    # Replace ground_truth with actual values
    ground_truth = [100]  # Example ground truth value
    r2 = r2_score(ground_truth, [prediction])
    mse = mean_squared_error(ground_truth, [prediction])
    
    st.write(f'R^2 Score: {r2}')
    st.write(f'Mean Squared Error: {mse}')
