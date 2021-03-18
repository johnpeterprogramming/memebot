import praw, os, wget
from datetime import date

today = date.today()

formatted_date = today.strftime("%d-%m-%Y")
download_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), formatted_date)


if formatted_date not in os.listdir(os.path.abspath(os.path.dirname(__file__))):
    os.mkdir(download_folder)

reddit = praw.Reddit(
    client_id="9v-IMWqAk3xvAQ",
    client_secret="RwXXDNHJqeI554JtmGa5gUkqMWk",
    user_agent="memegen by ToiletPaperMan",
    username="ToilerPaperMan",
    password='27johna04'
)

subreddits = [
    reddit.subreddit("memes"),
    reddit.subreddit("dankmemes"),
    reddit.subreddit("PewdiepieSubmissions")
]


for subreddit in subreddits:
    for submission in subreddit.hot(limit=20):
        url = str(submission.url)
        exists = False
        for i in os.listdir(download_folder):
            if submission.id in i: 
                exists = True

        if not exists:
            if url.endswith('png') or url.endswith('jpg') or url.endswith('bmp') or url.endswith('gif') or url.endswith('wav'):
                wget.download(url, download_folder + '/' + submission.id + '.' + url[-3:])

