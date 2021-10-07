import os.path
import time

import main
import tkinter as tk
from tkinter import ttk
from threading import Thread
from tkinter.filedialog import askdirectory


def read_from_file():
    papers_from_file = []
    with open('paper_names.txt', 'r') as f:
        papers = f.readlines()
    for paper in papers:
        papers_from_file.append(paper.strip())
    return papers_from_file


def save_file_path(path):
    with open("path.txt", 'w') as f:
        f.write(path)


def read_file_path():
    with open('path.txt', 'r') as f:
        path = f.readline()
    return path.strip()


def save_to_file():
    status.configure(text="Download started..")
    download_button.configure(state=tk.DISABLED)
    papers = []
    if E_Times.get():
        papers.append('E_Times')
    if Hindu.get():
        papers.append('Hindu')
    if T_O_India.get():
        papers.append('T_O_India')
    if B_Line.get():
        papers.append('B_Line')
    if H_Times.get():
        papers.append('H_Times')
    if B_Standard.get():
        papers.append('B_Standard')
    if L_Mint.get():
        papers.append('L_Mint')
    if M_Mirror.get():
        papers.append('M_Mirror')
    if F_Express.get():
        papers.append('F_Express')
    if I_Express.get():
        papers.append('I_Express')
    with open('paper_names.txt', 'w') as f:
        for paper in papers:
            f.write(f'{paper}\n')
    main.main()
    download_button.configure(state=tk.NORMAL)
    status.configure(text="Downloaded")
    time.sleep(2)
    status.configure(text="Idle..")


if __name__ == "__main__":
    selected_papers = read_from_file()
    root = tk.Tk()
    root.title('Newspaper Downloader')
    root.resizable(False, False)
    root.geometry('270x320')

    ttk.Label(root, text="DOWNLOADER", padding=10, font=('Trebuchet MS', 24)).grid(column=0, row=0, columnspan=2)

    E_Times = tk.IntVar(value=1) if 'E_Times' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="Economic Times", onvalue=1, offvalue=0, variable=E_Times, padding=10
    ).grid(column=0, row=1, sticky=tk.W)

    Hindu = tk.IntVar(value=1) if 'Hindu' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="The Hindu", onvalue=1, offvalue=0, variable=Hindu, padding=10
    ).grid(column=1, row=1, sticky=tk.W)

    T_O_India = tk.IntVar(value=1) if 'T_O_India' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="Times of India", onvalue=1, offvalue=0, variable=T_O_India, padding=10
    ).grid(column=0, row=2, sticky=tk.W)

    B_Line = tk.IntVar(value=1) if 'B_Line' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="Business Line", onvalue=1, offvalue=0, variable=B_Line, padding=10
    ).grid(column=1, row=2, sticky=tk.W)

    H_Times = tk.IntVar(value=1) if 'H_Times' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="Hindustan Times", onvalue=1, offvalue=0, variable=H_Times, padding=10
    ).grid(column=0, row=3, sticky=tk.W)

    B_Standard = tk.IntVar(value=1) if 'B_Standard' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="Business Standard", onvalue=1, offvalue=0, variable=B_Standard, padding=10
    ).grid(column=1, row=3, sticky=tk.W)

    L_Mint = tk.IntVar(value=1) if 'L_Mint' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="Live Mint", onvalue=1, offvalue=0, variable=L_Mint, padding=10
    ).grid(column=0, row=4, sticky=tk.W)

    M_Mirror = tk.IntVar(value=1) if 'M_Mirror' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="Mumbai Mirror", onvalue=1, offvalue=0, variable=M_Mirror, padding=10
    ).grid(column=1, row=4, sticky=tk.W)

    F_Express = tk.IntVar(value=1) if 'F_Express' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="Financial Express", onvalue=1, offvalue=0, variable=F_Express, padding=10
    ).grid(column=0, row=5, sticky=tk.W)

    I_Express = tk.IntVar(value=1) if 'I_Express' in selected_papers else tk.IntVar()
    ttk.Checkbutton(
        root, text="Indian Express", onvalue=1, offvalue=0, variable=I_Express, padding=10
    ).grid(column=1, row=5, sticky=tk.W)

    download_button = ttk.Button(
        root, text="Download", cursor="hand2", command=Thread(target=save_to_file).start
    )
    download_button.grid(column=1, row=6, sticky=tk.E, pady=10, padx=10)

    ttk.Separator(root, orient='horizontal').grid(column=0, row=7, columnspan=2, ipady=1, sticky=tk.W+tk.E)

    status = ttk.Label(
        root, text="Idle..", font=('Trebuchet MS', 10)
    )
    status.grid(column=0, row=8, columnspan=2,)

    if not os.path.isdir(read_file_path()):
        save_path = askdirectory()
        save_file_path(path=save_path)

    root.mainloop()
