# Election_Analysis

## Project Overview
A Colorado board of Elections employee has fiven you the following task to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of Candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: Election_results.csv
- Software: Python 3.7.6

## Summary
The analysis of the election show that:
-There were 369.711 votes cast in the election.
-candidates weres:
  - Charles Casper Stockham
  - Diana DeGette
  - Anthony Doane
- The Candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  
## Challenge OverView
For this challenge we were to go through the same data used in the election data for the above candidates and find out which county in the region had the highest turn out and which how many votes were cast in each county. To do this I followed very similar steps used to determine the analysis for each candidate. 
## Challenge Summary
Analysis of each county shows that:
- Counties were:
  - Jefferson
  - Denver
  - Arapahoe
- the county results were:
  - Jefferson had 10.5% of the votes cast with a number of 38,855 votes cast
  - Denver had 82.8% of the votes cast with a number of 306,055 votes cast
  - Arapahoe had 6.7% of the votes cast with a number of 24,801 votes cast
- the county with the highest voter turn out was:
  - Denver with 82.8% of votes cast with a number of 306,055 votes cast

## Election-Audit Summary
The script is highly versatile and can be modified to be used in pretty much any election in the state. Given that the data is read into the script has the same formatting as the data used it be used in presidential elections, mayor elections, the list continues. However, if there was ever a need to modify it to show more data that is completely possible with a few tweaks. For example, we could increase the accuracy of the percentages in a close race to show just how close two candidates were. If necessary, counties could be broken down even further to get to a township level to show which townships/city limits voted for which candidate. (Please note that not all states have townships however most states do break down into a lower tier after county.) Also, potentially if location where ballot was cast was provided, we could determine which polling locations receive the most traffic. There are many possibilities as to what can be done with this script with the correct data and a few minor tweaks. 
