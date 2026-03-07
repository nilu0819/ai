import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open(r"C:\Users\niles\spider\elctric bill analysis.py", 'rb'))

# Set the title of the Streamlit app
st.title("Bill Prediction App")

# Add a brief description
st.write("This app predicts the Monthely Comjumption of Bill using a simple linear regression model.")

# Add input widget for user to enter years of experience
Monthely_Bill = st.number_input("Enter Month of Comjumption:", min_value=0.0, max_value=5000.0, value=500.0, step=0.5)

# When the button is clicked, make predictions
if st.button("Predict Bill"):
    # Make a prediction using the trained model
    Comjumption_input = np.array([[Monthely_Bill]])  # Convert the input to a 2D array for prediction
    prediction = model.predict(Comjumption_input)
    
    # Display the result
    st.success(f"The predicted Bill for {Monthely_Bill} years of Comjumption is: ${prediction[0]:,.2f}")
    
# Display information about the model
st.write("The model was trained using a dataset of Comjumption of Bill.")