# Election Analysis

## Overview of Project

### Background and Purpose

Tom, a Colorado Board of Elections employee, needs help with an election audit of the tabulated results for a US Congressional precinct in Colorado. Tom is requesting help with the following tasks:

1. Calculating the total number of votes cast.
2. Retrieving a complete list of candidates who received votes.
3. Calculating the total number of votes each candidate received.
4. Calculating the percentage of votes each candidate won.
5. Determining the winner of the election based on popular vote.
6. Calculating the voter turnout for each county.
7. Calculating the percentage of votes from each county.
8. Determining the county with the largest turnout.

### Resources

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.68.1

## Results

The analysis of the election shows that:
- There were 369,711 total votes cast in the election.
- The county results were:
    - Jefferson county provided 10.5% of the vote with 38,855 votes.
    - Denver county provided 82.8% of the vote with 306,055 votes.
    - Arapahoe county provided 6.7% of the vote with 24,801 votes.
- The county with the largest number of votes was:
    - Denver county, which provided 82.8% of the vote with 306,055 votes.
- The candidate results were:
    - Charles Casper Stockham received 23% of the vote with 85,213 votes.
    - Diana DeGette received 73.8% of the vote with 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote with 272,892 votes.

![Text_File](https://user-images.githubusercontent.com/106830513/176824457-ff0ccf87-de4b-4944-896e-255e516c7d01.png)

## Summary

This scipt was created with the idea in mind that it could be used to audit not only other Congressional districts, but also Senatorial districts and local elections. There are several easy modifications to be able to use this script for another election. One way the script can be modified is by substituting another variable for the counties, such as states, cities, or school districts. Another modification would be if there were additional breakdowns in the results to be determined, such as affiliation or demographics. Part of the script can be copied and pasted with slight edits to add such results, which can also be printed to both the terminal and output text file.
