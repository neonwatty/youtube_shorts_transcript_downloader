import streamlit as st
import pandas as pd
from youtube_shorts_transcript_downloader.transcripts import get_batch_transcripts

st.set_page_config(page_title="YT Shorts Transcript Downloader", layout="wide")
st.title("YT Shorts Transcript Downloader")
st.markdown(
    "instructions: enter in urls separated by commas or upload a text file with one url per line"
)


base = st.container(border=True)
with base:
    col1, sep_col, col2 = st.columns([5, 2, 5])
    
    with col1:
        text_urls = st.text_area("youtube shorts urls", value="", placeholder="enter urls separated by commas - for example: https://www.youtube.com/shorts/o7a9hx-Pqyo, https://www.youtube.com/shorts/xkAYLnIsfX4")
    
    with col2:
        uploaded_file = st.file_uploader("Choose a File", type=["txt"])
        
    col3, col4, col5 = st.columns([3, 2, 3])
    with col3:
        trans_button_val = st.button(label="fetch transcripts", type="primary")
    with col4:
        empty_container = st.container()
    with col5:
        placeholder = st.empty()
        
download_area = st.container()

# https://www.youtube.com/shorts/o7a9hx-Pqyo, https://www.youtube.com/shorts/xkAYLnIsfX4

@st.cache_data
def convert_df(df: pd.DataFrame) -> "csv":
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


def button_logic(youtube_short_urls: list) -> None:
    if trans_button_val:
        batch_transcripts = get_batch_transcripts(youtube_short_urls)
        df = pd.DataFrame(batch_transcripts)
        # st.dataframe(df)
        converted_dv = convert_df(df)

        with download_area:
            st.download_button(
                label="Download transcripts",
                data=converted_dv,
                file_name="output.csv",
                mime="text/csv",
                disabled=False,
                type="primary",
            )


# default_file_path = main_dir + "/data/input/test_input.txt"
youtube_short_urls = []
if uploaded_file is not None:
    if text_urls is not None:
        if len(text_urls.strip()) > 0:
            st.warning("you can enter urls manually or from file but not both", icon="⚠️")
            st.stop()
    
    print('INFO: A')
    if uploaded_file.type == "text/plain":
        from io import StringIO

        stringio = StringIO(uploaded_file.read().decode("utf-8"))
        for line in stringio:
            youtube_short_urls.append(line.strip())
    # else:
    #     youtube_short_urls = parse_input_file(default_file_path)

if text_urls is not None:
    if len(text_urls.strip()) > 0:
        if uploaded_file is not None:
            st.warning("you can enter urls manually or from file but not both", icon="⚠️")
            st.stop()
        
    try:
        text_urls_split = text_urls.split(",")
        text_urls_split = [v.strip() for v in text_urls_split]
        youtube_short_urls = text_urls_split
    except:
        st.warning("please check your manually entered urls", icon="⚠️") 
        st.stop()
    
    with st.spinner(text="transcript pull in progress..."):
        print(f"youtube_short_urls --> {youtube_short_urls}")
        button_logic(youtube_short_urls)
