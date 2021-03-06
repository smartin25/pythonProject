from csv import reader

# Open the Excel file with the governor
AZGovDataFile = open("Arizona General Election Data for Governor.csv", 'r')

# Line Count to skip the header line
lineCount = 1

county = []
red_cnt = []
blue_cnt = []
green_cnt = []

# Column Positions in the file
ctyNamePos = 0
RepulicanPos = 3
DemocratPos = 4
GreenPartyPos = 5

# Loop through rows
for aline in reader(AZGovDataFile):

    if lineCount <> 1:
        county.append(aline[ctyNamePos])
        red_cnt.append(aline[RepulicanPos])
        blue_cnt.append(aline[DemocratPos])
        green_cnt.append(aline[GreenPartyPos])

    lineCount = lineCount + 1

print(county)
print(red_cnt)
print(blue_cnt)
print(green_cnt)
AZGovDataFile.close()