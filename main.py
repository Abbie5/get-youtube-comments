# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery
import pprint
import sys
import json

pp = pprint.PrettyPrinter(indent=4)
pp2 = pprint.PrettyPrinter(indent=4, depth=2)
pp1 = pprint.PrettyPrinter(depth=1)


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    

    api_service_name = "youtube"
    api_version = "v3"
    with open("key.json", "r") as f:
        DEVELOPER_KEY = json.load(f)["developer_key"]

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    input = sys.argv[1]
    # get video id using yt search
    request = youtube.search().list(
        part="snippet",
        q=input,
    )
    response = request.execute()
    video_id = response["items"][0]["id"]["videoId"]

    with open(f"responses_{video_id}.html", "w", encoding="utf-8") as f:
        next_page_token = ""
        while True:
            request = youtube.commentThreads().list(
                part="snippet",
                # videoId=input("Enter video id: ")
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token,
            )
            response = request.execute()

            # pp1.pprint(response)

            next_page_token = (
                response["nextPageToken"] if "nextPageToken" in response else False
            )
            # print(num_results)

            f.write("<ul>")
            for item in response["items"]:
                f.write(
                    f"<li>{item['snippet']['topLevelComment']['snippet']['textDisplay']}</li>"
                )
            f.write("</ul>")

            if not next_page_token:
                break

        f.close()


if __name__ == "__main__":
    main()
