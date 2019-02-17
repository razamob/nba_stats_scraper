# nba_stats_scraper

A web scraper that uses https://stats.nba.com/leaders/ to get stats for the top scorers in the nba. 

All of the stats for all of the categories are scraped. 

The stats are converted into a python dictionary which is then converted to csv file. 

The Points and Efficiency is analyzed using matplotlib to determine the MVP of the NBA so far(Not counting team wins).

Conclusion made that James Harden is the MVP so far, considering points per game and efficiency. 

Future implementation may include storing the data in a sqlite database and using that to visualize the data. 

Data may be visualized using D3 in the future.

The code for the graph is in the nba_stats_output.py file or Nba_Stats.ipynb if using Jupyter. 

CSV contains all the stored data from NBA.com

