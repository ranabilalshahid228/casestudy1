import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

# Load data
data = pd.read_csv('datagarment (2).csv')

# Placeholder for real-time data updates
placeholder = st.empty()

# Generate some example real-time data
for _ in range(100):
    # Simulate reading new data
    new_data = np.random.randn(1, data.shape[1])
    new_df = pd.DataFrame(new_data, columns=data.columns)
    data = pd.concat([data, new_df], ignore_index=True)
    
    # Plot the histogram of residuals
    residuals = data['Residuals']
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    
    ax[0].hist(residuals, bins=30, color='green', edgecolor='black')
    ax[0].set_title('Histogram of Residuals')
    ax[0].set_xlabel('Residuals')
    ax[0].set_ylabel('Frequency')

    # Q-Q plot
    sorted_residuals = np.sort(residuals)
    theoretical_quantiles = np.random.normal(0, 1, len(sorted_residuals))
    theoretical_quantiles.sort()
    ax[1].scatter(theoretical_quantiles, sorted_residuals, color='blue')
    ax[1].plot(theoretical_quantiles, theoretical_quantiles, color='red')
    ax[1].set_title('Q-Q Plot')
    ax[1].set_xlabel('Theoretical Quantiles')
    ax[1].set_ylabel('Ordered Values')

    # R-squared plot (assuming `True Values` and `Predicted Values` columns)
    true_values = data['True Values']
    predicted_values = data['Predicted Values']
    ax[2].scatter(true_values, predicted_values, color='green')
    ax[2].plot(true_values, true_values, color='red', linestyle='--')
    ax[2].set_title('R-squared Plot')
    ax[2].set_xlabel('True Values')
    ax[2].set_ylabel('Predicted Values')

    # Display the plots in the Streamlit app
    placeholder.pyplot(fig)

    # Pause to simulate real-time updates
    time.sleep(1)
