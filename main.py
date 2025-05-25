import streamlit as st
from image_analysis import analyze_image_azure         
from description_improvment import improve_description_with_llm     
from question_answering import answer_user_question             
from faq_loader import faq                           

def main():
    """
    Runs the main Streamlit web application for image analysis and user interacton.

    This function defines the user interface and main logic of the image description assistant.
    It allows the user to upload an image, which is then sent to the Azure Computer Vision API
    for analysis. The results include a description and a set of tags. These are further refined
    using a language model to generate a longer description.

    The application also provides a text input where users can assk questions related to the 
    image or a predefined FAQ. Depending on the question, the system will:
        - respond using the FAQ if a close match is found.
        - use the LLM to answer if the question is image-related.
        - fall back to a general assistant reply if unrelated to both.

    The function handles errors gracefully and provides user feedback through the Streamlit interface.
    """

    st.title("Image Description Assistant")

    uploaded_file = st.file_uploader("Upload an image for analysis", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image_bytes = uploaded_file.read()
        try:
            description, tags = analyze_image_azure(image_bytes)
            st.markdown("### Image Description (Azure):")
            st.write(description)

            st.markdown("### Tags and Confidence:")
            for tag in tags:
                st.write(f"- {tag['name']} (confidence: {tag['confidence']:.2f})")

            improved_description = improve_description_with_llm(description, tags)
            st.markdown("### Enhanced Description from LLM:")
            st.write(improved_description)

            st.markdown("---")
            user_question = st.text_input("Ask a question about the FAQ or image analysis:")

            if user_question:
                answer = answer_user_question(user_question, faq, improved_description, tags)
                st.markdown("### Answer:")
                st.write(answer)

        except Exception as e:
            st.error(f"Error during image analysis: {e}")
    else:
        st.info("Please upload an image to begin analysis.")

if __name__ == "__main__":
    main()