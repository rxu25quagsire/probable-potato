#To run: cd Downloads\cancercure
#To run: C:\Users\raymo\Downloads\cancercure>
#To run: streamlit run raymondxu.py

import streamlit as st
import webbrowser

st.set_page_config(page_title="Raymond Xu", page_icon=":panda_face:", layout="wide")

with st.container():
    st.title("Hey! My name is Raymond Xu :wave:")
    st.write("I am a rising college freshman interested in medicine, machine learning, and music!")
    st.write("This website is powered by Python")
    
    st.subheader("Medicine")
    st.write("""
    - As an **INSIGHT Scholar** (2023), I spent three weeks investigating access to care disparitie in the Pacific Northwest with the University of Washington.
    - As a **Hutchins Science Scholar** (2023-24), I spent eight weeks working at Sidney Kimmel Medical College characterizing three novel mitochondrial inhibitors for PDAC.I also presented my research at a school symposium.
    - In college, I hope to continue to research novel ways to address the complex challenge of cancer, both as a medical and social issue.
    """)
    file_path = r"C:\Users\raymo\Downloads\Team 3A TRREK presentation (1).pdf"

    with open(file_path, "rb") as file:
        st.download_button("Download Poster: Raymond's TRREK Presentation", file, file_name="Raymond's TRREK PRESENTATION.pdf")

    file_path2 = r"C:\Users\raymo\Downloads\Copy of Characterizing Mitochondrial Inhibitor Derivatives for Pancreatic Cancer.pptx (1).pdf"
    
    with open(file_path2, "rb") as file:
        st.download_button("Download Poster: Raymond's Mitochondrial Inhibitor Poster", file, file_name="Raymond's MITOCHONDRIAL INHIBITOR POSTER.pdf")

    
    st.subheader("Machine Learning / Computer Progamming")
    st.write("""
    - I was recently introduced to the machine learning through my Python Progamming class at school.
    - For my final project, I used KNN and Random Forest models to **recommend surgeries** to patients with colon cancer and **predicted the malignancy of breast cancer tumors** with a roughly 95% accuracy!
    - I hope to continue leveraging the power of computer progamming to tackle real-world problems in college and beyond.
    """)
    if st.button("Take a look at my Github project!"):
        webbrowser.open("https://github.com/rxu25quagsire/probable-potato/blob/main/Colon%20Cancer%20Surgery%20and%20Breast%20Cancer%20Scans.ipynb")

    
    st.subheader("Music")
    st.write("""
    - Since I was five, I have been formally learning piano. See a video of me performing below!
    - Over the years, piano has become one of my most meaningful activities, allowing me to perform everywhere from the stage of **Carnegie Hall** to the **Memorial Sloan Kettering Cancer Center** as an official volunteer musician.
    - I received my **ABRSM Diploma in Piano Performance** in 2023, and some of my recent awards include first prize at the Prima Volta Music Competition and first prize at the NY Young Virtuoso Competition.
    - In addition, I have played the oboe since the fifth grade, and enjoy performing in my school orchestra.
    """)
    pianolink = "https://youtu.be/lUxZ04aK8Sg"
    pianoid = "lUxZ04aK8Sg"
    thumbnaillink = f"https://img.youtube.com/vi/{pianoid}/hqdefault.jpg"
    st.markdown(f"[![Click here to watch me play piano!]({thumbnaillink})]({pianolink})")
    st.write("Click here to watch me play!")


with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/raymondrhxu@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 8px; margin: 5px 0; box-sizing: border-box;">
        <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 8px; margin: 5px 0; box-sizing: border-box;">
        <textarea name="message" placeholder="Your Message" required style="width: 100%; height: 100px; padding: 8px; margin: 5px 0; box-sizing: border-box;"></textarea>
        <button type="submit" style="padding: 8px 15px;">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

