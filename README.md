# TheMakeAPlaylistScript
Takes a youtube Playlist ID and add the videos of said playlist to your account one by one, until either done or you've ran out of quotas.
In a **really early state**, planning to add:

1. Update playlist function
2. User Interactions
3. Error handling

The rest will be added/or not on a "if I have time and want to" basis.

## Prerequisites
- Requests (Python Library) if you don't just : pip install requests
- Google Client Library :  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

The other requisites are your google console identifiants which you can obtain after creating a new project, simple is fairly simple;
and the Upload's playlist's ID of your youtuber of choice -- find their channel Id first, replace UC by UU.

## Limitations
Due to the Youtube Data V3 API having a 10K/day quota limit, and creating a playlist and inserting a video to it costs 50 credits everytime, you can only move about 19X videos per day. So there's a need to procceed in batches which current version can't really do, since there's no update playlist yet.



