import urllib
from bs4 import BeautifulSoup as Soup
import os
import time

url = "http://xkcd.com/archive"
explain = "http://www.explainxkcd.com/wiki/index.php/"
save = "/home/santosh/xkcd"
comic_list = list()


def get_soup(url):
	content = urllib.urlopen(url).read()
	soup = Soup(content)
	return soup
def get_details(soup):
	link_list = soup.find_all('a')
	for comic in link_list:
		if comic.get('href')[1:-1].isdigit():
			comic_link = url[:15]+comic.get('href')
			comic_set = (comic.get('href')[1:-1],comic.get('title'),url[:15]+comic.get('href'),comic.text.replace("/", " (or) "))
			comic_list.append(comic_set)
	return comic_list

def comic_download(comic_list,min_range,max_range): 
	if min_range==0 and max_range==1:
		#Download Latest comic
		for num in xrange(min_range,max_range):
			comic_num = comic_list[num][0]
			comic_date = comic_list[num][1]
			comic_link = comic_list[num][2]
			comic_title = comic_list[num][3]
			comic_content = urllib.urlopen(comic_link).read()
			comic_soup = Soup(comic_content)
			comic_img = comic_soup.find_all('img')[1].get('src')
			comic_desc = comic_soup.find_all('img')[1].get('title')
			comic_explain = explain + comic_num
			file_name = comic_num + "_" + comic_title + "_" + comic_date + comic_img[-4:]
			#comic_content.close()
			if not os.path.exists(save):
				print "\n\tCreating Directory : " + save
				os.mkdir(save)

			if not os.path.exists(save+'/'+'comics'):
				print "\n\tCreating Directory : " + save + '/' + 'comics'
				os.mkdir(save+'/'+'comics')

			if not os.path.exists(save+'/comics/' + file_name):
				img = urllib.urlopen(comic_img).read()
				print "\n\tDownloading comic #" + comic_num + " - " + save + "/comics/" + file_name
				comic = open(save+'/'+'comics'+'/'+file_name,"w")
				comic.write(img)
				comic.close()
				time.sleep(5)
			else:
				print "\n\tSkipping comic #" + comic_num + " - " + save + "/comics/" + file_name
				print "\t\tReason - File already exists!"
	else:
		for num in xrange(min_range,max_range):
			comic_num = comic_list[num][0]
			comic_date = comic_list[num][1]
			comic_link = comic_list[num][2]
			comic_title = comic_list[num][3]
			comic_content = urllib.urlopen(comic_link).read()
			comic_soup = Soup(comic_content)
			comic_img = comic_soup.find_all('img')[1].get('src')
			comic_desc = comic_soup.find_all('img')[1].get('title')
			comic_explain = explain + comic_num
			file_name = comic_num + "_" + comic_title + "_" + comic_date + comic_img[-4:]
			#comic_content.close()
			if not os.path.exists(save):
				print "\n\tCreating Directory : " + save
				os.mkdir(save)

			if not os.path.exists(save+'/'+'comics'):
				print "\n\tCreating Directory : " + save + '/' + 'comics'
				os.mkdir(save+'/'+'comics')

			if not os.path.exists(save+'/comics/' + file_name):
				img = urllib.urlopen(comic_img).read()
				print "\n\tDownloading comic #" + comic_num + " - " + save + "/comics/" + file_name
				comic = open(save+'/'+'comics'+'/'+file_name,"w")
				comic.write(img)
				comic.close()
				time.sleep(5)
			else:
				print "\n\tSkipping comic #" + comic_num + " - " + save + "/comics/" + file_name
				print "\t\tReason - File already exists!"

def main():
	print "\t\t\txkcd Comic Downloader v0.55a\n\n"
	soup = get_soup(url)
	comic_list = get_details(soup)
	comic_range = int(comic_list[0][0])
	print "\tLatest Comic\t:\t#" + str(comic_range) + "\n"
	print "Options:-\n\t1.Download all comics.\n\t2.Download specific set of comics.\n\t3.Download Latest Comic"
	choice = raw_input("Enter your choice : ")
	if choice=="1":
		comic_download(comic_list,0,max_range)
	elif choice=="2":
		min_range = raw_input("Enter the initial comic number : ")
		min_range = int(min_range)
		#max_range_temp = comic_range - min_range
		max_range = raw_input("Enter the final comic number : ")
		max_range = int(max_range)
		#min_range_temp = comic_range - max_range
		#max_range = min_range_temp
		#min_range = max_range_temp
		comic_download(comic_list,comic_range-max_range,comic_range-min_range+1)
	elif choice=="3":
		comic_download(comic_list,0,1)
	else:
		print "INVALID CHOICE ENTERED!"

if __name__ == '__main__':
	main()
