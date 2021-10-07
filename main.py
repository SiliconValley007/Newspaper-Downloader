import socket
import sys
import winreg

import requests
import os

import urllib3.exceptions
from bs4 import BeautifulSoup
from plyer import notification


def read_names():
    papers_from_file = []
    with open('paper_names.txt', 'r') as f:
        papers = f.readlines()
    for paper in papers:
        papers_from_file.append(paper.strip())
    return papers_from_file


def read_path():
    with open('path.txt', 'r') as f:
        path = f.readline()
    return path.strip()


def main():
    try:
        program_path = os.path.abspath(sys.argv[0])
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key, 'Newspaper', 0, winreg.REG_SZ, program_path)
        key.Close()

        path = read_path()

        if not os.path.isdir(f'{path}Newspaper'):
            os.mkdir(f'{path}Newspaper')

        urls = {
            'E_Times': ['https://www.careerswave.in/the-economic-times-epaper-pdf/', 'Economic Times'],
            'Hindu': ['https://www.careerswave.in/the-hindu-pdf-epaper-free-november/', 'The Hindu'],
            'T_O_India': ['https://www.careerswave.in/the-times-of-india-newspaper-pdf/', 'Times Of India'],
            'B_Line': ['https://www.careerswave.in/business-line-newspaper/', 'Business Line'],
            'H_Times': ['https://www.careerswave.in/hindustan-times-newspaper-download/', 'Hindustan Times'],
            'B_Standard': ['https://www.careerswave.in/business-standard-newspaper-download/', 'Business Standard'],
            'L_Mint': ['https://www.careerswave.in/mint-newspaper/', 'Live Mint'],
            'M_Mirror': ['https://www.careerswave.in/mumbai-mirror-epaper-pdf/', 'Mumbai Mirror'],
            'F_Express': ['https://www.careerswave.in/the-financial-express-epaper-pdf/', 'Financial Express'],
            'I_Express': ['https://www.careerswave.in/indian-express-newspaper/', 'Indian Express'],
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }

        date = ''
        pdf_link = ''
        papers = read_names()
        for paper in papers:
            req_s = requests.get(urls[paper][0], headers=headers)
            soup = BeautifulSoup(req_s.text, 'lxml')
            name = urls[paper][1]

            for link in soup.find_all('tr', class_="ninja_table_row_0 nt_row_id_0"):
                date = link.find_all('td')[0].text.strip()
                pdf_link = link.find_all('td')[1].text
            if pdf_link != '':
                if not os.path.isdir(f'{path}Newspaper//{date}'):
                    os.mkdir(f'{path}Newspaper//{date}')
                if not os.path.exists(f'{path}Newspaper//{date}//{date}{name}.pdf'):
                    pdf_req = requests.get(pdf_link)
                    pdf_soup = BeautifulSoup(pdf_req.text, 'lxml')

                    for links in pdf_soup.find_all('iframe', class_='iframe'):
                        r = requests.get(links.get('src'))
                        with open(f'{path}Newspaper//{date}//{date}{name}.pdf', 'wb') as f:
                            f.write(r.content)
                        notification.notify(
                            title="Download Successful",
                            message=f'{name} newspaper for {date} downloaded.',
                            timeout=5,
                        )
            else:
                notification.notify(
                    title="Try Later",
                    message=f'{name} newspaper for {date} not published yet.',
                    timeout=1,
                )
    except (
            socket.gaierror, urllib3.exceptions.NewConnectionError,
            urllib3.exceptions.MaxRetryError,
            requests.exceptions.ConnectionError
    ):
        notification.notify(
            title="Disconnected",
            message='Could not connect to the internet. Please connect to the internet and try again.',
            timeout=3,
        )


if __name__ == "__main__":
    main()
