import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("projectdata.csv")

toefl_score = df["TOEFL Score"].tolist()
weight = df["GRE Score"].tolist()

fig=px.scatter(x=toefl_score,y=weight)
# fig.show()

# y = mx + c
# m = slope
# c = intercept on y axis
#x = values of x

m = 0.95
c = -93
y = []
for x in toefl_score:
    y_value=m*x + c
    y.append(y_value)

fig=px.scatter(x=toefl_score,y=weight)
fig.update_layout(shapes=[
    dict(
        type='line',
        y0=min(y) ,       y1 =max(y),
        x0 =min(toefl_score) , x1 =max(toefl_score)
    )
])
#fig.show()

x =250
y = m*x + c
print(f"weight of someone with height {x} is {y}")


height_array = np.array(toefl_score)
weight_array = np.array(weight)

m,c = np.polyfit(height_array,weight_array,1)

y = []
for x in height_array:
    y_value=m*x + c
    y.append(y_value)

fig=px.scatter(x=height_array,y=weight_array)
fig.update_layout(shapes=[
    dict(
        type='line',
        y0=min(y) ,y1 =max(y),
        x0 =min(height_array) , x1 =max(height_array)
    )
])
fig.show()

x =250
y = m*x + c
print(f"weight of someone with height {x} is {y}")