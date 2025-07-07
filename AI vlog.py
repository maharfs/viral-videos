python
import streamlit as st
from datetime import datetime, timedelta
from googleapiclient.discovery import build

API_KEY ="AIzaSyCIYqDE9Zn8Q9pUg_2hSampeRzPINn_FjQ"
youtube = build("youtube", "v3", developerKey=API_KEY)

keywords = [
    "Mukbang vlog",
    "Mukbang challenge",
    "Mukbang fails",
    "Mukbang animation",
    "Mukbang parody",
    "Mukbang reaction",
    "Mukbang live stream"
]

st.title("Viral Mukbang Videos Search")

days = st.number_input("Enter number of days to search from today:", min_value=1, max_value=30, value=7)

#Fetch Data Button
if st.button("Fetch Data"):
    try:
        # Calculate date range
        start_date = (datetime.utcnow() - timedelta(days=int(days))).isoformat("T") + "Z"

        all_results = []

        # Iterate over the list of keywords
        for keyword in keywords:
            st.write(f"Searching for keyword: {keyword}")

            # Define search parameters
            search_params = {
                "part": "snippet",
                "q": keyword,
                "type": "video",
                "order": "viewCount","publishedAfter": start_date,
                "maxResults": 5
            }

            # Call the YouTube API
            response = youtube.search().list(**search_params).execute()

            for item in response["items"]:
                video_data = {
                    "title": item["snippet"]["title"],
                    "channel": item["snippet"]["channelTitle"],
                    "published_at": item["snippet"]["publishedAt"],
                    "video_id": item["id"]["videoId"]
                }
                all_results.append(video_data)

        # Show results
        st.subheader("Top Results:")
        for result in all_results:
            st.write(f"{result['title']}")
            st.write(f"Channel: {result['channel']}")
            st.write(f"Published: {result['published_at']}")
            st.video(f"https://www.youtube.com/watch?v={result['video_id']}")
            st.write("---")

    except Exception as e:
        st.error(f"Error occurred: {e}")
```
