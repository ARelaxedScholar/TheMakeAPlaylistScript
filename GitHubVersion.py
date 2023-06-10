import requests
import json
from Google import Create_Service


#USER DATA
youtubersUploadId = "UPLOAD_PLAYLIST_ID" #Find the channel ID of the youtuber and replace the UC with UU
userAPIKey = "YOUR_USER_API_KEY"
clientId = "YOUR_CLIENT_ID"
CLIENT_SECRET_FILE = "Path/To/Client/Secret.json"



#Google Stuff
API_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube"]



#Defining functions
##This function gets the playlist from the channel we want and spits them to a list
def getVideos(userAPIKey, uploadID):
    #Takes an user APIKEY and the id of the upload playlist of a youtuber
    #-> returns a list with all the metadata of all the videos posted by the youtuber.
    #
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    
    videoList = []

    #Adds each videoId to a list of video ids, to be used later when we make the add to playlist module.
    nextPageToken = None
    payload = {"part":"snippet", "playlistId":uploadID, "maxResults":50, "key":userAPIKey}
    result = requests.get(url, payload)
    resultJsonItems = result.json()['items']
    for video in resultJsonItems:
        videoList.append(video)
    
    while True:
        nextPageToken = result.json().get('nextPageToken')
        if nextPageToken is None:
            break
        payload = {"part":"snippet", "playlistId":uploadID, "maxResults":50, "pageToken":nextPageToken, "key":userAPIKey}
        result = requests.get(url, payload)
        resultJsonItems = result.json()['items']
        for video in resultJsonItems:
            videoList.append(video)
    return videoList

#We need a function which creates a playlist and one that adds the videos to the playlist and one for authentificationg
def createPlaylistAndPopulate(videos):
    #Authentificate
    service =  Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    #Now we create a playlist
    requestBody = {
        "snippet" : {
            "title" : "Just another playlist",
            "description":"A playlist created programmatically"
        }
    }
    service.playlists().insert(
        part = "snippet",
        body = requestBody
    ).execute()

    # Get the id of the newly created playlist
    response = service.playlists().list(
        part = "contentDetails",
        mine = True
    ).execute()

    playlists = response['items']
    playlistToModify = playlists[0]['id']

    #Now we populate the playlist
    for i, video in enumerate(videoList):
        requestBodyPlaylist = {
            "snippet" : {
                "playlistId" : playlistToModify,
                "resourceId" : {
                    "kind" : "youtube#video",
                    "videoId" : videoList[i]['snippet']['resourceId']['videoId']
                }
            }
        }
        service.playlistItems().insert(
            part = "snippet",
            body = requestBodyPlaylist
        ).execute()





videoList = getVideos(userAPIKey, youtubersUploadId)
print(videoList[0])
createPlaylistAndPopulate(videoList)
print("Your playlist is complete, enjoy!")