import os
import xml.etree.ElementTree as Xet


file_folder = input("Input folder containing reports: ")

path = os.getcwd()

dir_list = os.listdir(file_folder)

print(dir_list)


class converter():
    def __init__(self, file_di):
        self.file = file_di

#finds and prints the tune reports in the directory
    def find_tune_reports(self):
        try:
            file = file_folder + "\\" + self.file + "\\" + "TuneReport\BatchTuneReport.xml"
            print(file)

            with open(file, "r") as f:
                content = f.read()
                print(content)
        except:
            print("fail")
            pass
            


for x in dir_list:
    f = converter(x)
    f.find_tune_reports()