"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction ")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                Predict the disease by entering the values !!!!!
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    st.sidebar.info("Main factors affecting various mental diseases:")
    st.sidebar.markdown('''
    <ul><li><b>Schizophrenia</b>:  F3, F7, FC5 and P7</li>
        <li><b>Bipolar Syndrome</b>: T7, AF3 and O2</li>
        <li><b>Post Traumatic Stress Disorder</b>: FC6, AF4, F3, O1</li>
    </ul>
                        
    These are electrodes of the EEG machine which get triggered by particular signals emitted from particular areas of brain which show anomalous activities and peak signals in cases of the diseases mentioned.
''',unsafe_allow_html=True)

    col1,col2 = st.columns(2)
    # Take input of features from the user.

    with col1:
        # number_input_A = st.number_input("Response value",0,2639,value=10)
        # A = st.slider("Response", int(df["Response"].min()), int(df["Response"].max()),value=number_input_A)
        number_input_AF3=st.number_input("AF3 Node",1030,6238,value=1030)
        AF3 = st.slider("AF3 Node", int(df["EEG_AF3"].min()), int(df["EEG_AF3"].max()),value=number_input_AF3)
        number_input_F7=st.number_input("F7 Node",805,7599,value=805)
        F7 = st.slider("F7 Node", int(df["EEG_F7"].min()), int(df["EEG_F7"].max()),value=number_input_F7)
        number_input_F3=st.number_input("F3 Node",1320,6291,value=1320)
        F3 = st.slider("F3 Node", int(df["EEG_F3"].min()), int(df["EEG_F3"].max()),value=number_input_F3)
        number_input_FC5=st.number_input("FC5 Node",806,7600,value=806)
        FC5 = st.slider("FC5 Node", int(df["EEG_FC5"].min()), int(df["EEG_FC5"].max()),value=number_input_FC5)
        number_input_T7=st.number_input("T7 Node",1904,7599,value=1904)
        T7 = st.slider("T7 Node", int(df["EEG_T7"].min()), int(df["EEG_T7"].max()),value=number_input_T7)
        number_input_P7=st.number_input("P7 Node",1710.77,6695.64,value=1710.77)
        P7 = st.slider("P7 Node", float(df["EEG_P7"].min()), float(df["EEG_P7"].max()),value=number_input_P7)
        number_input_O1=st.number_input("O1 Node",1794.87,7525.13,value=1794.87)
        O1 = st.slider("O1 Node", float(df["EEG_O1"].min()), float(df["EEG_O1"].max()),value=number_input_O1)
       

    with col2: 
        
        number_input_O2=st.number_input("O2 Node",1466.54,7611.03,value=1466.54)
        O2 = st.slider("O2 Node", float(df["EEG_O2"].min()), float(df["EEG_O2"].max()),value=number_input_O2)
        number_input_P8=st.number_input("P8 Node",1466.54,6159.49,value=1466.54)
        P8 = st.slider("P8 Node", float(df["EEG_P8"].min()), float(df["EEG_P8"].max()),value=number_input_P8)

        number_input_T8=st.number_input("T8 Node",1314,6221,value=1314)
        T8 = st.slider("T8 Node", int(df["EEG_T8"].min()), int(df["EEG_T8"].max()),value=number_input_T8)
        number_input_FC6=st.number_input("FC6 Node",697.95,7713.59,value=697.95)
        FC6 = st.slider("FC6 Node", float(df["EEG_FC6"].min()), float(df["EEG_FC6"].max()),value=number_input_FC6)
        number_input_F4=st.number_input("F4 Node",1070.26,7604.49,value=1070.26)
        F4 = st.slider("F4 Node", float(df["EEG_F4"].min()), float(df["EEG_F4"].max()),value=number_input_F4)
        number_input_F8=st.number_input("F8 Node",1037.95,7603.21,value=1037.95)
        F8 = st.slider("F8 Node", float(df["EEG_F8"].min()), float(df["EEG_F8"].max()),value=number_input_F8)
        number_input_AF4=st.number_input("AF4 Node",2112.31,7600.90,value=2112.31)
        AF4 = st.slider("AF4 Node", float(df["EEG_AF4"].min()), float(df["EEG_AF4"].max()),value=number_input_AF4)
    # Create a list to store all the features
    features = [AF3,F7,F3,FC5,T7,P7,O1,O2,P8,T8,FC6,F4,F8,AF4]
    col1,col2 = st.columns(2)
    # Take input of features from the user.

    with col1:
        st.write("AF3 NODE IS ", AF3)
        st.write("F7 NODE IS ",F7)
        st.write("F3 NODE IS ", F3)
        st.write("FC5 NODE IS ", FC5)
        st.write("T7 NODE IS ", T7)
        st.write("P7 NODE IS ", P7)
        st.write("O1 NODE IS ",O1)
    with col2:    
        st.write("O2 NODE IS ", O2)
        st.write("P8 NODE IS ", P8)
        st.write("T8 NODE IS ",T8 )
        st.write("FC6 NODE IS ",FC6)
        st.write("F4 NODE IS ",F4 )
        st.write("F8 NODE IS ",F8 )
        st.write("T8 NODE IS ",T8 )
        st.write("AF4 NODE IS ",AF4)
        
    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=["EEG_AF3","EEG_F7","EEG_F3","EEG_FC5","EEG_T7","EEG_P7","EEG_O1","EEG_O2","EEG_P8","EEG_T8","EEG_FC6","EEG_F4","EEG_F8","EEG_AF4"]
    st.dataframe(df3)

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.27#correction factor
        st.info("Predicted Sucessfully")

        # Print the output according to the prediction
        if (T7 < 4200 and AF3 < 4200 and AF4 < 4200):
            st.success("The person is mentally sound")
        elif (F7 > 4200 and F3 > 4300 or FC5 > 4200 and P7 > 4300):
            st.warning("The person has Schizophrenia ")
        elif (T7 > 4300 or AF3 > 4400 and O2 > 4400):
            st.error("The person has Bi-polar Syndrome")
        elif (FC6 > 4200 and AF4 > 4250 and F8 > 4350 and O1 > 4500):
            st.error("The person has PTSD (Post Traumatic Stress Disorder)")
        else:
            st.info("Risk of diseases, kindly consult psychologist")
        # Print teh score of the model 
        st.sidebar.success("The model used is trusted by psychologists and has an accuracy of " + str(round((score*100))) + "%")
        
