import os
import xml.etree.ElementTree as Xet
import pandas as pd


file_folder = input("Input folder containing reports: ")

path = os.getcwd()

dir_list = os.listdir(file_folder)

print(dir_list)

#sets up the rows and columns for the csv creation
cols = ["Mass- 7", "Mass- 51", "Mass- 103", "EM Pulse", "EM Analog"]
row = []

#This class takes a file directory as an argument and parses XML files.
class xml_converter():
    def __init__(self, file_di):
        self.file = file_di

#finds and prints the tune reports in the directory
    def find_tune_reports(self):
        try:
            file = file_folder + "\\" + self.file + "\\" + "TuneReport\\BatchTuneReport.xml"
            print(file)

            with open(file, "r") as f:
                xmltext = f.read()

                print(xmltext)

#gets the a list of roots in the XML file
            

#searches for the specified root and gets the text in the root.
            """for rows in root:
                

#appends the found values to list rows

            row.append({

            })"""
            

#hopefully this will immediately runif the line 30 throws an error.
        except:
            print("fail")
            pass
            

#runs the converter class for every file in dir_list
for x in dir_list:
    f = xml_converter(x)
    f.find_tune_reports()

#data = pd.DataFrame(rows, columns=cols)
