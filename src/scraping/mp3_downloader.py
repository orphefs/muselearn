from pathlib import Path
import json
import requests
import re
import os
import ast
from scrapy.utils.url import urlparse
from muselearn.src.utils.parsers import input_file_path, output_file_path
from muselearn.definitions import ROOT_DIR


def get_json(youtube_video_link: str) -> Path:
    path_to_json = output_file_path(directory=os.path.join(ROOT_DIR, 'data', 'music'),
                                    file_name=re.match('.*=(?P<video_id>\w*)$', youtube_video_link).group(
                                        'video_id') + '.json',
                                    mode='overwrite')

    url_to_json = 'http://www.youtubeinmp3.com/fetch/?format=JSON&video=' + youtube_video_link

    r = requests.get(url_to_json)
    json_dict = ast.literal_eval(r.content.decode('utf-8'))

    with path_to_json.open(mode='w') as outfile:
        outfile.write(json.dumps(json_dict, indent=2))

    return path_to_json


def get_mp3(path_to_json: Path) -> Path:
    with path_to_json.open(mode='r') as outfile:
        json_content = json.loads(outfile.read())

    url_to_mp3 = json_content['link'].replace("\\", "")
    file_name = json_content['title'].replace(" ", "_")

    path_to_mp3 = output_file_path(directory=os.path.join(ROOT_DIR, 'data', 'music'),
                                   file_name=file_name + '.mp3',
                                   mode='protected')

    response = requests.get(url_to_mp3)

    byte_array = bytearray(response.content)

    with path_to_mp3.open(mode='wb') as outfile:
        outfile.write(byte_array)

    return path_to_mp3


def download_mp3_from_youtube_link(youtube_video_link: str):
    path_to_json = get_json(youtube_video_link)

    try:
        path_to_mp3 = get_mp3(path_to_json)
    except FileExistsError as err:
        print('mp3 file already exists: {}'.format(err))

    return path_to_mp3


if __name__ == '__main__':
    path_to_mp3 = download_mp3_from_youtube_link('https://www.youtube.com/watch?v=i62Zjga8JOM')
    print(path_to_mp3)
