<a href="https://colab.research.google.com/github/jermwatt/youtube_transcript_downloader/blob/main/transcript_downloader_walkthrough.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Youtube Shorts Transcripts downloader

Download transcripts for Youtube Shorts by dragging and dropping a text file containing valid Youtube Shorts urls into a simple streamlit app.

This repo illustrates also illustrates how to pull transcripts step-by-step in the `transcript_downloader_walkthrough.ipynb` notebook.

## Install instructions

To get setup to run the notebook / bleep your own videos / run the strealit demo first install the requirements for this project by pasting the below in your terminal.

```python
pip install -r requirements.txt
```


## Instructions for using the streamlit app

Start the streamlit app

```python
python -m streamlit run youtube_shorts_downloader/app.py
```

You can now drag and drop `.txt` files containing Youtube Shorts urls - one url per line - into the app for batch transcript fetching.