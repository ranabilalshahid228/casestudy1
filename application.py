import streamlit as st
from main import predict
import pandas as pd

# Function to add background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://miro.medium.com/v2/resize:fit:1160/1*8wCivXvVBBWy68X4Jb7dGQ.gif");
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
st.title('Garment Production Prediction by Bilal Rana')


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

    # Display the prediction
    st.write(f'Predicted Total Production: {prediction}')