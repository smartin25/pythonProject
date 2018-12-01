#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


# In[59]:


def mnData(df):
    '''
     :param df: a DataFrame of Minnesota election data
    '''
    #pick up information of counties in Minnesota
    counties = list(df['COUNTY'])
    
    #pick up information of parties in Minnesota and change it into list type
    is_parties = list(map(lambda x: np.array(df[x]).tolist(), df[['R_VOTES', 'D_VOTES', 'O_VOTES']]))
    
    #set bar colors
    colors = ['rgb(255, 204, 242)', 'rgb(255, 128, 223)', 'rgb(255, 0, 191)']
    return is_parties, counties, colors


# In[60]:


def coData(df):   
    '''
     :param df: a DataFrame of Colorado election data
    '''
    #Delete duplicate information rows
    df = df.drop(['Total Votes', 'Total Votes.2', 'Total Votes.4', 'Total Votes.6'],1) 
    
    #rename party information   
    df_clear = df[:-1].rename({'Total Votes.1':'Dem', 'Total Votes.3':'Rep', 'Total Votes.5': 'Unt', 'Total Votes.7':'Lib'}, axis = 'columns')
    
    #incorporate Lib and Unt parties election result into Other parties
    df_clear['Other Parties'] = df_clear[['Unt','Lib']].apply(np.sum, axis = 1)
    counties = list(df_clear['County'][:-1])
    
    #set bar chart colors
    colors = ['rgb(255, 242, 230)', 'rgb(255, 204, 153)','rgb(255, 166, 77)']
    
    #pick up parties information
    parties_election = df_clear[['Rep', 'Dem', 'Other Parties']]
    parties_election_np = list(map(lambda x: np.array(df_clear[x]).tolist(),parties_election.columns))
    return parties_election_np, counties, colors


# In[61]:


def azData(df):
    #pick up counties information
    counties = list(df['COUNTY'])
    
    #pick up parties information and change it into list type
    parties = list(map(lambda x: np.array(df[x]).tolist(), df.columns[3:-1]))
    
    #delete comma in the numbers
    new_parties = []
    for party in parties:
        new_parties.append(list(map(lambda x: int(''.join(x.split(','))), party)))
    colors = ['rgb(255, 247, 230)', 'rgb(255, 215, 128)', 'rgb(255, 174, 0)']
    return new_parties, counties, colors


# In[62]:


def draw_bar(parties_election, counties, colors, title):
    '''
    :param parties_election: a two-dimension list of parties' election results
    :param counties: a list of counties\
    :param colors: the colors of diffetent parties
    :return:  a bar chart
    '''
    parties = ['Replican', 'Democrat', 'Other parties']

    #use go.Bar to establish three traces and add them to data
    data = [go.Bar(x = counties, y = party_election, name = party, marker = dict(color = color)) for party_election, party, color in zip(parties_election, parties, colors)]
    
    #set layout
    layout = go.Layout(
        title= title,
        xaxis = dict(tickangle = 45),
        barmode = 'group'
    )
    
    #add fig
    fig = go.Figure(data = data, 
                    layout = layout)

    # add state
    py.plot(fig)    


# In[63]:


def main():
    #read csv files
    MN = pd.read_csv('minnesotaGovernorByCounty.txt')
    AZ = pd.read_csv('Arizona General Election Data for Governor.csv')
    CO = pd.read_csv('CGGED.csv', header = 2)
    
    #change them into DataFrame structure
    MN_df = pd.DataFrame(MN)
    AZ_df = pd.DataFrame(AZ)
    CO_df = pd.DataFrame(CO)
    
    
    #clean data 
    CO_elections, CO_counties, CO_colors = coData(CO_df)
    MN_elections, MN_counties, MN_colors = mnData(MN_df)
    AZ_elections, AZ_counties, AZ_colors = azData(AZ_df)
    
    #draw vertical bar chart
    draw_bar(CO_elections, CO_counties, CO_colors, 'Colorado Counties Election Vertical Bar Chart')
    draw_bar(MN_elections, MN_counties, MN_colors, 'Minnesota Counties Election Vertical Bar Chart')
    draw_bar(AZ_elections, AZ_counties, AZ_colors, 'Arizona Counties Election Vertical Bar Chart')
    
main()

