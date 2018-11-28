# Ellen Friedman
# Python 603-1
# November 2018
# Final Project
#
# COTransform.py

# Transform the results of the CO 2018 Governor's race from:
# State,County ID,Precinct name,Office ID,Office Name,District,Candidate Order Code,Candidate Name,Suffix,Incumbent Code,Party Abbreviation,Number of Precincts reporting,Total number of precincts voting for the office,Votes for Candidate,Percentage of Votes for Candidate out of Total Votes for Office,Total number of votes for Office in area
# to:
# FIPS,ST,COUNTYNAME,TOTAL_VOTES,R_VOTES,D_VOTES,O_VOTES
#
# The resulting file is input to AllCoropleth.py

def Transform(inF, outF):


    CountyFipsLookup = InitializeCountyFips()

    # todo change this to WITH filename
    theFile = open(inF)
    outFile = open(outF, "w")

    outLine = []
    outLines = []

    aLine = theFile.readline()
    while aLine:
        # Create a dictionary with FIPS, State, County Name, Total Votes,  Party Votes
        items = aLine.split(",")
        if CountyFipsLookup.get(items[0]):
            outLine.append(CountyFipsLookup.get(items[0])) #County Fips
            outLine.append('Colorado')
            outLine.append(items[0])   # County Name
            outLine.append(str(int(items[4]) + int(items[2]) + int(items[6]) + int(items[8])))  # all votes
            outLine.append(items[4])   # r votes
            outLine.append(items[2])   # d votes
            outLine.append(str(int(items[6]) + int(items[8])))    # o votes
            outLines.append(outLine)
        outLine = []
        aLine = theFile.readline()

    print(outLines)

    outFile.write('FIPS,STATE,COUNTY,TOTAL_VOTES,R_VOTES,D_VOTES,O_VOTES' + '\n')
    for line in outLines:
        outString = ','.join([str(x) for x in line])
        outFile.write(outString + '\n')


    # outFile.write('FIPS,STATE,COUNTY,TOTAL_VOTES,R_VOTES,D_VOTES,O_VOTES' + '\n')
    # for line in lines:
    #     outString = ','.join([str(x) for x in line])
    #     outFile.write(outString + '\n')

def InitializeCountyFips():


    CountyNames = ['Adams', 'Alamosa', 'Arapahoe', 'Archuleta', 'Baca', 'Bent', 'Boulder', 'Chaffee', 'Cheyenne',
    'Clear Creek', 'Conejos', 'Costilla', 'Crowley', 'Custer', 'Delta', 'Denver', 'Dolores', 'Douglas', 'Eagle',
    'Elbert', 'El Paso', 'Fremont', 'Garfield', 'Gilpin', 'Grand', 'Gunnison', 'Hinsdale', 'Huerfano', 'Jackson',
    'Jefferson', 'Kiowa', 'Kit Carson', 'Lake', 'La Plata', 'Larimer', 'Las Animas', 'Lincoln', 'Logan',
    'Mesa', 'Mineral', 'Moffat', 'Montezuma', 'Montrose', 'Morgan', 'Otero', 'Ouray', 'Park', 'Phillips',
    'Pitkin', 'Prowers', 'Pueblo', 'Rio Blanco', 'Rio Grande', 'Routt', 'Saguache', 'San Juan', 'San Miguel',
    'Sedgwick', 'Summit', 'Teller', 'Washington', 'Weld', 'Yuma']

    CountyIDs = [ '08001',  '08003',  '08005',  '08007',  '08009',  '08011',  '08013',  '08015',  '08017',  '08019',  '08021',  '08023',  '08025',
                 '08027',  '08029',  '08031',  '08033',  '08035',  '08037',  '08039',  '08041',  '08043',  '08045',  '08047',  '08049',  '08051',
                 '08053',  '08055',  '08057',  '08059',  '08061',  '08063',  '08065',  '08067',  '08069',  '08071',  '08073',  '08075',  '08077',
                 '08079',  '08081',  '08083',  '08085',  '08087',  '08089',  '08091',  '08093',  '08095',  '08097',  '08099',  '08101',  '08103',
                 '08105',  '08107',  '08109',  '08111',  '08113',  '08115',  '08117',  '08119',  '08121',  '08123',  '08125']
    
    return dict(zip(CountyNames, CountyIDs))


if __name__ == "__main__":

    Transform("../../datasets/co/cgged.csv",
              "../../datasets/co/ColoradoGovernorByCounty.txt" )