import streamlit as st
import io
import pandas as pd
from youtube_shorts_downloader import main_dir
from youtube_shorts_downloader.transcripts import get_batch_transcripts
from youtube_shorts_downloader.input_output import parse_input_file, save_output


st.title("YT Shorts Transcript Downloader")
st.markdown(
    "instructions: upload a text file with valid youtube urls, one per line, to fetch transcripts"
)


base = st.container(border=True)
with base:
    x, col1, col2 = st.columns([3, 20, 5])
    with col1:
        uploaded_file = st.file_uploader("Choose a File", type=["txt"])
        col2, col3, col4 = st.columns([3, 2, 3])
        with col2:
            trans_button_val = st.button(label="fetch transcripts", type="primary")
        with col3:
            empty_container = st.container()
        with col4:
            placeholder = st.empty()


@st.cache_data
def convert_df(df: pd.DataFrame) -> "csv":
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


def button_logic(youtube_short_urls: list) -> None:
    if trans_button_val:
        batch_transcripts = get_batch_transcripts(youtube_short_urls)
        df = pd.DataFrame(batch_transcripts)
        converted_dv = convert_df(df)

        with col4:
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
    if uploaded_file.type == "text/plain":
        from io import StringIO

        stringio = StringIO(uploaded_file.read().decode("utf-8"))
        for line in stringio:
            youtube_short_urls.append(line.strip())
    # else:
    #     youtube_short_urls = parse_input_file(default_file_path)

    with st.spinner(text="transcript pull in progress..."):
        button_logic(youtube_short_urls)
