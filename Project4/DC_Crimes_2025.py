import csv
import matplotlib.pyplot as plt

csv_path = 'Crime_Incidents_in_2025.csv'

offenses = {}
shifts = {}
daily_crimes = {}

with open(csv_path) as crimes_file:
    crimes_reader = csv.reader(crimes_file)
    next(crimes_reader)
    
    for row in crimes_reader:
        
        offense_type = row[6]
        shift = row[4]
        
        date_time = row[3].split()
        day = date_time[0]

        
        if offense_type in offenses:
            offenses[offense_type] += 1
        else:
            offenses[offense_type] = 1
        
        if shift in shifts:
            shifts[shift] += 1
        else:
            shifts[shift] = 1
        
        if day in daily_crimes:
            daily_crimes[day] += 1
        else:
            daily_crimes[day] = 1

offense_types = []
offense_counts = []

for offense_type in offenses: 
    offense_types.append(offense_type)
    offense_counts.append(offenses[offense_type])

plt.bar(offense_types, offense_counts)
plt.title('Number of Incidents per Offense Type')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=75, fontsize = 6) # X axis overlap with horizontal text: https://stackoverflow.com/questions/50033189/matplotlib-x-axis-overlap
plt.tight_layout() # Text cut off at bottom of graph: https://stackoverflow.com/questions/6774086/how-to-adjust-padding-with-cutoff-or-overlapping-labels
plt.show()

shift_names = []
shift_counts = []

for shift_name in shifts:
    shift_names.append(shift_name)
    shift_counts.append(shifts[shift_name])

plt.pie(shift_counts, labels=shift_names, autopct='%1.0f%%') # How to show percentage on pie chart: https://stackoverflow.com/questions/72166012/getting-percent-sign-to-show-up-in-pie-chart
plt.title('Crime Spread by Time of Day')
plt.show()

days = []
daily_crime_counts = []

sorted_days = sorted(daily_crimes)  

for day in sorted_days:
    days.append(day)  
    daily_crime_counts.append(daily_crimes[day]) 

weekly_ticks = []
for i in range(0, len(days), 7):
    weekly_ticks.append(days[i])

plt.plot(days, daily_crime_counts)
plt.title('Daily Crime Incidents in 2025')
plt.ylabel('Number of Incidents')
plt.xticks(weekly_ticks, rotation = 75, fontsize = 6)
plt.tight_layout()
plt.show()