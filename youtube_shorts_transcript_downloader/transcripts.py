import re
from typing import List, Dict
from youtube_transcript_api import YouTubeTranscriptApi


def is_valid_youtube_shorts_url(url: str) -> bool:
    if not isinstance(url, str):
        return False 
    pattern = r'^https://www\.youtube\.com/shorts/[A-Za-z0-9_-]{11}$'  # youtube vido ids are always 11 chars long
    return re.match(pattern, url) is not None


def get_single_transcript(youtube_url: str) -> dict:
    try:
        if is_valid_youtube_shorts_url(youtube_url):
            video_id = youtube_url.split("/")[-1]
            video_transcript = YouTubeTranscriptApi.get_transcript(video_id)
            entry = {}
            entry["youtube_url"] = youtube_url
            entry["video_id"] = video_id
            entry["transcript"] = video_transcript
            return entry
        else:
            print(f"FAILURE: youtube_url is not valid - {youtube_url}")
            return {}
    except Exception as e:
        print(
            f"FAILURE: transcript pull for youtube_url - {youtube_url} - failed with exception {e}"
        )
        return {}


def get_batch_transcripts(youtube_urls: List[str]) -> List[Dict]:
    valid_urls = []
    valid_vids = []
    for i, url in enumerate(youtube_urls):
        if is_valid_youtube_shorts_url(url):
            vid = url.split("/")[-1]
            valid_urls.append(url)
            valid_vids.append(vid)
    try:
        video_transcripts = YouTubeTranscriptApi.get_transcripts(
            valid_vids, languages=["en"]
        )[0]
            
        entries = []
        for i in range(len(valid_urls)):
            entry = {}
            entry["youtube_url"] = valid_urls[i]
            entry["video_id"] = valid_vids[i]
            entry["transcript"] = video_transcripts[valid_vids[i]]
            entries.append(entry)
        return entries
    except Exception as e:
        print(f"FAILURE: batch transcription fetch failed with exception {e}")
        return []
