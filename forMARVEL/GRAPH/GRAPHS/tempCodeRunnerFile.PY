import pandas as pd
import matplotlib.pyplot as plt

# dataset credits  UVCE-TPO
data = {
    'Branch': ['CSE', 'CIVIL', 'ECE', 'EEE', 'ISE', 'MECH'],
    'Intake': [87, 142, 66, 88, 66, 110],
    '% Placed': [94, 11, 81, 45, 92, 50], 
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Plot 1: Line graph for Intake (though the data is constant, this will show a flat line)
plt.plot(df['Branch'], df['Intake'], marker='o', color='black')
plt.title('UVCE Placement Statics (2019-2020) Intake Over the Branch')
plt.xlabel('Branch')
plt.ylabel('Intake')
plt.xticks(rotation=45)
plt.show()

# Plot 2: Bar graph for % Placed
plt.bar(df['Branch'], df['% Placed'], color='black')
plt.title('UVCE Placement Statics (2019-2020) % Placed Over the Branch')
plt.xlabel('Branch')
plt.ylabel('% Placed')
plt.xticks(rotation=45)
plt.show()

# Plot 3: Scatter plot for Intake vs % Placed
plt.scatter(df['Intake'], df['% Placed'], color='black')
plt.title('UVCE Placement Statics (2019-2020) Intake vs % Placed')
plt.xlabel('Intake')
plt.ylabel('% Placed')
plt.show()
