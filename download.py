import urllib2
from bs4 import BeautifulSoup
import os

xkcd_url = "http://xkcd.com"
url = "http://xkcd.com/163"

def download_xkcd(url):
	if not url=="http://xkcd.com/404":
		response = urllib2.urlopen(url)
		content = response.read()
		soup = BeautifulSoup(content)

	comic_num = url[16:]
	for links in soup.find_all('img'):
		if "comics" in links.get('src'):
			comic_url = links.get('src')
			comic_title = links.get('alt')
			comic_desc = links.get('title')
	
	comic_title = comic_title.replace("/"," (or) ")
	xkcd_path = '/home/santosh/xkcd'
	if not os.path.exists(xkcd_path):
		print "\n\tCreating directory \'" + xkcd_path + "\'..."
		os.mkdir(xkcd_path)
	
	comic_path = ""
	comic_path = xkcd_path + "/" + str(comic_num)
	if not os.path.exists(comic_path):
		print "\n\tCreating directory \'" + comic_path + "\'..."
		os.mkdir(comic_path)

	comic_response = urllib2.urlopen(comic_url)
	comic_content = comic_response.read()
	comic_file = ""
	comic_file = comic_path + "/" + comic_title + comic_url[-4:]
	if not os.path.exists(comic_file):
		print "\n\tDownloading comic \'" + comic_title + "\'..."
		f = open(comic_file,"w")
		f.write(comic_content)
		f.close()
		print "\n\tComic \'" + comic_title + "\' successfully downloaded!"
	comic_prev_link = ""
	comic_prev = ""
	comic_next_link = ""
	comic_next = ""
	for links in soup.find_all('a'):
		if not links.get('rel') == None:
			if not links.get('accesskey') == None:
				if 'p' in links.get('accesskey'):
					comic_prev_link = links.get('href')
					comic_prev = xkcd_url + links.get('href')
				#if 'n' in links.get('accesskey'):
					#comic_next_link = links.get('href')
					#comic_next = xkcd_url + links.get('href')

	#if not comic_next_link == "#":
		#print "\n\t Next - " + comic_next
	if not comic_prev_link == "#":
		print "\n\t\t\t Prev Comic link- " + comic_prev
		download_xkcd(comic_prev)
	else:
		print "\n\n\t\t All comics downloaded successfully! XKCD!"

def main():
	download_xkcd(url)

if __name__ == '__main__':
	main()
