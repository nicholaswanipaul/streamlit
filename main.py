import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# To set a webpage title, header and subtitle
st.set_page_config(page_title = "Food price analysis",layout = 'wide')
st.header("Commodity Price Prediction")
st.subheader("Interact with this dashboard using the widgets on the sidebar")


#read in the file
price_data = pd.read_csv("https://raw.githubusercontent.com/nicholaswanipaul/streamlit/main/food_prices_cleaned.csv")
price_data.info()
price_data.duplicated()
price_data.count()
price_data.dropna()


# Creating sidebar widget filters from price dataset
year_list = price_data['Year'].unique().tolist()
price_rating = price_data['unit_price'].unique().tolist()
category_list = price_data['category'].unique().tolist()


# Add the filters. Every widget goes in here
with st.sidebar:
    st.write("Select a range on the slider (it represents prices) to view the total number of commodities that falls within that range")
    #create a slider to hold user scores
    new_price_rating = st.slider(label = "Choose a value:",
                                  min_value = 1.0,
                                  max_value = 350000.0,
                                 value = (3.0,4.0))


    st.write("Select your preferred commodity categories and year to view the commodity prices that year")
    #create a multiselect option that holds genre
    new_category_list = st.multiselect('Choose Genre:',
                                        category_list, default = ['cereals and tubers', 'pulses and nuts', 'non-food', 'oil and fats'])

    #create a selectbox option that holds all unique years
    year = st.selectbox('Choose a Year', year_list, 0)

#Configure the slider widget for interactivity
commodity_info = (price_data['unit_price'].between(*new_price_rating))



#Configure the selectbox and multiselect widget for interactivity
new_category_year = (price_data['category'].isin(new_category_list)) & (price_data['Year'] == year)


#VISUALIZATION SECTION
#group the columns needed for visualizations
col1, col2 = st.columns([2,3])
with col1:
    st.write("""#### Lists of commodities filtered by year and categories """)
    dataframe_price_year = price_data[new_category_year].groupby(['commodity', 'unit_price'])['Year'].sum()
    dataframe_price_year = dataframe_price_year.reset_index()
    st.dataframe(dataframe_price_year, width = 400)

with col2:
    st.write("""#### User score of movies and their genre """)
    rating_count_year = price_data[commodity_info].groupby('category')['unit_price'].count()
    rating_count_year = rating_count_year.reset_index()
    figpx = px.line(rating_count_year, x = 'category', y = 'unit_price')
    st.plotly_chart(figpx)

 # creating a bar graph with matplotlib
st.write("""
Average Movie Budget, Grouped by Genre
    """)
#avg_budget = movies_data.groupby('genre')['budget'].mean().round()
#avg_budget = avg_budget.reset_index()
#genre = avg_budget['genre']
#avg_bud = avg_budget['budget']

#fig = plt.figure(figsize = (19, 10))

#plt.bar(genre, avg_bud, color = 'maroon')
#plt.xlabel('genre')
#plt.ylabel('budget')
#plt.title('Matplotlib Bar Chart Showing The Average Budget of Movies in Each Genre')
#st.pyplot(fig)

