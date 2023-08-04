#import libraries
import streamlit as st
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

warnings.filterwarnings("ignore")

df = pd.read_csv("music_genre.csv")
pd.set_option('display.max_columns', None)
# Team 1 Bottom-> top caleb Diego Lucas:

#1 charts -> caleb
#2 charts -> Diego
#3 summary -> Lucas

# team 2 -> Top Relena Kendra
# Inpection / top portion:Relena
# Cleaning: kendra

# Write the code here:
st.title("Popping Pistachios")
st.write("Relena Clark:16")
st.write("Kendra Moon:???")
st.write("Lucas Silver:13")
st.write("Caleb Arndt:14")
st.write("Kayla Moon:???")
st.write("Diego Lopez:???")
st.title("Popular Music Statistics")
st.header("Introduction")
st.write(
  "This dataset contains 50,000 of Spotifys most popular songs, describing their tone, key, creator, and  popularity, as well as other aspects of their composition. We identified and analyzed the relationships between these catagories with the intent of discovering what makes a song successful."
)
st.markdown("""---""")
st.header("Inspection")
st.write("This is Head")
st.write(df.head(6))

st.write("This is Tail")
st.write(df.tail(6))

st.write("This is columns")
st.write(df.columns)

st.write("This is Shape")
st.write(df.shape)

st.write("This is Basic Info")
st.write(df.describe())
st.markdown("""---""")

# Cleaning:
st.header("Cleaning")
st.write(df.isna().sum())
st.write(
  "There are 5 null values in each columns. Data cleaning involves checking for null values and un wanted data columns. After isolating said data, data cleaning involves removing all of said data"
)
# are there any columns you want to drop?

#Instance ID

# Check for null values

# Look at preview file, in EDA, code is like .dropna(inplace = True) also do reset index
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
st.header("There Are no More Null values")
st.write("This is what this looks like with no null values")
st.write(df.isna().sum())
st.header("Post data cleaning head")
st.write(df.head())
st.header("Post cleaning tail")
st.write(df.tail())
st.header("This is Columns After Cleaning")
df.drop("instance_id", axis=1, inplace=True)
st.write(df.columns)
st.write(
  "After cleaning through the data we decided that instance ID was of no use to us so we got rid of it"
)
st.header("This is shape after cleaning")
st.write(df.shape)

#smaller dataframe
df = df.iloc[:1000]

# Visualize, and analyze:
# Hypothesis:  is there a relationship between energy and duration
# code (visualize)
# sns.set(color_codes=True)

#sns.barplot(x="energy", y="duration", data=df)

#sns.barplot(x = 'key', y = 'popularity', data = df)

#sns.barplot(x = "popularity", y = "energy", data = df) -- > Lucas
#hypothesis: I thought that as the energy went up so would the popularity
#visualize
#sumarize: There did not seem to be a relationship between energy and popularity

# summary -> what you find out from the graph

#HYPOTHESIS:c is there a relationship between enery and dancebility? - Kendra
# create a fig
# fig = plt.figure(figsize=(10, 4))

# fig3 = plt.figure(figsize=(10, 4))
# sns.set(style='whitegrid')
# sns.scatterplot(
#   x="energy", y="danceability",
#   data=df).set(title="Relationship Between Energy & Danceability")
# #st.pyplot(fig)
# st.pyplot(fig3)

#Diego is there a relationship between energy and duration?

# fig.show()

#fig = px.scatter(data_frame=df, x="energy", y="duration_ms")
#fig.show()
# fig = plt.figure(figsize=(10, 4))
# sns.lineplot(x="energy", y="duration_ms", data=df)
# st.pyplot(fig)
# print(
#   "Most of the songs seem to have a similar run time. However more of the songs"
# )
# print(
#   "with low energy seem to have a longer rum time. This could be because when the"
# )
# print(
#   "artist could have a hard time maintaining a high energy level for an extended period"
# )
# print(
#   "of time. While the low energy singers are able to maintain a low energy level for"
# )
# print("a longer amount of time.")

#Does the music key affect the song's popularity

# fig = px.scatter(data_frame=df, x='key', y='popularity')
# # fig.show()

print("All the keys seem to have a pretty similar number of songs.")
print("The popularity ratings seem to be similar as well. As far as I")
print("can tell there seems to be no variation in the songs due to the key.")

#Is there a relation ship between the popularity and energy

fig = px.scatter(data_frame=df, x="popularity", y="energy")
# fig.show()

print("All songs in the 80 popular range have a .24 energy at least.")
print("All other energy are under 80. From this I can tell that for a ")
print("song to be popular genarally you need to have a moderate energy level.")
print("All of the songs below .24 are below the 80 popularity range.")
print(
  "However just because you have high energy doesen't guarentee that a song")
print(
  "will be popular. But if you want a popular song a high energy seems to do better than a low energy."
)

st.title("Question 0: Is there a relationship between artist and popularity?")
df_new = df.groupby(
  "artist_name")['popularity'].mean().reset_index().sort_values(
    by="popularity", ascending=False).head(10)

figA = px.bar(df_new, x="artist_name", y="popularity")
st.plotly_chart(figA, use_container_width=True)
st.write(
  "Once artists have a popular song they tend to have more of them since they've established a name"
)

st.title(
  "Question 1: Is There A Relationship Between Popularity and The Songs Duration"
)
figB = px.scatter(df,
                  x="duration_ms",
                  y="popularity",
                  title='Durations Effect on Popularity')
st.plotly_chart(figB, use_container_width=True)
st.write(
  "Longest sond to hit 50pop is 16 minutes, Highest ranking song is about 2.5 minutes, most songs are <= 10.25min, longest song == 80ish mins. Songs do best when they're around 3.5 mins which makes since as that is the industry standard."
)

st.title(
  "Question 2: Is There A Relationship Between Popularity And the Song's Key")

fig = plt.figure(figsize=(10, 4))
sns.lineplot(x="key", y="popularity", data=df)
st.pyplot(fig)
st.write()
st.header(
  "Caleb, My hypothsys is that the music key will not majorly effect the popularity, because the music key is not the main attraction of the song. However I belive that the lower the key the more popular it will be, this assumption is because most people tend to enjoy songs that are in lower keys, and octives. "
)
st.title(
  "Question 3: Is There A Relationship Between Popularity And The Song's Energy"
)

fig = plt.figure(figsize=(10, 4))
sns.lineplot(x="energy", y="popularity", data=df)
st.pyplot(fig)
st.header(
  "Hypothesis: I think that there will be a relationship between popularity, and energy. I believe that the most popular will be right in the middle of the energy, because people seem to like more high energy songs."
)

st.header(
  "Summary: There seems to be no relationship between energy and popularity.")
print("\n\n\n")

st.header(
  "Summary: There seems to be no relationship between energy and popularity")
st.title(
  "Question 4: Is There A Relationship Between Song's Duration And Energy")

figC = plt.figure(figsize=(10, 4))
figC = px.scatter(data_frame=df, x="energy",
                  y="duration_ms", title="Energies Effect on Duration")

st.plotly_chart(figC, use_container_width=True)
st.write(
  "Summary: Most of the songs seem to have a similar run time. However more of the songs"
)
st.write(
  "with low energy seem to have a longer rum time. This could be because when the"
)
st.write(
  "artist could have a hard time maintaining a high energy level for an extended period of time. While the low energy singers are able to maintain a low energy level for a longer amount of time."
)

st.title(
  "Question 5: Is There A Relationship Between The Song's Danceability And Energy"
)
#your code kendra for the chart
st.title("Is there a relationship between duration and popularity")
fig3 = plt.figure(figsize=(10, 4))
sns.set(style='whitegrid')
sns.scatterplot(
  x="energy", y="danceability",
  data=df).set(title="Relationship Between Energy & Danceability")
#st.pyplot(fig)
st.pyplot(fig3)
# write summary of the hyp
st.write("There are fewer songs less than 0.5 energy.")
st.write(
  "For the lower energy songs there is no correlation between energy and danceability, as the data points are scattered across the graph randomely"
)
st.write(
  "For the lower energy songs there is no correlation between energy and danceability, as the data points are scattered across the graph randomely"
)
st.write(
  "Past energy 0.5, a majority of songs danceability started at 0.5 and continued to increase."
)
# st.title(
#   "question 6: Is There A Relationship Between thee Song's Insturmentalness And Artist"
# )
