# Newspaper-Downloader

![newspaper](https://user-images.githubusercontent.com/63968451/136515138-cd9fa596-7366-4f83-8121-b54addb789bb.png)

A simple python GUI program utilizing python web scraping to automatically download the selected newspapers of the current date from the careerswave website(https://www.careerswave.in/). This website contains download links for multiple newspapers but i have used only the ones i needed. You can easily add more to this program by adding the names and urls to the dictionary in main.py. Run the UI.py script, select the directory in which you want to store all the downloaded newspapers. Then select all the required newspapers you want to be downloaded everyday and click on the save button. Upon clicking the save button the main.py file will be automatically added to the registry so that it is automatically run everytime you power on your system. You can change which newspapers you want to be downloaded at any time using the Tkinter GUI and the changes will be reflected in the next download.

Run the following command to install the required packages:
> pip install requests, beautifulsoup4, plyer
