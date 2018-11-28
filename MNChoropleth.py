# Ellen Friedman
# Python 603-1
# November 2018
# Final Project
#
# MNChropleth.py
#
# Use Plotly to create a choropleth map of the differences between the DFL (blue) votes and the R (red) votes
# for the 2018 governor's race.


import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd

def parseData(DataSets):
    fips = []
    states = []
    r_votes = []
    d_votes = []
    o_votes = []
    county_names = []
    total_votes = []

    for ds in DataSets:
        total_votes += ds['TOTAL_VOTES'].tolist()
        fips += ds['FIPS'].tolist()
        states += ds['STATE'].tolist()
        r_votes += ds['R_VOTES'].tolist()
        d_votes += ds['D_VOTES'].tolist()
        o_votes += ds['O_VOTES'].tolist()
        county_names += ds['COUNTY'].tolist()

    return fips, states, r_votes, d_votes, o_votes, total_votes



def GetVoteDiffs(r_votes, d_votes, total_votes):
    vote_diffs = []
    for i in range(len(total_votes)):
        vote_diffs.append((r_votes[i] / total_votes[i]) - (d_votes[i] / total_votes[i]))

    return vote_diffs


def CreateMap(fips, states, vote_diffs):

    # blue_to_red = [
    #     '#010d85', '#081488', '#101c8c', '#182390', '#202b94', '#283298', '#303a9b', '#38419f', '#4049a3', '#4851a7', '#5058ab',
    #     '#ffffff',
    #     '#e06850',  '#de6148',  '#dd5a40',  '#db5338',  '#da4d30','#d94628',  '#d73f20', '#d63818',  '#d43110',  '#d32a08',  '#d22401']

    blue_to_red = [
        '#010d85', '#252f96', '#4952a7', '#6d74b9',
        '#f8dfda',
        '#e5816d', '#de6249', '#d84325', '#d22401'
    ]


    myMap = ff.create_choropleth(
        fips=fips, values=vote_diffs,
        scope=states,
        county_outline={'color': 'rgb(192,192,192)', 'width': 0.5},
        state_outline={'color': 'rgb(0,0,0)', 'width': 0.5},
        # binning_endpoints=[-.5, -0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0,0.0001,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5],
        binning_endpoints=[-0.3, -0.2,-0.1, 0, 0.1, 0.2, 0.3],
        legend_title='Margin of Difference per County',
        colorscale=blue_to_red)


    myMap['layout']['legend'].update({'x': 0})
    myMap['layout']['annotations'][0].update({'x': .1, 'xanchor': 'left'})
    py.plot(myMap, filename='MN Choropleth')


def main():
    ElectionDataSets = []
    ElectionDataSets.append(pd.read_csv("../../datasets/mn/minnesotaGovernorByCounty.txt"))

    all_Fips, all_States, all_r_votes, all_d_votes, all_o_votes, all_total_votes = parseData( ElectionDataSets)

    vote_diffs = GetVoteDiffs(all_r_votes, all_d_votes, all_total_votes)

    CreateMap(all_Fips, all_States, vote_diffs)



main()