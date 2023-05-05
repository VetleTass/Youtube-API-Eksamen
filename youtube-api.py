from googleapiclient.discovery import build
import requests
import re
import webbrowser
from pytube import YouTube
import os 

#denne koden finner linken til youtuben video din, den tar hensyn til hva du har spurt om å søke etter og bruker API-keyen til å finne det 
def søk_videoer(søk, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)

    #sender en request for youtube videoen gjennom API-en
    request = youtube.search().list(
        part="id",
        #finner video og ikke youtube short eller ett innlegg
        type="video",
        q=søk,
        maxResults=1,
    )
    response = request.execute()

    #sammensetter youtube linken slik at den kan printes ut som bare linken 
    video_sitt_ids = [item['id']['videoId'] for item in response['items']]
    video_sine_links = ["https://www.youtube.com/watch?v=" + video_id for video_id in video_sitt_ids]
    return video_sine_links

#input legg til det du vil søke etter
søk = input("hva vil du laste ned?: ")
api_key = "Legg til API-keyen din her"

#printer ut hele linken til youtube videon 
video_sine_links = søk_videoer(søk, api_key)
for video_link in video_sine_links:
    print (video_link)


vise_video = input("vil du se videoen? Skriv Y eller N: ")
if vise_video.lower == "y":
    print("her er den")
    webbrowser.open(video_link)
else:
    print("laster ned videoen nå")

def last_ned_video(video_link):
    yt = YouTube(video_link)#tar video linken og putter den inn i youtube 
    stream = yt.streams.get_highest_resolution()#laster ned den høyeste kvaliteten 
    directory = os.getcwd() #får det mest aktive filen å putte filmen i 
    stream.download(output_path=directory) 

print("videoen er lastet ned til:", os.getcwd())#sier hvor videoen er lasted ned til

