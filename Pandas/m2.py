import matplotlib.pyplot as plt
import pandas as pd
header = ['Week 1', 'Week 2', 'Week 3', 'Day']
col = [
    (5000,4000,4000,'Monday'),
    (5900,3000,5800,'Tuesday'),
    (6500,5000,3500,'Wednesday'),
    (3500,5500,2500,'Thursday'),
    (4000,3000,3000,'Friday'),
    (5300,4300,5300,'Saturday'),
    (7900,5900,6000,'Sunday'),
]
plt.plot(header, col)
plt.xlabel('Week')
plt.ylabel('Sales in Rs')
plt.title('Algo')
plt.grid(True)
plt.yticks(col)
plt.show()

# plots a bar chart with the column "Days" as x axis


