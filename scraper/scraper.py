#!/usr/bin/python3.6
import os
import sys
import urllib

''''
AnonExcavationCrew: 03/22/2019
You can reach us at: https://discord.gg/vKhAsB

This application is designed to make scraping a newline delimited list of URLs and download the 
website in it's entirety for viewing offline. This currently does not scrape ALL URLS associated.
It merely downloads the URLs provided in the list. This is not YET a crawler. Site-for-site...
'''

class Scraper:

    def scrape(self, urlList):
        #Get the current directory
        cwd = os.getcwd()
        #Iterate the URL list and try to download each page. May not always work due to page redirection
        #on pages like google, youtube, facebook, etc. Not targeted pages normally. Put some checks for
        #common mistakes that would be enountered. 
        with open(urlList) as urllist:
            urlCount = 0
            for url in urllist:
                try:
                    print("Downloading {0} to {1}/".format(url, cwd))
                    urlData = urllib.URLopener()
                    urlData.retrieve("{0}".format(url), "{0}/URL_{1}.html".format(cwd, urlCount))
                    print("Download complete!")
                    urlCount += 1
                except Exception as e:
                    print("Invalid URL detected. Passing!")
                    urlCount += 1
        

    def argCheck(self):
        #Check to ensure the proper number of arguments have been passed at runtime
        argLen = len(sys.argv)
        if argLen != 2:
            print("ERROR:: Invalid number of arguments. Please only pass the location of the URL list ex:")
            print("python ./scraper.py /location/of/list.txt")
            sys.exit()
        #Ensure that the URl file exists. Too lazy to check consistency of URL format. New lines. not hard folks.
        urlPath = sys.argv[1]
        if os.path.isfile(urlPath):
            Scraper().scrape(urlPath)
        else:
            print("Invalid file path. Check that file exists and try again.")


Scraper().argCheck()
