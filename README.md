Fuzzy Logic Based Washing Machine Controller (Streamlit App)

##Project Overview
This project implements a Fuzzy Logic Controller (FLC) for a washing machine that automatically determines the wash speed based on two input parameters:
-->Weight of clothes
-->Dirtiness level
The system mimics human decision-making using fuzzy logic instead of strict numerical thresholds.
An interactive Streamlit web interface is provided to visualize inputs, fuzzy values, and the final wash speed.

##Objectives
To design a Mamdani-type fuzzy logic controller
To model real-life washing decisions using fuzzy rules
To compute wash speed using centroid defuzzification
To provide an interactive UI using Streamlit

##Fuzzy Logic Design
Input Variables
| Variable      | Range   | Linguistic Terms     |
| ------------- | ------- | -------------------- |
| Weight (kg)   | 0 – 10  | Light, Medium, Heavy |
| Dirtiness (%) | 0 – 100 | Low, Medium, High    |

-->Output Variable
| Variable   | Range   | Linguistic Terms   |
| ---------- | ------- | ------------------ |
| Wash Speed | 0 – 100 | Slow, Normal, Fast |

##Methodology

1.Fuzzification
Crisp inputs are converted into fuzzy values using triangular membership functions
2. Rule Base
IF–THEN rules define the relationship between inputs and output
Example:
IF Weight is Heavy AND Dirtiness is High THEN Wash Speed is Fast
3. Inference Mechanism
Mamdani inference method
AND → min operator
OR → max operator
4.Defuzzification
Centroid (Center of Area) method
Produces a single crisp wash speed value

##Streamlit User Interface Features

Slider to select weight of clothes
Slider to select dirtiness level
Button to compute wash speed
Display of:
Fuzzy membership values
Rule activation strengths
Final wash speed
Output membership function graph

##How to Run the Project
1️ Clone or Download the Project
git clone <repository-url>
cd fuzzy-washing-machine
2️ Install Required Libraries
pip install streamlit numpy matplotlib
3 Run the Streamlit App
streamlit run app.py
4 Open Browser
http://localhost:8501

##Technologies Used
Python
NumPy
Matplotlib
Streamlit
Fuzzy Logic (Mamdani Model)

Result -- Actual Prototype
<img width="1916" height="968" alt="image" src="https://github.com/user-attachments/assets/db0f3c2c-1a9b-4eae-8262-2fbce2fa74db" />
<img width="1919" height="971" alt="image" src="https://github.com/user-attachments/assets/5374337a-4189-4e7a-ba06-48f83bff8a57" />
<img width="1885" height="743" alt="image" src="https://github.com/user-attachments/assets/e23a1552-fed1-484d-8414-0fda8ea48999" />
<img width="1918" height="869" alt="image" src="https://github.com/user-attachments/assets/c8c46451-fcb0-43b5-8200-5986fb7263aa" />
<img width="1919" height="739" alt="image" src="https://github.com/user-attachments/assets/9319c78e-a664-456a-b18c-87f1a89a070c" />
<img width="1919" height="873" alt="image" src="https://github.com/user-attachments/assets/3337cf4f-bc4b-4c00-8e54-b89c0a8b46d0" />





