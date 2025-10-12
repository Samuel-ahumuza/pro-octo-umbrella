import pychromecast
chromecast, browser = pychromecast.get_listed_chromecasts("")
import time
cast = chromecast[0]
cast.wait()
mediaController = cast.media_
import logging

# Set up logging for pychromecast (optional but helpful)
logging.basicConfig(level=logging.INFO)

# Discover Chromecasts on the network
# This can take a few seconds
chromecasts = pychromecast.get_chromecasts()

if chromecasts:
    # Assuming your Chromecast is named "Living Room"
    cast = next((cc for cc in chromecasts if cc.device.friendly_name == "Living Room"), None)

    if cast:
        # Wait for the cast device to be ready
        cast.wait()
        
        # Get the media controller object
        mc = cast.media_controller

        # Play a media file from a URL
        media_url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
        mc.play_media(media_url, 'video/mp4')

        print(f"Casting to {cast.device.friendly_name}...")

        # Wait until the media starts playing (or block until it finishes)
        mc.block_until_active() 

    else:
        print("Chromecast 'Living Room' not found.")
else:
    print("No Chromecasts found.")