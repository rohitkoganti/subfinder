import urllib3
from PyQt4.QtCore import QThread, SIGNAL
from bs4 import BeautifulSoup
import zipfile
from StringIO import StringIO
import re
import os

class GetSubsThread(QThread):

    def __init__(self, location, query, subLinksList, subNameList, movieName):
        QThread.__init__(self)
        self.location = location
        self.query = query
        self.subLinksList = subLinksList
        self.subNameList = subNameList
        self.movieName = movieName

    def __del__(self):
        self.wait()

    def _get_the_subs(self, location, query, subLinksList, subNameList, movieName ):
        http = urllib3.PoolManager(timeout=3.0)

        # Making the subLinksList for the first download. Do this only when there's no movieName.
        if not subLinksList and not movieName:
            if location:
                print 'Trying for title: ', query.replace(" ", "-")
                url = 'https://subscene.com/subtitles/' + query.replace(" ", "-")
            else:
                print 'Trying for title: ', query.replace(" ", "-")
                url = 'https://subscene.com/subtitles/' + query.replace(" ", "-")
            try:
                releasePage = http.request('GET', url)
                soup = BeautifulSoup(releasePage.data, "html.parser")
                print 'Link:', soup.link.get('href')
            except AttributeError:
                print "No exact matches found. Spell check!"
                return movieName, None, None, 2
            except urllib3.exceptions.MaxRetryError, urllib3.exceptions.TimeoutError:
                print "Max Retries or Timeout error. Returning nothing."
                return movieName, None, None, 1

            # If the query stays on the title page without redirecting, do this.
#            if 'https://subscene.com/subtitles/searchbytitle' in soup.link.get('href').encode('ascii', 'ignore'):
#               try:
#                   moviePageurl = soup.find("h2", {"class": "exact"}).next_sibling.next_sibling.a.get('href')
#                   print 'Exact match:', moviePageurl
#                   moviePage = http.request('GET', 'https://subscene.com' + moviePageurl)
#                   soup = BeautifulSoup(moviePage.data, "html.parser")
#               except urllib3.exceptions.MaxRetryError, urllib3.exceptions.TimeoutError:
#                   return movieName, None, None, 1
#               except AttributeError:
#                   print "No exact matches found. Spell check!"
#                   return movieName, None, None, 2

            # When at the release page or the movie page.
            print 'Making the subLinksList..'
            subLinksList = [sub for sub in soup.find_all("td", {"class": "a1"}) if 'English' in sub.a.span.text]

            # When we have the subLinksList, either for the first time or otherwise(when we directly jump here)
        for index, sub in enumerate(subLinksList):
            if sub.a.contents[3].text.encode('ascii', 'ignore').strip() not in subNameList:
                downloadPageUrl = sub.a.get('href')
                try:
                    downloadPage = http.request('GET', 'https://subscene.com' + downloadPageUrl)
                except urllib3.exceptions.MaxRetryError, urllib3.exceptions.TimeoutError:
                    return movieName, None, subLinksList, 1
                secondSoup = BeautifulSoup(downloadPage.data, "html.parser")
                pageMovieName = secondSoup.find("span", {"itemprop": "name"}).text.encode('ascii', 'ignore').strip()
                if pageMovieName != movieName:
                    print 'MovieName:', pageMovieName  # Printing all unique title names of the download page.
                if (movieName and (movieName == pageMovieName)) or not movieName:
                    movieName = pageMovieName
                    downloadLink = secondSoup.find_all("a", {"id": "downloadButton"})[0].get('href')
                    break

        if 'downloadLink' in locals():
            try:
                subFile = http.request('GET', 'https://subscene.com' + downloadLink)
                zip_ref = zipfile.ZipFile(StringIO(subFile.data), 'r')
                zip_ref.extractall(location)
                zip_ref.close()
            except urllib3.exceptions.MaxRetryError, urllib3.exceptions.TimeoutError:
                return movieName, None, subLinksList, 1
            except zipfile.BadZipfile:
                print "Can't unzip this time. Downloading it directly."
                filetitle = subFile.headers.get('content-disposition')
                if not location:
                    location = os.getcwd()
                with open(location.encode('ascii', 'ignore') + '/' + re.findall("filename=(.+)", filetitle)[0], "wb") as code:
                    code.write(subFile.data)

            # Copying the other similar release names (even when there's a bad zipfile.) and slice the subLinksList
            subLinksList = subLinksList[index + 1:]
            print 'Len(subLinksList):', len(subLinksList)
            try:
                otherSubNames = [element.text.encode('ascii', 'ignore').strip()
                                 for element in secondSoup.find("li", {"class": "release"}).findChildren('div')]
                return movieName, otherSubNames, subLinksList, None
            except AttributeError:
                return movieName, None, subLinksList, None
        else:
            print 'Could not find any(more) English subtitles!'
            return movieName, None, subLinksList, 3

    def run(self):
        urllib3.disable_warnings()
        sub_param = self._get_the_subs(self.location, self.query, self.subLinksList, self.subNameList, self.movieName)
        self.emit(SIGNAL('subtitle_params(PyQt_PyObject)'), sub_param)