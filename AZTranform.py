# Ellen Friedman
# Python 603-1
# November 2018
# Final Project
#
# AZTransform.py

# Transform the results of the AZ 2018 Governor's race from:
# County name, Precincts reporting, fips, ducey, garcia, torres, total
# to:
# FIPS,STATE,COUNTY,TOTAL_VOTES,R_VOTES,D_VOTES,O_VOTES
#
# The resulting file is input to AllCoropleth.py

from csv import reader


def Transform(inF, outF):
    outLine = []
    outLines = []

    countyNamePos = 0
    fipsPos = 2
    rPos = 3
    dPos = 4
    gPos  = 5
    allPos = 6

    fipsPrefix = '04'

    with open(inF) as theFile:
        next(theFile)   # skip the first line of the input file
        for aLine in reader(theFile):
            outLine.append(fipsPrefix + aLine[fipsPos])
            outLine.append('Arizona')
            outLine.append(aLine[countyNamePos])  # County Name
            outLine.append(aLine[allPos].replace(",",""))  # all votes
            outLine.append(aLine[rPos].replace(",",""))  # r votes
            outLine.append(aLine[dPos].replace(",",""))  # d votes
            outLine.append(aLine[gPos].replace(",",""))  # o votes
            outLines.append(outLine)
            outLine = []


    with open(outF, "w") as outFile:
        outFile.write('FIPS,STATE,COUNTY,TOTAL_VOTES,R_VOTES,D_VOTES,O_VOTES' + '\n')
        for line in outLines:
            outString = ','.join([str(x) for x in line])
            outFile.write(outString + '\n')


if __name__ == "__main__":
    Transform("../datasets/az/Arizona General Election Data for Governor.csv",
              "../datasets/az/ArizonaGovernorByCounty.txt")