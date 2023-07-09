import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# To set a webpage title, header and subtitle
st.set_page_config(page_title = "Food price analysis",layout = 'wide')
st.header("South Sudan Commodities Prices")
st.subheader("Interact with this dashboard using the widgets on the sidebar")


#read in the file
df3 = pd.read_csv("https://raw.githubusercontent.com/nicholaswanipaul/streamlit/main/food_prices_cleaned.csv")
df3.info()
#df3.duplicated()
df3.count()
#df3.dropna()


# Creating sidebar widget filters from movies dataset
year_list = df3['Year'].tolist()
#score_rating = movies_data['score'].unique().tolist()
unit_price = df3['unit_price'].tolist()
#genre_list = movies_data['genre'].unique().tolist()
#genre_list = movies_data['genre'].unique().tolist()


# Add the filters. Every widget goes in here
with st.sidebar:
    st.write("Select a range on the slider (it represents movie score) to view the total number of movies in a genre that falls within that range ")
    #create a slider to hold user scores
   # new_score_rating = st.slider(label = "Choose a value:",
                                #  min_value = 1.0,
                                #  max_value = 10.0,
                                # value = (3.0,4.0))


    st.write("Select your preferred genre(s) and year to view the movies released that year and on that genre")
    #create a multiselect option that holds genre
   # new_genre_list = st.multiselect('Choose Genre:',
                                       # genre_list, default = ['Animation', 'Horror', 'Fantasy', 'Romance'])

    #create a selectbox option that holds all unique years
    year = st.selectbox('Choose a Year', year_list, 0)

#Configure the slider widget for interactivity
#score_info = (movies_data['score'].between(*new_score_rating))



#Configure the selectbox and multiselect widget for interactivity
#new_genre_year = (df3['market'].isin(new_genre_list)) & (df3['Year'] == year)


#VISUALIZATION SECTION
#group the columns needed for visualizations
col1, col2 = st.columns([2,3])
with col1:
    st.write("""#### South Sudan Market locations""")


    #dataframe_genre_year = movies_data[new_genre_year].groupby(['name', 'genre'])['year'].sum()
    #dataframe_genre_year = movies_data[new_genre_year].groupby(['commodity', 'market'])['Year'].sum()
    #dataframe_genre_year = dataframe_genre_year.reset_index()
    #st.dataframe(dataframe_genre_year, width = 400)

with col2:
    #st.write("""#### User score of movies and their genre """)
    #rating_count_year = movies_data[score_info].groupby('genre')['score'].count()
    #rating_count_year = rating_count_year.reset_index()
    #figpx = px.line(rating_count_year, x = 'genre', y = 'score')
   # st.plotly_chart(figpx)
     plot=sns.lineplot(x="Year", y="unit_price", data=df3)
     st.pyplot(plot.get_figure())
 # creating a bar graph with matplotlib
st.write("""
Average Movie Budget, Grouped by Genre
    """)
avg_price = df3.groupby('category')['unit_price'].mean().round()
avg_budget = avg_price.reset_index()
genre = avg_budget['category']
avg_bud = avg_budget['unit_price']

fig = plt.figure(figsize = (19, 10))

plt.bar(genre, avg_bud, color = 'green')
plt.xlabel('Commodity Categories')
plt.ylabel('unit_price')
plt.title('Bar Chart Showing The Average unit price of Commodities per Category')
st.pyplot(fig)

