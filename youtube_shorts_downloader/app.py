import streamlit as st
import tempfile
import io
import pandas as pd
from youtube_shorts_downloader import main_dir
from youtube_shorts_downloader.transcripts import get_batch_transcripts
from youtube_shorts_downloader.input_output import parse_input_file, save_output

st.title("Youtube Transcript Downloader")
st.paragraph(
    "instructions: upload a text file with valid youtube urls, one per line, to fetch transcripts"
)


with st.container(border=True):
    col1, col2 = st.columns([3, 3])

    with col1:
        uploaded_file = st.file_uploader("Choose a File", type=["text"])
        col3 = st.container()
        with col3:
            trans_button_val = st.button(label="fetch transcripts", type="primary")

a, col0, b = st.columns([1, 20, 1])
colo1, colo2 = st.columns([3, 3])


@st.cache_data
def convert_df(df: pd.DataFrame) -> "csv":
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


def button_logic(temp_input_location: str):
    temp_output_location = temp_input_location.replace("txt", "csv")

    if trans_button_val:
        youtube_urls = parse_input_file(temp_input_location)
        batch_transcripts = get_batch_transcripts(youtube_urls)
        df = pd.DataFrame(batch_transcripts)
        converted_dv = convert_df(df)
        
        st.download_button(
            label="Download data as CSV",
            data=converted_dv,
            file_name=temp_output_location.split("/")[-1],
            mime="text/csv",
        )


@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="large_df.csv",
    mime="text/csv",
)



default_file = main_dir + "/data/input/test_input.txt"
if uploaded_file is not None:
    byte_file = io.BytesIO(uploaded_file.read())
else:
    filename = open(default_file, "rb")
    byte_file = io.BytesIO(filename.read())

with tempfile.TemporaryDirectory() as tmpdirname:
    temporary_video_location = tmpdirname + "/" + "input.txt"
    with open(temporary_video_location, "wb") as out:
        out.write(byte_file.read())
        button_logic(temporary_video_location, model_selection, bleep_words_list)
        out.close()
