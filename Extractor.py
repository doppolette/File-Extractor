import webbrowser
import os
import tkinter.filedialog
import tkinter as tk
import shutil


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Extractor")

        self.parent.geometry("370x160")

        self.fromdirectory_label = tk.Label(text="Extract from:")
        self.fromdirectory_label.grid(row=0, column=0, sticky="W")

        self.fromdirectory_entry = tk.Entry(borderwidth=3, relief="groove")
        self.fromdirectory_entry.grid(
            row=0, column=1, columnspan=2, ipadx=50, pady=5, padx=3)

        self.fdir_button = tk.Button(
            command=self.get_fdirectory, text="Browse...", borderwidth=3, relief="groove")
        self.fdir_button.grid(row=0, column=3)

        self.todirectory_label = tk.Label(text="Extract to:")
        self.todirectory_label.grid(row=1, column=0, sticky="W")

        self.todirectory_entry = tk.Entry(borderwidth=3, relief="groove")
        self.todirectory_entry.grid(row=1, column=1, columnspan=2, ipadx=50)

        self.tdir_button = tk.Button(
            command=self.get_tdirectory, text="Browse...", borderwidth=3, relief="groove")
        self.tdir_button.grid(row=1, column=3)

        self.filename_label = tk.Label(text="File Name:")
        self.filename_label.grid(row=2, column=0, sticky="W")

        self.filename_entry = tk.Entry(borderwidth=3, relief="groove")
        self.filename_entry.grid(
            row=2, column=1, ipadx=35, padx=(0, 14))

        self.naming_label = tk.Label(text="Rename to:")
        self.naming_label.grid(row=3, column=0, sticky="W")

        self.naming_entry = tk.Entry(borderwidth=3, relief="groove")
        self.naming_entry.grid(row=3, column=1, ipadx=35, padx=(0, 14))

        self.extract_button = tk.Button(
            text="EXTRACT", borderwidth=2, relief="groove", command=self.extract)
        self.extract_button.grid(row=4, column=1, pady=8)

        self.git_button = tk.Button(
            borderwidth=2, relief="groove", command=self.open_git, text="GitHub")
        self.git_button.grid(row=2, rowspan=2, column=2,
                             columnspan=2, ipadx=6, ipady=10, padx=(0, 15), pady=(7, 0))

    def get_fdirectory(self):
        filePath = tk.filedialog.askdirectory()
        self.fromdirectory_entry.delete(0, tk.END)
        self.fromdirectory_entry.insert(0, filePath)

    def get_tdirectory(self):
        filePath = tk.filedialog.askdirectory()
        self.todirectory_entry.delete(0, tk.END)
        self.todirectory_entry.insert(0, filePath)

    @staticmethod
    def open_git():
        webbrowser.open("https://github.doppolettecom/", new=1)

    def extract(self):
        filename = self.filename_entry.get()
        newname = self.naming_entry.get()
        fdirectory = self.fromdirectory_entry.get().replace("/", "\\")
        tdirectory = (self.todirectory_entry.get() +
                      "\\New Extractor Folder").replace("/", "\\")
        os.mkdir(tdirectory)

        filenum = 1

        for dirpath, dirnames, filenames in os.walk(fdirectory):
            dirpath = dirpath.replace("/", "\\")

            files_folders = dirnames + filenames

            for file_folder in files_folders:
                if file_folder == filename:
                    filedir = dirpath + "\\" + filename
                    shutil.copy(filedir, tdirectory)
                    os.rename(tdirectory + "\\" + filename, tdirectory +
                              "\\" + str(filenum) + newname)
                    filenum += 1


root = tk.Tk()
application = MainApplication(root)
application.mainloop()
