# addon.py

import xbmc
import xbmcaddon
import subprocess

# Get the addon instance
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# Define the Netflix URL
NETFLIX_URL = 'https://www.netflix.com'

def open_netflix():
    # Open the URL in the default web browser using flatpak-spawn
    try:
        subprocess.run(['flatpak-spawn', '--host', 'xdg-open', NETFLIX_URL], check=True)
        xbmc.executebuiltin('Notification(Netflix, Opening in default browser, 5000)')
    except Exception as e:
        xbmc.log(f"Error opening Netflix: {str(e)}", xbmc.LOGERROR)
        xbmc.executebuiltin('Notification(Netflix, Failed to open browser, 5000)')

# Entry point
if __name__ == '__main__':
    open_netflix()

