import streamlit as st
from googletrans import Translator
import time

st.set_page_config(
    page_title="Kamada Cool App Series ver1",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("Pythonで翻訳アプリを作ってみたよ")
st.caption("Create by Kamada!")

st.markdown("""
            - サイドバーから言語選択。
            - 翻訳したい言語(単語、文章等)を入力。※５００文字以内
            - [翻訳するよ～]ボタンを教して翻訳実行！
            """)


# sideber1:翻訳したい言語設定
add_selectbox1 = st.sidebar.selectbox(
    '翻訳したい言語は?',
    ('日本語', '英語', 'ドイツ語','フランス語','イタリア語')
)
st.sidebar.write(f'設定値は {add_selectbox1} です')
select1 = add_selectbox1

language_dict = {
    '日本語':'ja',
    '英語':'en',
    'ドイツ語':'de',
    'フランス語':'fr',
    'イタリア語':'it'
}

# sideber2:翻訳する言語設定
add_selectbox2 = st.sidebar.selectbox(
    '何語に翻訳する?',
    ('英語', '日本語','ドイツ語','フランス語','イタリア語')
)
st.sidebar.write(f'設定値は {add_selectbox2} です')
select2 = add_selectbox2

translate_dict = {
    '日本語':'ja',
    '英語':'en',
    'ドイツ語':'de',
    'フランス語':'fr',
    'イタリア語':'it'
}

#def kamada():
#    if button == True:
#        tr.translate(text_language, src=language_dict[select1], dest=translate_dict[select2]).text
#        return kamada

# 画面分割用
col1, col2 = st.columns(2)
with col1:
    # インスタンス化
    tr = Translator()
    text_language = st.text_area('翻訳する単語、言葉を入力してちょ',max_chars=500,height=300)
    button = st.button("翻訳するよ～")
with col2:
    if button:
        with st.spinner('頑張ってググってます...'):
            time.sleep(3)
        result = tr.translate(text_language, src=language_dict[select1], dest=translate_dict[select2]).text
        st.text_area('翻訳したよ～',result,height=300)
        st.success('( ´ー｀)ﾌｩｰ．．．やってやったぜ')
    
    
    