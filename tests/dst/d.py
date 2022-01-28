
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()

ax = fig.add_subplot(111)
df = pd.read_csv(r'C:\Users\user\OneDrive\Documents\GitHub\pyabaqus\tests\dst\DATA\data.csv')
lines = 0
x, ys = 'TIME', ['CSHEAR1']
for y in ys:
    if y not in df.columns:
        continue
    lines += 1
    ax.plot(df[x], df[y], label=y)
if lines > 0:
    ax.legend()
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_title('')
fig.tight_layout()

plt.show()