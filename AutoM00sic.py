#!/usr/bin/env python3
from os import listdir, getcwd, chdir
from ast import literal_eval
import youtube_dl

music_dir = ""
ydl_opts = {'download_archive': 'download_archive'}

def qna(dir_list, artist_dict):
	for dirs in dir_list: 
		if dirs not in artist_dict.keys():
			print("do u want to automate", dirs, "? Type y/n/s(kip for now)") 
			care = input('> ')                                 
			if str.lower(care) == 'y':			   
				print('enter soundcloud artist track page url')
				url = input('> ')
				artist_dict[dirs]=url 
			elif str.lower(care) == 'n':
				artist_dict[dirs]="ignore" 
	with open("artist_list.dat", "w", encoding="utf-8") as artist_dict_fh:
		artist_dict_fh.write(str(artist_dict))
		artist_dict_fh.close()	
	return artist_dict

def download(artist_dict):
	startpath = getcwd()
	for key in artist_dict.keys():
		if not artist_dict.get(key) == "ignore":
			arraystuff = artist_dict.get(key).split("/")
			if "soundcloud.com" in arraystuff:
				chdir(music_dir + '/' + key)
				with youtube_dl.YoutubeDL(ydl_opts) as ydl:
					ydl.download([artist_dict.get(key)])
				chdir(startpath)
			else: 
				print("im lazy sorry. just use soundcloud")

def main():		
	dir_list = listdir(music_dir)
	with open("artist_list.dat", 'r') as artist_dict_fh:
		artist_dict_str = artist_dict_fh.read()
		artist_dict_fh.close()
	if len(artist_dict_str) > 0:
		artist_dict = literal_eval(artist_dict_str)
	else:
		artist_dict = {}
	qna(dir_list, artist_dict)
	download(artist_dict)	

if __name__ ==  '__main__':
	main()
