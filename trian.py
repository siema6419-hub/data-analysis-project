import pandas as pd
import matplotlib.pyplot as plt

data = {
    "month": [1,2,3,4,5],
    "sales": [100,150,120,180,200]
}

df = pd.DataFrame(data)

print(df.describe())

df.plot(
    x="month",
    y="sales",
    kind="line",
    marker="o",
    figsize=(8,5),
    title="Monthly Sales Analysis"
)

plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.show()