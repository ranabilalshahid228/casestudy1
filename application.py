import streamlit as st
from main import predict
import pandas as pd

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
    <div style="text-align: center; margin-top: 5px;">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDQaB3z7wmDwQmROUxci8vNh8_jrPNTrkgHAS2Yx3c5Q&s" alt="Logo" style="width: 300px; margin-bottom: 5px;">
    </div>""", unsafe_allow_html=True
)





# st.image("7.jpeg", width=300)
# Setup the layout
st.markdown("<h1 style='color: black;'>Garment Production Prediction CaseStudy</h1>", unsafe_allow_html=True)



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
    st.write(f'Predicted Total Production for Selected Department and at selected Workers: {prediction}')

    st.write(f"background-color: #09ab3b Actual Productivity Prediction: :blue[{prediction}]")
    st.markdown(
    """
    <span style="background-color: #09ab3b">R-squared (Train): 0.9135524926797545 and Normalized MSE:0.0036</span>
    """,
    unsafe_allow_html=True
)
# Display a caption in Streamlit
st.caption("R-squared (Train): 0.9135524926797545 and Normalized MSE:0.0036")

# Custom CSS to position and style images

st.markdown(
    """
    <div style="text-align: left; margin-bottom: 20px;">
    <img src="https://i.pinimg.com/736x/d1/64/42/d16442754c442cc9d22d40f5c529bba7.jpg"style="width: 600px; margin-bottom: 5px;">
    </div>""", unsafe_allow_html=True
)
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 20px;">
    <img src=" https://i.pinimg.com/736x/06/de/62/06de624722bcde1117f99d65d5530f43.jpg"style="width: 300px; margin-bottom: 5px;">
    </div>""", unsafe_allow_html=True
)
