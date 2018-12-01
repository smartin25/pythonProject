# Ellen Friedman
# Python 603-1
# November 2018
# Final Project
#
# MNTranform.py
#




# Transform the results of the MN 2018 Governor's race from:
# State,County ID,Precinct name,Office ID,Office Name,District,Candidate Order Code,Candidate Name,Suffix,Incumbent Code,Party Abbreviation,Number of Precincts reporting,Total number of precincts voting for the office,Votes for Candidate,Percentage of Votes for Candidate out of Total Votes for Office,Total number of votes for Office in area
# to:
# FIPS,ST,COUNTYNAME,TOTAL_VOTES,R_VOTES,D_VOTES,O_VOTES
#
# The resulting file is input to MNChoropleth.py and AllChoropleth.py

def Transform(inF, outF):


    CountyNameLookup = InitializeCountyNames()
    CountyFipsLookup = InitializeCountyFips()

    with open(inF) as theFile:

        Precincts = []

        aLine = theFile.readline()
        while aLine:
            # Create a dictionary with FIPS, State, County Name, Total Votes,  Party Votes
            items = aLine.split(";")
            outD = {}
            outD['FIPS'] = CountyFipsLookup[items[1]] # County ID
            outD['State'] = 'Minnesota'  # Hardcode -> State
            outD['CountyName'] = CountyNameLookup[items[1]] # County ID
            outD['TotalVotes'] = int(items[15].strip()) #Total number of votes for Office in area
            outD['Party'] = items[10] # Party Abbreviation
            outD['PartyVotes'] = int(items[13])
            Precincts.append(outD)
            aLine = theFile.readline()

    # Each county has many precincts. We want to collapse the file down to one line per county.
    lines = CollapsePrecincts(Precincts)

    with open(outF, "w") as outFile:
        outFile.write('FIPS,STATE,COUNTY,TOTAL_VOTES,R_VOTES,D_VOTES,O_VOTES' + '\n')
        for line in lines:
            outString = ','.join([str(x) for x in line])
            outFile.write(outString + '\n')

    # theFile.close()
    # outFile.close()

def CollapsePrecincts(Precincts):
    # a collection of precincts sorted by county, precinct.
    # Collapse each precinct into its county and sum the votes.

    currentCountyName = ""
    dataLines = []
    dataLine = []

    for precinct in Precincts:
        if precinct['CountyName'] == currentCountyName:
            if precinct['Party'] == 'R':
                dataLine[4] += precinct['PartyVotes']
            elif precinct['Party'] == 'DFL':
                dataLine[5] += precinct['PartyVotes']
            else:
                dataLine[6] += precinct['PartyVotes']

        else:
            # new County starts
            # re-initialize current dataline
            if len(dataLine) > 0:
                dataLine[3] = dataLine[4] + dataLine[5] + dataLine[6] # total votes
                dataLines.append(dataLine)
                dataLine = []
            currentCountyName = precinct['CountyName']
            dataLine.append(precinct['FIPS'])
            dataLine.append(precinct['State'])
            dataLine.append(precinct['CountyName'])
            dataLine.append(0) #Total votes are calculated at end of county.
            if precinct['Party'] == 'R':
                dataLine.append(precinct['PartyVotes'])
            else:
                dataLine.append(0)
            if precinct['Party'] == 'DFL':
                dataLine.append(precinct['PartyVotes'])
            else:
                dataLine.append(0)
            if  precinct['Party'] != 'R' and precinct['Party'] != 'DFL':
                dataLine.append(precinct['PartyVotes'])
            else:
                dataLine.append(0)

    if len(dataLine) > 0:
        dataLine[3] = dataLine[4] + dataLine[5] + dataLine[6]
        dataLines.append(dataLine)
    return dataLines

def InitializeCountyNames():
    CountyIDs = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
             "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36",
             "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54",
             "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72",
             "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87"]

    CountyNames = ["Aitkin", "Anoka", "Becker", "Beltrami", "Benton", "Big Stone", "Blue Earth", "Brown", "Carlton",
                   "Carver", "Cass", "Chippewa", "Chisago", "Clay", "Clearwater", "Cook", "Cottonwood", "Crow Wing",
                   "Dakota", "Dodge", "Douglas", "Faribault", "Fillmore", "Freeborn", "Goodhue", "Grant", "Hennepin",
                   "Houston", "Hubbard", "Isanti", "Itasca", "Jackson", "Kanabec", "Kandiyohi", "Kittson",
                   "Koochiching", "Lac Qui Parle", "Lake", "Lake Of The Woods", "Le Sueur", "Lincoln", "Lyon", "Mcleod",
                   "Mahnomen", "Marshall", "Martin", "Meeker", "Mille Lacs", "Morrison", "Mower", "Murray", "Nicollet",
                   "Nobles", "Norman", "Olmsted", "Otter Tail", "Pennington", "Pine", "Pipestone", "Polk", "Pope",
                   "Ramsey", "Red Lake", "Redwood", "Renville", "Rice", "Rock", "Roseau", "St. Louis", "Scott",
                   "Sherburne", "Sibley", "Stearns", "Steele", "Stevens", "Swift", "Todd", "Traverse", "Wabasha",
                   "Wadena", "Waseca", "Washington", "Watonwan", "Wilkin", "Winona", "Wright", "Yellow Medicine"]
    return dict(zip(CountyIDs, CountyNames))



def InitializeCountyFips():

    CountyIDs = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
             "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36",
             "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54",
             "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72",
             "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87"]



    CountyFips =  ["27001","27003","27005","27007","27009","27011","27013","27015","27017","27019","27021","27023",
                       "27025","27027","27029","27031","27033","27035","27037","27039","27041","27043","27045","27047",
                       "27049","27051","27053","27055","27057","27059","27061","27063","27065","27067","27069","27071",
                       "27073","27075","27077","27079","27081","27083","27085","27087","27089","27091","27093","27095",
                       "27097","27099","27101","27103","27105","27107","27109","27111","27113","27115","27117","27119",
                       "27121","27123","27125","27127","27129","27131","27133","27135","27137","27139","27141","27143",
                       "27145","27147","27149","27151","27153","27155","27157","27159","27161","27163","27165","27167",
                       "27169","27171","27173"]

    return dict(zip(CountyIDs, CountyFips))


CountyNameLookup = {}
CountyFipsLookup = {}

if __name__ == "__main__":

    Transform("../datasets/mn/minnesotaGovernorByPrecinct.txt",
              "../datasets/mn/minnesotaGovernorByCounty.txt" )

