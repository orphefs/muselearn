from muselearn.definitions import ROOT_DIR
import os
from apiclient.discovery import build  # pip install google-api-python-client
from apiclient.errors import HttpError  # pip install google-api-python-client
from oauth2client.tools import argparser  # pip install oauth2client
import pandas as pd  # pip install pandas

with open(os.path.join(ROOT_DIR, 'config', '_developer.key')) as infile:
    developer_key = infile.readline()

DEVELOPER_KEY = developer_key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

argparser.add_argument("--q", help="Search term", default="Pink")
argparser.add_argument("--max-results", help="Max results", default=25)
args = argparser.parse_args()
options = args

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# Call the search.list method to retrieve results matching the specified
# query term.
search_response = youtube.search().list(
    q=options.q,
    videoCategoryId='10',
    type="video",
    part="id,snippet",
    maxResults=options.max_results
).execute()
videos = {}

# Add each result to the appropriate list, and then display the lists of
# matching videos.
# Filter out channels, and playlists.
for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
        # videos.append("%s" % (search_result["id"]["videoId"]))
        videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]

# print "Videos:\n", "\n".join(videos), "\n"
s = ','.join(videos.keys())

videos_list_response = youtube.videos().list(
    id=s,
    part='id,statistics'
).execute()
res = []
for i in videos_list_response['items']:
    temp_res = dict(v_id=i['id'], v_title=videos[i['id']])
    temp_res.update(i['statistics'])
    res.append(temp_res)

df = pd.DataFrame.from_dict(res)
print(df.head())
