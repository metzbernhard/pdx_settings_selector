import shutil
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import linecache
import settings_db
import re


class Selector:
	def __init__(self, window):
		# main app
		self.window = window

		# prepare arguments
		self.mods = []
		self.dlc = []
		self.mod = []
		self.game = ''
		self.x = 0
		self.y = 0

		# get paths, either saved or default, see functions
		self.path = self.set_path()
		self.playpath = self.set_playpath()

		# create the database to store data, see settings_db.py
		self.database = settings_db.db()

		# create the GUI, can also be put completely in the __init method
		self.interface()

		# for closing the database, when app is closed, see self._close function
		self.window.protocol("WM_DELETE_WINDOW", self._close)

		self.helptext = '''Create new settings:
1) Set the path to settings.txt and (optional) the path to Steam
2) Select the Game you want
3) Start the Launcher and set the settings you want to save
4) Either close the Launcher or start the game 
(otherwise the settings.txt won't be saved)
5) Enter a Name for your settings and click the button to save
        
Start the game using settings:
1) Select the game you want to start
2) Select the settings you want to use in the dropdown menu
3) Click "Use"
4) Either start EU4 via Steam or the directly via the Play Button if Steampath is set
        
Delete settings:
1) Select the game
2) Select the settings you want to delete in the dropdown menu
3) Click Delete'''

	def interface(self):
		self.window.title('PDX Settings Selector')
		self.style = ttk.Style()

		# HEADER
		self.frame_header = ttk.Frame(self.window)
		self.frame_header.grid(row=1, column=0)
		# self.logo = PhotoImage(file='eu4.gif')
		# removed because it crashed the compile process, not sure why

		# ttk.Label(self.frame_header, image=self.logo).grid(column=0, row=0, rowspan=2)
		self.header = ttk.Label(self.frame_header, text='Paradox\nSettings Selector', font=('Arial', 20, 'bold'),
								justify=CENTER).grid(row=0, column=0)

		# help
		self.helpframe = ttk.Frame(self.frame_header, padding=(5, 5))
		self.helpframe.grid(row=1, column=0)
		self.help = ttk.Button(self.helpframe, text="How to use this tool", command=lambda: self.helpmessage())
		self.help.grid(row=0, column=0, columnspan=2, pady=5)

		ttk.Separator(self.window, orient=HORIZONTAL).grid(row=2, column=0, sticky="ew", pady=10)

		# give me your path
		self.frame_path = ttk.LabelFrame(self.window, text='Path', padding=(3, 3), height=75, width=300, borderwidth=3)
		self.frame_path.grid(row=3, column=0)
		self.frame_path.grid_propagate(0)
		self.frame_pathentry = ttk.Entry(self.frame_path, width=47)
		self.frame_pathentry.grid(row=0, column=0, columnspan=2)
		self.frame_pathentry.insert(0, self.path)

		self.frame_game = ttk.LabelFrame(self.window, text='Select Game', padding=(3, 3), height=75, width=300, borderwidth=3)
		self.frame_game.grid(row=4, column=0)
		self.frame_game.grid_propagate(0)
		self.eubutton = ttk.Button(self.frame_game, text='Europa Universalis IV', width=22,
									command=lambda: self.populate_selectionbox('Europa Universalis IV'))
		self.hoibutton = ttk.Button(self.frame_game, text='Hearts of Iron IV', width=22,
									command=lambda: self.populate_selectionbox('Hearts of Iron IV'))
		self.stebutton = ttk.Button(self.frame_game, text='Stellaris', width=22,
									command=lambda: self.populate_selectionbox('Stellaris'))
		self.ckbutton = ttk.Button(self.frame_game, text='Crusader Kings II', width=22,
									command=lambda: self.populate_selectionbox('Crusader Kings II'))
		self.eubutton.grid(row=1, column=0)
		self.hoibutton.grid(row=1, column=1)
		self.stebutton.grid(row=2, column=0)
		self.ckbutton.grid(row=2, column=1)
		self.ckbutton['state'] = 'disabled'

		# select path
		self.frame_pathbutton = ttk.Button(self.frame_path, text='Select Paradox Documents Path...',
										   command=lambda: self.getdirectory())
		self.frame_pathbutton.grid(row=1, column=0, sticky="w")

		ttk.Separator(self.window, orient=HORIZONTAL).grid(row=5, column=0, sticky="ew", pady=10)

		# insert name
		self.frame_name = ttk.LabelFrame(self.window, text='Name', padding=(3, 3), height=75, width=300, borderwidth=3)
		self.frame_name.grid(row=6, column=0)
		self.frame_name.grid_propagate(0)
		self.frame_name_entry = ttk.Entry(self.frame_name, width=47)
		self.frame_name_entry.grid(row=0, column=0, columnspan=2)

		# parsing settings.txt
		self.frame_setting = ttk.Button(self.frame_name, text='Scrape and Save Current Settings',
										command=lambda: self.scrape(self.game))
		self.frame_setting.grid(row=1, column=0, sticky="w")

		ttk.Separator(self.window, orient=HORIZONTAL).grid(row=7, column=0, sticky="ew", pady=10)

		# selector
		self.frame_selector = ttk.LabelFrame(self.window, text='Selector', padding=(3, 3), borderwidth=3, height=55,
											 width=300)
		self.frame_selector.grid(row=8, column=0)
		self.frame_selector.grid_propagate(0)

		selection = StringVar()
		self.selectionbox = ttk.Combobox(self.frame_selector, textvariable=selection)
		self.selectionbox.grid(row=0, column=0, sticky="e")
		# self.populate_selectionbox()

		self.use_button = ttk.Button(self.frame_selector, text="Use", width=10, command=lambda: self.write_settings())
		self.use_button.grid(row=0, column=1, sticky="e")

		self.delete_button = ttk.Button(self.frame_selector, text="Delete", width=10,
										command=lambda: self.delete_settings())
		self.delete_button.grid(row=0, column=2, sticky="e")

		ttk.Separator(self.window, orient=HORIZONTAL).grid(row=9, column=0, sticky="ew", pady=10)

		# play-section
		self.frame_play = ttk.LabelFrame(self.window, text='Play', padding=(3, 3), height=80, width=300)
		self.frame_play.grid(row=10, column=0)
		self.frame_play.grid_propagate(0)

		self.playentry = ttk.Entry(self.frame_play, width=47)
		self.playentry.grid(row=0, column=0, columnspan=2)
		self.playentry.insert(0, self.playpath)

		self.play_button = ttk.Button(self.frame_play, text="Play", width=20, command=lambda: self.start())
		self.play_button.grid(row=1, column=0, sticky='w')

		self.play_setpath = ttk.Button(self.frame_play, text="Set Steam Path...", width=20,
									   command=lambda: self.getplaydirectory())
		self.play_setpath.grid(row=1, column=1, sticky='e')

	def helpmessage(self):
		messagebox.showinfo(title="How to use", message=self.helptext)

	def set_path(self):
		if os.path.exists('path.txt'):
			with open('path.txt', 'r') as f:
				return f.read()
		else:
			with open('path.txt', 'w') as f:
				f.write('C:\\Users\\YOURUSERNAME\\Documents\\Paradox Interactive')
				return 'C:\\Users\\YOURUSERNAME\\Documents\\Paradox Interactive'

	def set_playpath(self):
		if os.path.exists('playpath.txt'):
			with open('playpath.txt', 'r') as f:
				return f.read()
		else:
			with open('playpath.txt', 'w') as f:
				# print('why')
				f.write('C:\\Program Files\\Steam\\steamapps\\common')
				return 'C:\\Program Files\\Steam\\steamapps\\common'

	def start(self):
		# starts the game with the used settings
		workpath = os.getcwd()
		try:
			os.chdir(self.playpath)
		except FileNotFoundError:
			messagebox.showerror(title="Path not found", message="Could not find specified path!")
			return
		game = self.game
		if game == '':
			messagebox.showinfo(title="No Game selected", message='Please select the game you want to start')
		elif game == 'Europa Universalis IV':
			os.chdir(game)
			os.system(r'eu4.exe -skiplauncher')
		elif game == 'Hearts of Iron IV':
			os.chdir(game)
			# HoI does not have -skiplauncher and -nolauncher ignores for some reason the mods, so we have to do this...
			specialhoistring = 'hoi4.exe -nolauncher'
			data = self.database.get(self.selectionbox.get(), self.game)
			modlist = data['mods'].split(',')
			for mod in modlist:
				specialhoistring = specialhoistring + ' -mod=mod/' + mod
			# print(specialhoistring)
			os.system(specialhoistring)
		elif game == 'Stellaris':
			os.chdir(game)
			os.system(r'stellaris.exe -skiplauncher')
		os.chdir(workpath)

	def _close(self):
		"""closes the db, before closing the window"""
		self.database.close()
		self.window.destroy()

	def getdirectory(self):
		"""Asks Directory for Documents Paradox Folder"""
		self.path = filedialog.askdirectory()
		self.frame_pathentry.delete(0, END)
		self.frame_pathentry.insert(0, self.path)
		with open('path.txt', 'w') as f:
			f.write(self.path)

	def getplaydirectory(self):
		"""Asks Steam/steamapps/common folder for game starting"""
		self.playpath = filedialog.askdirectory()
		self.playentry.delete(0, END)
		self.playentry.insert(0, self.playpath)
		with open('playpath.txt', 'w') as f:
			f.write(self.playpath)

	def populate_selectionbox(self, game):
		"""Puts the valid settings in the selectionbox"""
		# games = {'Europa Universalis IV': 'EU4', 'Hearts of Iron IV': 'HoI 4', 'Stellaris': 'Stellaris'}
		names = []
		self.game = game
		for row in self.database:
			if row['game'] == game:
				names.append(row['name'])
		self.selectionbox.config(values=names)
		if names:
			self.selectionbox.set(names[-1])
		else:
			# set to empty when no settings to select
			self.selectionbox.set('')

	def scrape(self, game):
		"""Scrapes the settings.txt for settings, takes name of the game"""
		set_name = self.frame_name_entry.get()
		# check if name is entered:
		if len(set_name) == 0:
			messagebox.showinfo(title="No Name", message="Please enter name for settings")
			return
		if self.game == '':
			messagebox.showinfo(title="No Game", message="Please select the game you want to save settings for")
			return
		# print (self.database.check(set_name))
		# check if name is in use:
		if self.database.check(game, set_name):
			messagebox.showinfo(title="Duplicate",
								message="Name is already used for settings. Either Delete Set to create a new one under this name or choose a different name")
			return
		workpath = os.getcwd()
		os.chdir(self.path + '\\' + game)
		# print(os.getcwd())
		# error message if path is not correct, since this will already throw an exception, no further
		# handling down for the open command.
		# print(linecache.getline('settings.txt', 5))
		try:
		# using linenumber because it's always the same and x= is twice in the file
			self.x = int(number_re(linecache.getline('settings.txt', 5)))
			self.y = int(number_re(linecache.getline('settings.txt', 6)))
		except FileNotFoundError:
			messagebox.showerror(title='Parsing Error',
								 message='Error parsing settings.txt, did you set the path correctly?')
			return
		self.dlc = []
		self.mod = []
		file = open('settings.txt', 'r')
		# going through the file, saving the relevant information
		# could have used RE instead of list-slicing
		for line in file:
			# print(line)
			if 'language' in line:
				self.lang = line[12:-2]
			elif 'fullScreen' in line:
				if ('no' in line[12:]):
					self.fs = 0
				elif ('yes' in line[12:]):
					self.fs = 1
			elif 'borderless' in line:
				if ('no' in line[12:]):
					self.bl = 0
				elif ('yes' in line[12:]):
					self.bl = 1
			elif '.dlc' in line:
				self.dlc.append(line[6:-2])
			elif '.mod' in line:
				self.mod.append(line[6:-2])
		# put the data in the database
		self.database.new(game=game, name=set_name, lang=self.lang, rx=self.x, ry=self.y, fs=self.fs, bl=self.bl,
						  mods=self.mod,
						  dlc=self.dlc)
		self.populate_selectionbox(self.game)
		messagebox.showinfo(title="Done", message="Saved Current settings.txt for " + game + " under " + set_name)
		self.frame_name_entry.delete(0, END)
		# I always go back to the workpath, isn't really necessary
		os.chdir(workpath)

	def write_settings(self):
		"""Writes the data into the settings.txt, no arguments, uses self.game"""
		data = self.database.get(self.selectionbox.get(), self.game)
		workpath = os.getcwd()
		os.chdir(self.path + '\\' + self.game)
		# print(data)
		# print(os.getcwd())
		try:
			with open('settings.txt', 'r') as f:
				file = f.read()
		except FileNotFoundError:
			messagebox.showerror(title='Not Found', message="Couldn't find settings.txt, something is wrong with the Path!")
			return
		# put content of settings.txt in text to do string-manipulations
		text = file.splitlines()
		# uses linenumber, breaks, when PDX decides to change layout of settings.txt
		# some of this could have be done nice with REs now that I think about it
		# print(text)
		text[1] = 'language="l_' + data['lang'] + '"'
		text[4] = '\t\tx=' + str(data['rx'])
		text[5] = '\t\ty=' + str(data['ry'])
		# writes data
		fs = self.yes_no(data['fs'])
		index = [i for i, s in enumerate(text) if 'fullScreen' in s]
		text[index[0]] = '\tfullScreen=' + fs
		bl = self.yes_no(data['bl'])
		index = [i for i, s in enumerate(text) if 'borderless' in s]
		text[index[0]]= '\tborderless=' + bl
		# remove current dlc/mods in settings.txt to write the ones we want
		text = [x for x in text if '.dlc' not in x]
		text = [x for x in text if '.mod' not in x]
		# print(text)
		# put dlcs and mods from database into a list
		dlclist = data['dlc'].split(',')
		# print(dlclist)
		modlist = data['mods'].split(',')
		# print(modlist)
		# prepare for if-monster
		# the different games want the mods/dlc part at different part of the settings file
		# when no dlcs are activated the part is removed and needs to be added empty before filling up with DLCs & Mods
		if self.game == 'Europa Universalis IV':
			if 'last_dlcs={' not in text:
				text = text + ['last_dlcs={','}']
			if 'last_mods={' not in text:
				text = text + ['last_mods={','}']
		if self.game == 'Hearts of Iron IV':
			if 'last_dlcs={' not in text:
				text.insert(self.select_contain(text, 'hints') + 1, 'last_dlcs={')
				text.insert(self.select_contain(text, 'last_dlcs={') + 1, '}')
			if 'last_mods={' not in text:
				text.insert(self.select_contain(text, 'counter'), 'last_mods={')
				text.insert(self.select_contain(text, 'counter'), '}')
		if self.game == 'Stellaris':
			if 'last_dlcs={' not in text:
				text.insert(self.select_contain(text, 'name=') + 1, 'last_dlcs={')
				text.insert(self.select_contain(text, 'last_dlcs={') + 1, '}')
			if 'last_mods={' not in text:
				text.insert(self.select_contain(text, 'autosave'), 'last_mods={')
				text.insert(self.select_contain(text, 'autosave'), '}')
		# now last_dlcs and last_mods exist at the correct part of the setting.txt, let's populate it
		if dlclist != ['']:
			for dlc in dlclist:
				text.insert(self.select_contain(text, 'last_dlcs') + 1, '\t"dlc/' + dlc + '"')
		if modlist != ['']:
			for mod in modlist:
				text.insert(self.select_contain(text, 'last_mods') + 1, '\t"mod/' + mod + '"')
		# make text into a multiline string to write to data
		text2 = [x + '\n' for x in text]
		text2 = ''.join(text2)
		with open('settings.txt', 'w') as f:
			f.write(text2)
			f.close()
		os.chdir(workpath)

	def select_contain(self, list, string):
		"""selects the line in list that contains string, returns index"""
		# why didn't I use text[text.index()] directly?
		for item in list:
			if string in item:
				# print(item)
				return list.index(item)

	def yes_no(self, int):
		"""turns int into yes or no"""
		if int == 0:
			return 'no'
		elif int == 1:
			return 'yes'

	def delete_settings(self):
		"""deletes settings from database"""
		self.database.delete(self.selectionbox.get(), self.game)
		self.populate_selectionbox(self.game)



###############################################################################################

def main():
	window = Tk()
	# build me a GUI
	selector = Selector(window)
	window.mainloop()


def number_re(text):
	find = re.search('[0-9]+', text)
	if find:
		return find.group()


if __name__ == "__main__":
	main()
