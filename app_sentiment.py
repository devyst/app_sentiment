import streamlit as st
from textblob import TextBlob
from googletrans import Translator

def translate_text(text, dest_lang='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity, analysis.sentiment.subjectivity

def highlight_sentiment(text):
    analysis = TextBlob(text)
    sentences = analysis.sentences
    highlighted_text = ""

    for sentence in sentences:
        sentiment, _ = analyze_sentiment(str(sentence))
        if sentiment > 0:
            highlighted_text += f'<span style="color:green">{sentence}</span> '
        elif sentiment < 0:
            highlighted_text += f'<span style="color:red">{sentence}</span> '
        else:
            highlighted_text += f'<span style="color:gray">{sentence}</span> '
    return highlighted_text

def main():
    st.title("Aplikasi Analisis Sentimen Multibahasa")

    st.write("Masukkan caption untuk menganalisis sentimen:")

    user_input = st.text_area("Caption:", "")

    if st.button("Analisis Sentimen"):
        if user_input:
            translated_text = translate_text(user_input)
            overall_sentiment, _ = analyze_sentiment(translated_text)

            if overall_sentiment > 0:
                st.markdown('<h3 style="color:green; font-weight:bold">Sentimen: Positif</h3>', unsafe_allow_html=True)
            elif overall_sentiment < 0:
                st.markdown('<h3 style="color:red; font-weight:bold">Sentimen: Negatif</h3>', unsafe_allow_html=True)
            else:
                st.markdown('<h3 style="color:black; font-weight:bold">Sentimen: Netral</h3>', unsafe_allow_html=True)

            highlighted_text = highlight_sentiment(translated_text)
            st.markdown("Translation in English:")
            st.markdown(highlighted_text, unsafe_allow_html=True)
        else:
            st.write("Mohon masukkan caption terlebih dahulu.")

if __name__ == "__main__":
    main()
