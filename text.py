import streamlit as st
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set up the Streamlit app
st.title("Image Text Extraction with Streamlit")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Check if an image is uploaded
if uploaded_file is not None:
    # Open the image with PIL
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text using Tesseract OCR
    st.write("Extracting text from image...")
    text = pytesseract.image_to_string(image)
    
    # Display extracted text
    st.write("Extracted Text:")
    st.write(text)

    # Option to download the extracted text
    st.download_button(
        label="Download Extracted Text",
        data=text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
