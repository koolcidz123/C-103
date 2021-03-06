#DONT RUN THEM TOGETHER
#RUN EACH OF THEM SEPARATELY


#LINE GRAPH:-
import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("line_chart.csv")
fig = px.line(df, x="Year", y="Per capita income", color="Country", title="Per Capitals income")
fig.show()


#BAR GRAPH :-
import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.bar(df,x="Country", y="InternetUsers", color="Country")
fig.show()


#SCATTER GRAPH:-
import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Population", y="Per capita", size="Percentage", color="Country", size_max=60 )
fig.show()