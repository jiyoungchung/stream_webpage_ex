import streamlit as st
from googletrans import Translator

# 번역 함수
# pip install --upgrade googletrans==4.0.0-rc1

def translate_text(text, src_language, trg_language):
    """
    :param target_language: 대상 언어 코드 ('en' for English, 'ko' for Korean, 'zh-CN' for Simplified Chinese 등)
    """
    translator = Translator()
    translated = translator.translate(text, src=src_language, dest=trg_language)
    return translated.text


# language dict
languages = {"영어":"en", "한국어":"ko", "중국어":"zh-CN"}

# 페이지 기본 설명
st.set_page_config( 
    page_icon='📢',                         # 이모티콘 넣을 수 있는 곳
    page_title='번역 서비스 웹 페이지',  # 페이지 제목
    layout='wide'                            # 페이지를 넓은 화면으로 보기
)
st.title("🙄 번역 서비스")
text = st.text_area("번역할 텍스트를 입력하세요", "")
src_language = st.selectbox("원본 언어", ["영어","한국어","중국어"], index=1)
trg_language = st.selectbox("목표 언어", ["영어","한국어","중국어"], index=0)  # default는 1로 지정

if st.button("번역"):
    src_lang = languages[src_language]
    trg_lang = languages[trg_language]
    translated_text = translate_text(text, src_language=src_lang, trg_language=trg_lang)
    st.success(translated_text)

    print(translate_text("안녕하세요", src_language=src_lang, trg_language=trg_lang))
