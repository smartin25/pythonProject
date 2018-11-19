import readAZ_Data as electionData
import plotly.plotly as py
import plotly.graph_objs as go
import random

barData = []
colorNames = ['AntiqueWhite', 'Aqua','Aquamarine','Azure','Beige','Bisque','Black','BlanchedAlmond','Blue','BlueViolet','Brown',
                   'BurlyWood','CadetBlue','Chartreuse','Chocolate','Coral','CornflowerBlue','Cornsilk','Crimson','Cyan',
                   'DarkBlue','DarkCyan','DarkGoldenRod','DarkGray','DarkGrey','DarkGreen','DarkKhaki','DarkMagenta','DarkOliveGreen',
                   'DarkOrange','DarkOrchid','DarkRed','DarkSalmon','DarkSeaGreen','DarkSlateBlue','DarkSlateGray','DarkSlateGrey',
                   'DarkTurquoise','DarkViolet','DeepPink','DeepSkyBlue','DimGray','DimGrey','DodgerBlue','FireBrick','FloralWhite',
                   'ForestGreen','Fuchsia','Gainsboro','GhostWhite','Gold','GoldenRod','Gray','Grey','Green','GreenYellow','HoneyDew',
                   'HotPink','IndianRed','Indigo','Ivory','Khaki','Lavender','LavenderBlush','LawnGreen','LemonChiffon','LightBlue',
                   'LightCoral','LightCyan','LightGoldenRodYellow','LightGray','LightGrey','LightGreen','LightPink','LightSalmon',
                   'LightSeaGreen','LightSkyBlue','LightSlateGray','LightSlateGrey','LightSteelBlue','LightYellow','Lime','LimeGreen',
                   'Linen','Magenta','Maroon','MediumAquaMarine','MediumBlue','MediumOrchid','MediumPurple','MediumSeaGreen',
                   'MediumSlateBlue','MediumSpringGreen','MediumTurquoise','MediumVioletRed','MidnightBlue','MintCream','MistyRose',
                   'Moccasin','NavajoWhite','Navy','OldLace','Olive','OliveDrab','Orange','OrangeRed','Orchid','PaleGoldenRod','PaleGreen',
                   'PaleTurquoise','PaleVioletRed','PapayaWhip','PeachPuff','Peru','Pink','Plum','PowderBlue','Purple','RebeccaPurple',
                   'Red','RosyBrown','RoyalBlue','SaddleBrown','Salmon','SandyBrown','SeaGreen','SeaShell','Sienna','Silver','SkyBlue',
                   'SlateBlue','SlateGray','SlateGrey','Snow','SpringGreen','SteelBlue','Tan','Teal','Thistle','Tomato','Turquoise',
                   'Violet','Wheat','White','WhiteSmoke','Yellow','YellowGreen']

# plotly.tools.set_credentials_file(username='mart4546', api_key='uH1WNZwq0zjD7IPCJZ1R')

def createBar (voteCounts, countyName, countyColor):

    cLine = go.Bar(
        y=['Repulican', 'Democrat', 'Other'],
        x=[voteCounts[0], voteCounts[1], voteCounts[2]],
        name=countyName,
        orientation = 'h',
        marker = dict(
            color = [countyColor,countyColor,countyColor],
            line = dict(
                color = 'rgba(0, 0, 0, 1.0)',
                width = 3)
        )
    )

    return cLine

def randomColorGenerator ():

    colorNum = random.randint(0, 146)
    return colorNames[colorNum]



def setupData (counties, repVotes, demVotes, otherPartyVotes):

    voteCount = [1,2,2]
    ctyCount = 0

    for nextCty in counties:
        voteCount[0] = repVotes[ctyCount]
        voteCount[1] = demVotes[ctyCount]
        voteCount[2] = otherPartyVotes[ctyCount]

        getColor = randomColorGenerator()
        barData.append(createBar (voteCount, counties[ctyCount], getColor))
        ctyCount = ctyCount + 1                                 

def main():
    print "In main"    # Declare lists for plotly
    county = []
    red_cnt = []
    blue_cnt = []
    green_cnt = []

    #  read data and put in lists
    fileName = "Arizona General Election Data for Governor.csv"

    electionData.readElectionData (fileName,county,red_cnt,blue_cnt,green_cnt)

    setupData(county, red_cnt, blue_cnt, green_cnt)
    layout = go.Layout(
        barmode='stack'
    )

# add state
    fig = go.Figure(data= barData, layout=layout)
    py.plot(fig, filename='marker-h-bar')

main ()

