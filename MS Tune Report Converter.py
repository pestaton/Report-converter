import os
import pandas as pd

file_folder = input("Input folder containing reports: ")

path = os.getcwd()

dir_list = os.listdir(file_folder)

#sets up the rows and columns for the csv creation
cols = ["Date", "Mass- 59", "Mass- 89", "Mass- 205", "Analog V", "Pulse V"]
rows = []

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
                xmltext = list(enumerate(f))

                for count, ele in xmltext:
                    #finds the first tune report and the date/time should be 3 rows down
                    if ele.strip() == "<ReportSetID>0</ReportSetID>":
                        date = (tuple((xmltext)[count + 3])[1]).strip()
                        date = date[9:28]
                        date = date.replace("T", " ")
                        break

                for count, ele in xmltext:
                    #finds the first tune element of mass 59
                    if ele.strip() == "<TuneElementID>0</TuneElementID>":
                        #the remaining elements should be spaced consistently, file to file
                        MZ_59 = (tuple((xmltext)[count + 2])[1]).strip()
                        MZ_89 = (tuple((xmltext)[count + 17])[1]).strip()
                        MZ_205 = (tuple((xmltext)[count + 32])[1]).strip()


                        MZ_59 = MZ_59[7:15]
                        MZ_89 = MZ_89[7:15]
                        MZ_205 = MZ_205[7:15]
                        break

                for count, ele in xmltext:
                    #finds the EM pulse and analog values
                    if ele.strip() == "<TuneParamID>47</TuneParamID>":
                        #the remaining elements should be spaced consistently, file to file
                        analog = (tuple((xmltext)[count + 2])[1]).strip()
                        pulse = (tuple((xmltext)[count + 9])[1]).strip()
                        


                        analog = analog[126:130].strip(">")
                        pulse = pulse[126:130].strip(">")
                        
                        break
    
#appends the found values to list rows

            rows.append({"Date": date,
                         "Mass- 59": MZ_59,
                         "Mass- 89": MZ_89,
                         "Mass- 205": MZ_205,
                         "Analog V": analog,
                         "Pulse V": pulse
            })
            print(rows)

#hopefully this will immediately runif the line 21 throws an error. Typically this means the file had no tune report.
        except:
            print("FAILED: No tune report found in folder: " + file_folder + "\\" + self.file)
            pass
            

#runs the converter class for every file in dir_list
for x in dir_list:
    f = xml_converter(x)
    f.find_tune_reports()

data = pd.DataFrame(rows, columns=cols)
data.to_csv('output.csv')
