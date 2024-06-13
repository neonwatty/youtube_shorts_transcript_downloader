import pandas as pd


def parse_input_file(input_file_path: str) -> list:
    youtube_urls = []
    with open(input_file_path, 'r') as file:
        for line in file:
            youtube_urls.append(line.strip())
    return youtube_urls


def save_output(data: list,
                output_file_path: str) -> None:
    df = pd.DataFrame(data)
    df.to_csv(output_file_path, index=False)