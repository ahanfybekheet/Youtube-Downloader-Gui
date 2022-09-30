#-------------------------------------------------------------------
# YouTube (Video/Playlist) Download.
# Author        : Ahmed Hanfy Bekheet && 
# Version       : 1.0
# Python Version: 3.9.10
# Date          : 3/7/2022
#-------------------------------------------------------------------



from pytube import Playlist
from pytube import YouTube
from pytube import Search
from prettytable import PrettyTable
import os
from googleapiclient.discovery import build


class Downloader():
    
    def download_video_mp4(self,url:str,quality:str):
        self.video = YouTube(url)
        self.video.streams.filter(res=quality,progressive=True).last().download(filename=f"{self.video.title}.mp4")

    def download_video_mp3(self,url:str):
        self.video = YouTube(url)
        self.video.streams.filter(type="audio").last().download(filename=f"{self.video.title}.mp3")

    def define_playlist(self,url:str):
        self.playlist = Playlist(url)

    def get_video_duration(self,url):
        return YouTube(url).length

    def is_valid_video(self,url):
        try: YouTube(url)
        except: return False
        return True

    def is_valid_playlist(self,url):
        try: len(Playlist(url).video_urls)
        except: return False
        return True

    def get_title(self,url):
        return YouTube(url).title



class ApiSearch():
    DEVELOPER_KEY = 'AIzaSyDiW59MiKr5_G4fNpq3uIAE7o-gcERRLAM'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    MAX_RESULTS = 12

    def search(self,query):
        youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION, developerKey=self.DEVELOPER_KEY)
        search_response = youtube.search().list(q=query,part='id,snippet',maxResults=self.MAX_RESULTS).execute()
        self.videos = []
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                self.videos.append(f"https://www.youtube.com/watch?v={search_result['id']['videoId']}")


