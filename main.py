from datetime import datetime
import datetime
import pandas as pd
import requests



TOKEN = "BQBxd5T9i5aKnrfoicV9Q0obDeyHFOsr4-IBBCrSj-dAFvs9_T7B7eMPmYdsCQeXi5FmDQXXzRO54TSX0Al8ImptQAZQqMRRZ4wncZpbSHUVjch9Hj7eyZM6YnlQCipN4K9HiraZpgKqpRY_zA0dodeF40VzYz1bNBe7VXVu7VwwajdtylUwhLCCNqAGwKGI85pvyaT_9ESkKbipvAJ86L-Hhouu617BQ26rPgHX90xNMJC4ag9MCVswdGIuB3kArYhJlJGYcWG_7eEFPMvvooOxIQ"


if __name__ == "__main__":

    headers = {
        "Accept": "application/json",
        "Constent-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 100

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after{time}.".format(time=yesterday_unix_timestamp), headers=headers)

    data = r.json()

    songs = []
    artists = []
    played_at = []
    timestamps = []

    for song in data["items"]:
        songs.append(song["track"]["name"])
        artists.append(song["track"]["album"]["artists"][0]["name"])
        played_at.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    songs_dict = {
        "song": songs,
        "artist": artists,
        "Played_at": played_at,
        "Timestamp": timestamps
    }

    songs_df = pd.DataFrame(songs_dict)
    print(songs_df)