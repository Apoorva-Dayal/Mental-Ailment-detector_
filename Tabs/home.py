"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Mental-Ailment Detection by AAP")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
        """<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
Mental ailments, also referred to as mental health disorders or psychiatric illnesses, encompass a diverse range of conditions that affect an individual's cognitive, emotional, and behavioral functioning. These disorders can manifest in various ways, from mood disturbances and irrational fears to disruptions in perception and impaired social interactions.

**Types of Mental Ailments:**
1. **Mood Disorders**: These include conditions like depression and bipolar disorder, characterized by persistent feelings of sadness, hopelessness, or extreme mood swings.
2. **Anxiety Disorders**: Anxiety disorders, such as generalized anxiety disorder (GAD), panic disorder, and phobias, involve excessive worry, fear, or apprehension that can interfere with daily life.
3. **Psychotic Disorders**: Psychotic disorders, like schizophrenia, involve disruptions in thinking, perception, and behavior, often leading to hallucinations, delusions, and disorganized thoughts.
4. **Personality Disorders**: Conditions like borderline personality disorder (BPD) or antisocial personality disorder (ASPD) involve maladaptive patterns of behavior, cognition, and interpersonal relationships.
5. **Eating Disorders**: Eating disorders, such as anorexia nervosa, bulimia nervosa, and binge-eating disorder, involve disturbances in eating behaviors and body image.
6. **Substance Use Disorders**: These disorders involve problematic patterns of substance use, leading to significant impairment or distress. <br><br>

<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
Summary : Mental ailments are complex conditions that require comprehensive evaluation, compassionate care, and ongoing support. By promoting awareness, challenging stigma, and advocating for accessible mental health services, we can work towards creating a more inclusive and supportive society for all individuals affected by mental illness.
        </p>
    """, unsafe_allow_html=True)
