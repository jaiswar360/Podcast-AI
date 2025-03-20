import streamlit as st

# Page config
st.set_page_config(
    page_title="PodcastAI 1",
    page_icon="📚",
)

st.title("Welcome to PodcastAI Notes 🎧")
st.write("**MSC IT Notes, Now in Podcast Form!**")
st.write(
    "Our platform offers easy-to-understand podcasts based on MSC IT subject notes. Whether you're studying or revising , listen anytime, anywhere, and make learning more convenient and accessible."
)

st.title("Data Science")
with st.container():
    # Path to your Audio file
    audio_path = (
        r"E:\Data Analysis\Projects\PodcastAI_Notes\podAi\audio_files\Data Science.wav"
    )

    # Read as bytes
    with open(audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()

    # Streamlit audio player
    st.audio(audio_bytes, format="audio/wav")

    # Path to your PDF file
    pdf_file_path = (
        r"E:\Data Analysis\Projects\PodcastAI_Notes\podAi\audio_files\DS Q&A.pdf"
    )

    # Open and read the PDF file as bytes
    with open(pdf_file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    # Display download button
    st.download_button(
        label="📥 Download DS PDF Notes",
        data=PDFbyte,
        file_name="DS Q&A.pdf",
        mime="application/pdf",
    )

st.title("Soft Computing Techniques")
with st.container():
    audio_path2 = r"E:/Data Analysis/Projects/PodcastAI_Notes/podAi/audio_files/Soft Computing Techniques.wav"

    with open(audio_path2, "rb") as audio_file:
        audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/wav")

    pdf_file_path2 = (
        r"E:\Data Analysis\Projects\PodcastAI_Notes\podAi\audio_files\SCT Q&A.pdf"
    )

    with open(pdf_file_path2, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📥 Download SCT PDF Notes",
        data=PDFbyte,
        file_name="SCT Q&A.pdf",
        mime="application/pdf",
    )


st.title("Cloud Computing")
with st.container():
    audio_path3 = r"E:/Data Analysis/Projects/PodcastAI_Notes/podAi/audio_files/Cloud Computing.wav"

    with open(audio_path3, "rb") as audio_file:
        audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/wav")

    pdf_file_path3 = (
        r"E:\Data Analysis\Projects\PodcastAI_Notes\podAi\audio_files\CC Q&A.pdf"
    )

    with open(pdf_file_path3, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📥 Download CC PDF Notes",
        data=PDFbyte,
        file_name="CC Q&A.pdf",
        mime="application/pdf",
    )


st.title("Research Methodology")
with st.container():
    audio_path4 = r"E:/Data Analysis/Projects/PodcastAI_Notes/podAi/audio_files/Research Methodology.wav"

    with open(audio_path4, "rb") as audio_file:
        audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/wav")

    pdf_file_path4 = (
        r"E:\Data Analysis\Projects\PodcastAI_Notes\podAi\audio_files\RM Q&A.pdf"
    )

    with open(pdf_file_path4, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📥 Download RM PDF Notes",
        data=PDFbyte,
        file_name="RM Q&A.pdf",
        mime="application/pdf",
    )
