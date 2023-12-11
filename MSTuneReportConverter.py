import os
import pandas as pd



file_folder = input("Input folder containing reports: ")

path = os.getcwd()

dir_list = os.listdir(file_folder)

#sets up the rows and columns for the csv creation
cols = ["Date", "Mass- 59", "Mass- 89", "Mass- 205", "Analog V", "Pulse V", "If/B Pressure", "Analyzer Pressure"]
rows = []



#This class takes a file directory as an argument and parses XML files.
class xml_converter():
    def __init__(self, file_di):
        self.file = file_di

    #finds the value and truncates it.
    def format_value(self, x):
        first_index = x.index(">") + 1
        last_index = x.index("</")
        x = x[first_index: last_index]
        return x

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
                        date = self.format_value(date)
                        date = date[0:date.index(".")]
                        date = date.replace("T", " ")
                        break

                for count, ele in xmltext:
                    #finds the first tune element of mass 59
                    if ele.strip() == "<TuneElementID>0</TuneElementID>":
                        #the remaining elements should be spaced consistently, file to file
                        MZ_59 = (tuple((xmltext)[count + 2])[1]).strip()
                        MZ_89 = (tuple((xmltext)[count + 17])[1]).strip()
                        MZ_205 = (tuple((xmltext)[count + 32])[1]).strip()

                        MZ_59 = self.format_value(MZ_59)
                        MZ_89 = self.format_value(MZ_89)
                        MZ_205 = self.format_value(MZ_205)

                        MZ_59 = round(float(MZ_59))
                        MZ_89 = round(float(MZ_89))
                        MZ_205 = round(float(MZ_205))
                        break

                for count, ele in xmltext:
                    #finds the EM pulse and analog values
                    if ele.strip() == "<TuneParamID>47</TuneParamID>":
                        #the remaining elements should be spaced consistently, file to file
                        analog = (tuple((xmltext)[count + 2])[1]).strip()
                        pulse = (tuple((xmltext)[count + 9])[1]).strip()
                        
                        #occasonally the values will have 3 digits and a < character will need to be removed.
                        analog = self.format_value(analog)
                        pulse = self.format_value(pulse)
                        
                        break

                for count, ele in xmltext:
                    #finds the EM pulse and analog values
                    if ele.strip() == "<Name>Vacuum_IfBkPress</Name>":
                        #the remaining elements should be spaced consistently, file to file
                        Vacuum_IfBkPress = (tuple((xmltext)[count + 1])[1]).strip()
                        Vacuum_AnalyzerPress = (tuple((xmltext)[count + 9])[1]).strip()
                        
                        #occasonally the values will have 3 digits and a > character will need to be removed.
                        Vacuum_IfBkPress = self.format_value(Vacuum_IfBkPress)
                        Vacuum_AnalyzerPress = self.format_value(Vacuum_AnalyzerPress)
                        
                        break
    
#appends the found values to list rows

            rows.append({"Date": date,
                         "Mass- 59": MZ_59,
                         "Mass- 89": MZ_89,
                         "Mass- 205": MZ_205,
                         "Analog V": analog,
                         "Pulse V": pulse,
                         "If/B Pressure": Vacuum_IfBkPress,
                         "Analyzer Pressure": Vacuum_AnalyzerPress
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
