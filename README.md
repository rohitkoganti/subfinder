# SubFinder
This project creates a standalone executable which can download subtitles for movies/videos. The movie in the computer can be browsed or the name just typed (spelled right). It downloads the English subtitles, if available, into the same folder as the movie. It can also fetch alternate subtitles for a movie. It is implemented using Python 2.7, PyQt4 and py2exe.

# SubFinder.py
This is the 'main' file where everything takes off from. It imports the UI from design.py, images from resources_rc.py and implements several functions- like connecting the buttons with their functionalities- through the class 'MyApp'.

# getsubs.py
This is the where the magic happens. When SubFinder.py calls it, it takes a movie name, the location where it has to be downloaded, among other things and does exactly that. It queries a particular site, scrapes the data, follows hyperlinks and gets our job done.

# design.py and design.ui
These implement the UI aspects of the project. It is first designed in the QtDesigner and later converted into .py file with the help of pyrcc4.

# setup.py
This is the script needed to run the py2exe tool, which converts our python code into an executable, with appropriate flags.

# Main Features:
- The executable is standalone- which means it has no dependencies on any dlls or such.
- It can download subtitles even without the release name of the movie, with just the name (without the year).
- It unzips the folder downloaded and saves the file into the same folder as the movie. 
- Since we 'cache' the possible subtitles for a movie, getting alternate subtitless is much faster.
- Threading is done with QThreads so that the UI does not hang when it is fetching a subtitle.

# Note:
- The executable is to be built with the command 'python setup.py py2exe' in the command prompt.
- The errors, if any, are not flushed out and would printed into a log file. This is for testing purposes. You can choose to 'uncomment' it in the SubFinder.py to ignore the errors. If you find some bugs/discrepancies, ping me at koganti.rohit@gmail.com
