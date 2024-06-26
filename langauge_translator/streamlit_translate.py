import streamlit as st
from translate import Translator

# List of common languages and their ISO 639-1 codes
LANGUAGES = {
    "Auto-detect": "autodetect",
    "English": "en",
    "Japanese": "ja",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Russian": "ru",
    "Korean": "ko",
    "Portuguese": "pt",
    "Italian": "it",
    "Arabic": "ar",
    "Hindi": "hi",
    "Bengali": "bn",
    "Urdu": "ur",
    "Punjabi": "pa",
}

def translate_text(text, source_language='auto', target_language='ja'):
    """
    Translates the provided text from the source language to the target language.

    Parameters:
    text (str): Text to be translated.
    source_language (str): Source language for translation (default is 'auto' for auto-detection).
    target_language (str): Target language for translation (default is 'ja' for Japanese).
    
    Returns:
    str: Translated text.
    """
    translator = Translator(from_lang=source_language, to_lang=target_language)
    return translator.translate(text)

def main():
    st.title("File and Text Translator")

    st.sidebar.write("## Translation Options")
    
    translation_type = st.sidebar.selectbox("Select Translation Type", options=["Translate Text", "Translate File"])

    if translation_type == "Translate Text":
        st.write("### Translate Text")
        source_language = st.sidebar.selectbox("Source Language", options=list(LANGUAGES.keys()), index=0)
        target_language = st.sidebar.selectbox("Target Language", options=list(LANGUAGES.keys()), index=2)
        
        source_language_code = LANGUAGES[source_language]
        target_language_code = LANGUAGES[target_language]

        text = st.text_area("Enter text to translate:")
        
        if st.button("Translate"):
            translated_text = translate_text(text, source_language_code, target_language_code)
            st.write("Translated Text:")
            st.write(translated_text)

    elif translation_type == "Translate File":
        st.write("### Translate File")
        source_language_file = st.sidebar.selectbox("Source Language", options=list(LANGUAGES.keys()), index=0)
        target_language_file = st.sidebar.selectbox("Target Language", options=list(LANGUAGES.keys()), index=2)
        
        source_language_code_file = LANGUAGES[source_language_file]
        target_language_code_file = LANGUAGES[target_language_file]

        st.write("Upload a text file to translate its contents.")
        uploaded_file = st.file_uploader("Choose a file", type="txt")
        
        if uploaded_file is not None:
            # To read file as string:
            text = uploaded_file.read().decode("utf-8")

            if st.button("Translate"):
                translated_text = translate_text(text, source_language_code_file, target_language_code_file)
                
                st.write("Translated Text:")
                st.write(translated_text)
                
                st.download_button(
                    label="Download Translated File",
                    data=translated_text,
                    file_name=f"translated_{uploaded_file.name}",
                    mime="text/plain"
                )

if __name__ == "__main__":
    main()

