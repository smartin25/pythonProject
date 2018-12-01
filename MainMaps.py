# Ellen Friedman
# Python 603-1
# November 2018
# Final Project
#
# MainMaps.py

# Starting point for the creating maps from results of Governor's 2018 races in AZ, CO, MN

import AZTranform
import MNTransform
import COTransform

import MNChoropleth
import AllChoropleth

import pandas as pd

def main():
    # create a variable for each pair of files

    # Arizona files
    azIn = "../datasets/az/Arizona General Election Data for Governor.csv"
    azOut = "../datasets/az/ArizonaGovernorByCounty.txt"

    # Colorado files
    coIn = "../datasets/co/cgged.csv"
    coOut =  "../datasets/co/ColoradoGovernorByCounty.txt"

    # Minnesota files
    mnIn = "../datasets/mn/MinnesotaGovernorByPrecinct.txt"
    mnOut = "../datasets/mn/MinnesotaGovernorByCounty.txt"

    # Transform each file
    AZTranform.Transform(azIn, azOut)
    COTransform.Transform(coIn, coOut)
    MNTransform.Transform(mnIn, mnOut)

    # Create a plotly choropleth map of Minnesota
    MNChoropleth.main(mnOut)

    # Create a plotly choropleth map of AZ, CO and MN superimposed on the USA
    ElectionDataSets = []
    ElectionDataSets.append(pd.read_csv("../datasets/mn/MinnesotaGovernorByCounty.txt"))
    ElectionDataSets.append(pd.read_csv("../datasets/az/ArizonaGovernorByCounty.txt"))
    ElectionDataSets.append(pd.read_csv("../datasets/co/ColoradoGovernorByCounty.txt"))

    AllChoropleth.main(ElectionDataSets)

main()