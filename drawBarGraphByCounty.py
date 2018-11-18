import readAZ_Data as electionData
import plotly.plotly as py
import plotly.graph_objs as go

barData[]

# plotly.tools.set_credentials_file(username='mart4546', api_key='uH1WNZwq0zjD7IPCJZ1R')

def createBar (voteCounts, countyName):
    cLine = go.Bar(
        y=['Repulican', 'Democrat', 'Green Party'],
        x=[voteCounts[0], voteCounts[1], voteCounts[2]],
        name=countyName,
        orientation = 'h',
        marker = dict(
            color = 'rgba(246, 78, 139, 0.6)',
            line = dict(
                color = 'rgba(246, 78, 139, 1.0)',
                width = 3)
        )
    )

    return cLine

def setupData (counties, repVotes, demVotes, otherPartyVotes):

    voteCount [3]
    ctyCount = 0

    for nextCty in counties:
        voteCount[0] = repVotes [ctyCount]
        voteCount[1] = demVotes[ctyCount]
        voteCount[2] = otherPartyVotes[ctyCount]

        barData[ctyCount] = createBar (voteCount, nextCty)
        ctyCount = ctyCount + 1


def main():
    print "In main"    # Declare lists for plotly
    county = []
    red_cnt = [5,10,15]
    blue_cnt = [10,15,5]
    green_cnt = [15,5,10]

    #  read data and put in lists
    fileName = "Arizona General Election Data for Governor.csv"

 #   electionData.readElectionData (fileName,county,red_cnt,blue_cnt,green_cnt)
    county.append("A")
    county.append("B")
    county.append("C")

    setupData(county, red_cnt, blue_cnt, green_cnt)
    layout = go.Layout(
        barmode='stack'
    )

# add state
    fig = go.Figure(data= barData, layout=layout)
    py.plot(fig, filename='marker-h-bar')

main ()

