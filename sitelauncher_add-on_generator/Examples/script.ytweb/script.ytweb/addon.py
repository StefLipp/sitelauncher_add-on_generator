# addon.py

import xbmc
import xbmcaddon
import subprocess

# Get the addon instance
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# Define the URL
YT_URL = 'https://www.youtube.com'

def open_url():
    # Open the URL in the default web browser using flatpak-spawn
    try:
        subprocess.run(['flatpak-spawn', '--host', 'xdg-open', YT_URL], check=True)
        xbmc.executebuiltin('Notification(YouTube, Opening in default browser, 5000)')
    except Exception as e:
        xbmc.log(f"Error opening YouTube: {str(e)}", xbmc.LOGERROR)
        xbmc.executebuiltin('Notification(Youtube, Failed to open browser, 5000)')

# Entry point
if __name__ == '__main__':
    open_url()

