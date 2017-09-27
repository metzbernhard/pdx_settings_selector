# PDX Settings Selector

Little Python Tool for PDX Games to quickly change between sets of settings, without having to manually (de)select DLCs,Mods or other settings. 

![Image](https://puu.sh/xK7pL/f8e232f56d.png "Selector")

# How to use:
  - Start the program using settings_selector.py (Python 3 needs to be installed, https://python.org) or
    using the settings_selector.exe (this should not need Python to be installed)
  - Set Path to the Paradox Documents Folder (default: Documents/Paradox Interactive)
  - Select a name for the current settings you use and click "Save Current Settings"
  - In the Selector you choose the settings you want and click Use (or delete if you don't need those settings)
  - The Play Section is optional, you can select your path to the "Steam\steamapps\common" Folder in the Steam-Directory and then start the game via "Play" after selecting your Settings, this will skip the launcher and start the game using the current settings. Alternatively you can start the game as usual via steam after selecting your settings.

Video-Introduction: https://www.youtube.com/watch?v=wZHHEEHBGk0

# Which Settings will be saved?
  - Resolution
  - Language
  - Fullscreen & Borderless
  - DLC-Selecton
  - Mod-Selection

# Other Information
  - You can put the scripts (settings_db.py & settings_selector.py) whereever you want
  - The program will generate three files (settings.db, path.txt, playpath.txt) which it uses to save data, if you move the scripts, move these files too. Other than that it's completely portable. 
  - If you use the program, please subcsribe the [Steam Workshop Mod](http://steamcommunity.com/sharedfiles/filedetails/?id=1148717746) for the Tool, which I'd like to use to keep track of amount of users and as a plattform for feedback! 
