This is a python sdk to manipulate the deezer's API

# installation

```bash
pip install deezersdk
```

# Authentication
You need to create a deezer's account.

And then you need to create an app on https://developers.deezer.com/myapps

We will need, your Application ID, Secret Key and the Redirect URL after authentication

```bash
deezersdk.Deezer(app_id=YOUR_APPLICATION_ID,
                 app_secret=YOUR_SECRET_KEY)
```
A pop up will open and we will be able to login to your deezer account.

You will then be redirected to the url you put in your app with an authorization code in your url.

With this code you can, request your access token 

You now have your access token, and can use the SDK.

# Use the sdk
## Instantiate the sdk
```bash
deezer = deezersdk.Deezer(app_id=DEEZER_APP_ID,
                          app_secret=DEEZER_APP_SECRET,
                          code=YOUR_URL_CODE,
                          token=YOUR_ACCESS_TOKEN)
```
## Query the API
### Get my playlists
```bash
deezer.get_my_playlists()
```
Will return an array of Playlist objects witch contain information like the title, and is_loved_track to True if it's 
your loved playlist

### Play a playlist with the plugins
```bash
playlists = deezer.get_my_playlists()
url = deezer.get_widget(playlist=playlists[0])
```
you can add the url in an iframe to display the plugin 
or you can open it directly with :  
```bash
import webbrowser
webbrowser.open(url)
```

### Get my favorites artists
### Play a Song
### Get author information
### Get albums information

 

