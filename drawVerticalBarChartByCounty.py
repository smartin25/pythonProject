import plotly.plotly as py
import plotly.graph_objs as go

def draw_bar(parties_election, counties, colors):
    '''

    :param parties_election: a two-dimension list of parties' election results
    :param counties: a list of counties\
    :param colors: the colors of diffetent parties
    :return:  a bar chart
    '''
    parties = ['Democrat', 'Replican', 'Other parties']

    # use go.Bar to establish three traces and add them to data
    data = [go.Bar(x = counties, y = party_election, name = party, marker = dict(color = color)) for party_election, party, color in zip(parties_election, parties, colors)]

    layout = go.Layout(
        xaxis = dict(tickangle = 45),
        barmode = 'group'
    )
    fig = go.Figure(data = data, #add fig
                    layout = layout)

    # add state
    py.plot(fig, filename = 'marker-v-bar')