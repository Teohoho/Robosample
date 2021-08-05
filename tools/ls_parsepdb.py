import os, sys

## Class which reads a pdb file and parses the text into a 
## list of lists of strings
class ParsePdb:
    def __init__(self):
        self.inF = None
        self.parsed_data = []
        self.lines = []
    #

    # Parses text
    def Read(self, inFN):
        self.inF = None
        self.parsed_data = []
        self.inF = open(inFN, "r")
        all_lines = self.inF.readlines()

        j = -1
        for i in range(len(all_lines)):
            line = all_lines[i].rstrip('\n')
            if len(line) > 0:
                j = j + 1
                self.lines.append(line)
                self.parsed_data.append([])
                self.parsed_data[j] = {}
                self.parsed_data[j]["record"] = self.lines[j][0:6]
                if self.parsed_data[j]["record"] in ["ATOM  ", "HETATM"]:
                    self.parsed_data[j]["serial"] = int(self.lines[j][6:11])
                    self.parsed_data[j]["name"] = self.lines[j][12:16]
                    self.parsed_data[j]["resName"] = self.lines[j][17:20]
                    self.parsed_data[j]["chain"] = self.lines[j][21]
                    self.parsed_data[j]["resNo"] = int(self.lines[j][22:26])
                    self.parsed_data[j]["alt"] = self.lines[j][26]
                    self.parsed_data[j]["x"] = float(self.lines[j][30:38])
                    self.parsed_data[j]["y"] = float(self.lines[j][38:46])
                    self.parsed_data[j]["z"] = float(self.lines[j][46:54])
                    self.parsed_data[j]["occ"] = float(self.lines[j][56:60])
                    self.parsed_data[j]["beta"] = float(self.lines[j][60:66])
                    self.parsed_data[j]["element"] = self.lines[j][76:78]
                else:
                    self.parsed_data[j]["rest"] = self.lines[j][6:80]

        self.inF.close()
    #

    # Dump parsed data
    def Dump(self):
        print (self.parsed_data)
    #

    def PrintPdb(self):
        j = -1
        for pd in self.parsed_data:
            j = j + 1
            if pd["record"] in ["ATOM  ", "HETATM"]:
                print ("%6s%5d %4s %3s %c%4d%c   %8.3f%8.3f%8.3f  %4.2f%6.2f          %2s" % (
                      pd["record"]
                    , pd["serial"]
                    , pd["name"]
                    , pd["resName"]
                    , pd["chain"]
                    , pd["resNo"]
                    , pd["alt"]
                    , pd["x"]
                    , pd["y"]
                    , pd["z"]
                    , pd["occ"]
                    , pd["beta"]
                    , pd["element"]))
            else:
                print ("%s%s" % (pd["record"], pd["rest"]))
            
    #

#





