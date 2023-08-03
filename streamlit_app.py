#import libraries
import streamlit as st
import pandas as pd
import warnings
import plotly.express as px
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

warnings.filterwarnings("ignore")

df = pd.read_csv("Netflix Userbase.csv")

# Inspection:

st.title("Monarch Mammoths")
st.write("Chantelle Ho: Lives in Bay Area, 13")
st.title("Netflix Userbase Dataset")
st.header("About")
st.write(
  "This dataset shows an example of the Netflix userbase, containing information about User ID, Subscription Type, Monthly Revenue, Join Date, Last Payment Date, Country, Age, Gender, Device, and Plan Duration"
)
st.divider()
# head
st.write("Head")
st.write(df.head())
# tail
st.write("Tail")
st.write(df.tail())
# columns
st.write("Shape")
st.write(df.shape)
st.write("Topics")
st.write(df.columns)

# df.shape
# describe
# df.describe()

# Cleaning:
columns_to_drop = [
  'User ID', 'Join Date', 'Last Payment Date', 'Plan Duration'
]
df.drop(columns_to_drop, axis=1, inplace=True)
df.isna().sum()

st.divider()
st.subheader("Cleaned Data:")
st.write(
  "The cleaning process removed 4 columns, User ID, Join Date, Last Payment Date, and  Plan Duration. They were removed because it wasn't useful to the dataset and irrelevant."
)
st.write("Cleaned Data - Head")
st.write(df.head())
st.write("Cleaned Data - Tail")
st.write(df.tail())
st.write("Cleaned Data - Shape")
st.write(df.shape)
st.write("Cleaned Data - Columns")
st.write(df.columns)
st.divider()
st.subheader(
  "Hypothesis 1: What is the most common device people use Netflix on?")
# visualizations:

new = df['Device'].value_counts().reset_index()
new.columns = ['Device', 'Counts']
fig = px.bar(new, x='Device', y='Counts')
#fig.show()
st.plotly_chart(fig, use_container_width=True)
st.write(
  "Bar graph of 'What is the most common device people use Netflix on?' The bar graph shows the types and numbers of devices that are used to watch Netflix. The bar graph goes in order, the left side has the most device #'s, and the right side has the least. There is also a scale on the left side going vertically, that shows the rough estimate of the # of devices. The graph shows that there are 636 laptops, 633 tablets, 621 smartphones, and 610 smart TVs being used to watch Netflix"
)
st.divider()
st.subheader("Hypothesis 2: What country are most Netflix subscribers from?")
new = df['Country'].value_counts().reset_index()
new.columns = ['Country', 'Counts']
fig = px.pie(new, values='Counts', names='Country')
st.plotly_chart(fig, use_container_width=True)
st.write(
  "Pie graph of 'What country are most Netflix subscribers from?'. The pie graph Shows the # of users that are from a country. For instance, United States takes up about 18% of the pie graph (also says this when you hover) meaning that 18% of Netflix's subscriptions are from the United States. The pie chart shows information that is corresponding to other countries. According to the chart, 36% of Netflix subscriptions are from the United States and Spain (18% each), 12.7% from Canada, 51.24% from the United Kingdom, Australia, Germany, France, Brazil, Mexico, and Italy (7.32% each)."
)
st.divider()
st.subheader("Hypothesis 3: What is the most common subscription type?")
new = df['Subscription Type'].value_counts().reset_index()
new.columns = ['Subscription Type', "Counts"]
fig = px.bar(new, x='Subscription Type', y='Counts')
# fig.show()
st.plotly_chart(fig, use_container_width=True)
st.write(
  "In this bar graph for 'What is the most common subscription type?', it shows the number of subscriptions each type has. On the left, there are numbers that are in intervals of 100 so you can't see the exact number, but if you hover over the bars, it has information on what subscription type it is, and what the exact count of it is. There are three types of subscriptions. Premium, standard, basic. The graph shows that 999 people have bought the basic subscription, 768 people have subscribed to the standard, and 733 people have subscribed to premium. "
)
st.divider()
st.subheader(
  "Hypothesis 4: What is the relationship with the subscription type and country"
)
fd = df.groupby("Country")["Subscription Type"].value_counts().reset_index(
  name="Counts")
fig = px.bar(fd, x='Subscription Type', y='Counts', color='Country')
#fig.show()
st.plotly_chart(fig, use_container_width=True)
st.write(
  "The bar chart of 'What is the relationship with the subscription type and country?' shows what subscriptions are from what country. For example, the premium subscription has 145 counts from United States, meaning that there are 145 premium subscriptions from the U.S. The graph also shows this information for other subscription types and countries. For example, in the premium category, it shows that 212 people have subscribed from Spain"
)
st.divider()

# try machine learning:
# do preprocessing, using label encoder:
st.header("Hey, check out our machine learning model!")
st.subheader(
  "It has a 65% chance of getting the correct answer when you put in a country's number. The answer is supposed to be the countries highest subscription count. (Which type of subscription has the most counts from one specific country) You can verify the answer using graph #4."
)
col1, col2 = st.columns(2)
col1.write("Australia: 0")
col1.write("Brazil: 1")
col1.write("Canada: 2")
col1.write("France: 3")
col1.write("Germany: 4")
col1.write("Italy: 5")
col1.write("Mexico: 6")
col1.write("Spain: 7")
col1.write("United Kingdom: 8")
col1.write("United States: 9")
user_input = col2.text_input("Put a country number here", 0)

le = preprocessing.LabelEncoder()
df['Country'] = le.fit_transform(df['Country'])
# use X ="Country", and y = "Subsription type"
X = df["Country"].to_numpy().reshape(-1, 1)
y = df["Subscription Type"].to_numpy()
# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.33,
                                                    random_state=42)
# Use decision tree classifier
clf = DecisionTreeClassifier(random_state=0, max_depth=4).fit(X_train, y_train)
# use predict
predict = clf.predict(np.array([user_input]).reshape(-1, 1))
col2.write(predict)
st.divider()
st.subheader("Conclusion")
st.write(
  "In conclusion, the Netflix Userbase Dataset shows different variations of who and what interacts with Netflix subscriptions. In the dataset, there is a large age range of buyers, between the ages of 26 and 51. There are also different subscription types that people can buy as well as different devices they can use Netflix on. This dataset was really helpful because it shows us insights on what potential people subscribe to Netflix. "
)
st.write(
  "In graph #1, it is asking, 'What is the most common device people use Netflix on?' The bar graph  tells us the number of devices used for Netflix. For graph #2, the pie chart shows us what percentage of Netflix's subscribers are from what country. For graph #3, the bar graph shows us how many people have bought what Netflix subscription type (Basic, standard, or premium). The graph also shows us the relationship the subscription type has with the amount of people buying it. It is a possiblility that there are more people buying the basic subscription because it is cheaper. Same for premium because it is more expensive. Graph #4 shows us the relationship between the number of subscription types bought and the country. This graph has a lot of detail because it not only shows us the three subscription types, but it also shows us how much subscribers are from each country. The graph is a mix of #2 and #3"
)
