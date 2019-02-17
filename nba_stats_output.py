from bokeh.io import output_file
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("nba_stats.csv")

plt.figure(figsize=(30,20))

p1 = df.loc[(df['EFF'] >= 25.00) & (df['PTS'] >= 25)]['Player']
eff = df.loc[(df['EFF'] >= 25.00) & (df['PTS'] >= 25)]['EFF']

p2 = df.loc[(df['PTS'] >= 25.00) & (df['EFF'] >= 25.00)]['Player']
pts = df.loc[(df['PTS'] >= 25.00) & (df['EFF'] >= 25.00)]['PTS']

plt.plot(p2, pts, label="Points")
plt.title('NBA Scorers Averaging More Than 25PPG and Higher Than 25 Efficiency',fontsize=20)
plt.ylabel('Points', fontsize=20)
plt.xlabel('Players',fontsize=20)

plt.plot(p1, eff, label="Efficiency")
plt.ylabel('Effeciency + Points')

plt.legend(loc='upper right',prop={'size': 20})
plt.rcParams.update({'font.size': 15})
output_file("NBA_Comparison.html")
plt.show()