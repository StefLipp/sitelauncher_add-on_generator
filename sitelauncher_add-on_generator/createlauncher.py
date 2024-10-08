#!/usr/bin/env python3

# Importing
import shutil
import os
import sys

# Setting working directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

print('Feel free to personalise the icon.png before configuring the add-on if need be.')

# Asking site address
while True:
    VAR_URL= str(input('What is the address of the site in format https://www.example.com?: '))
    if VAR_URL.startswith('https://'):
        break
    elif VAR_URL.startswith('http://'):
        break
    else:
        print("Invalid input. Please enter the address of the site in format https://www.example.com.: ")

# Asking the site name
SITE_NAME = str(input('What is the title of the site?: '))

#Asking operating system and wether they use Flatpak
while True:
    OPSYS = input("Do you use Kodi on Windows or Linux? (Windows/Linux): ")
    if OPSYS.lower() == "linux":
        while True:
            VFLATPAK = input("Do you use the Flatpak version of Kodi? (y/n): ")
            if VFLATPAK == "y":
                RUN_SCRIPT = ['flatpak-spawn', '--host', 'xdg-open', f'{VAR_URL}']
                break
            elif VFLATPAK == "n":
                RUN_SCRIPT = ['xdg-open', f'{VAR_URL}']
                break
            else:
                print("Invalid input. Please enter y/n: ")
        break
    elif OPSYS.lower() == "windows":
        RUN_SCRIPT = ['cmd', '/c', 'start', f'{VAR_URL}']
        break
    else:
        print("Invalid input. Please enter Linux/Windows: ")

# Declaring variables
ADDON_NAME = f"{SITE_NAME} Web Launcher"
ADDON_ID = f"script.{SITE_NAME}web"

# Creating py file
os.mkdir(f"{ADDON_ID}")
os.mkdir(f"{ADDON_ID}/{ADDON_ID}")
f = open(f"./{ADDON_ID}/{ADDON_ID}/addon.py", "w")
f.write(f"""
# imports
import xbmc
import xbmcaddon
import subprocess

# Get the addon instance
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# Define the URL
def open_link():
    # Open the URL in the default web browser using flatpak-spawn
    try:
        subprocess.run({RUN_SCRIPT}, check=True)
        xbmc.executebuiltin('Notification(example, Opening in default browser, 5000)')
    except Exception as e:
        xbmc.executebuiltin('Notification(example, Failed to open browser, 5000)')
# Entry point
if __name__ == '__main__':
    open_link()
""")
f.close()

# Creating XML file
f2 = open(f"./{ADDON_ID}/{ADDON_ID}/addon.xml", "w")
f2.write(f"""
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="{ADDON_ID}" name="{ADDON_NAME}" version="1.0.0" provider-name="StefLipp">
	<requires>
		<import addon="xbmc.python" version="3.0.0"/>
	</requires>
	<extension point="xbmc.python.script" library="addon.py">
		<provides>executable</provides>
	</extension>
	<extension point="xbmc.addon.metadata">
		<platform>all</platform>
		<summary lang="en">Launch link to {SITE_NAME} in browser</summary>
		<description lang="en">Launch link in default browser. </description>
		<license>GNU General Public License, v3</license>
		<language></language>
		<forum>none</forum>
		<source>none</source>
		<website>none</website>
		<email>none</email>
		<assets>
			<icon>icon.png</icon>
			<fanart>fanart.jpg</fanart>
			<screenshot>resources/screenshot-01.jpg</screenshot>
			<screenshot>resources/screenshot-02.jpg</screenshot>
			<screenshot>resources/screenshot-03.jpg</screenshot>
		</assets>
		<news>none</news>
	</extension>
</addon>
""")
f2.close()

# copy icons into folder and create ZIP
try:
    source = 'icon.png'
    destination = f"./{ADDON_ID}/{ADDON_ID}/icon.png"
    shutil.copyfile(source, destination, follow_symlinks=True)
except Exception:
    print('No icon.png provided, skipping step...')
    pass

shutil.make_archive(f"{ADDON_ID}_zipped/{ADDON_ID}", 'zip', f"{ADDON_ID}")

# Response
print('Site launcher script was created and zipped succesfully.')
print('You can now install the generated zip file as an add-on from within Kodi.')
