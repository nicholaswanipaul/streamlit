import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# To set a webpage title, header and subtitle
st.set_page_config(page_title="Food price analysis", layout='wide')
st.header("Commodity Price Prediction")
st.subheader("Interact with this dashboard using the widgets on the sidebar")

# read in the file
price_data = pd.read_csv("https://raw.githubusercontent.com/nicholaswanipaul/streamlit/main/food_prices_cleaned.csv")
price_data.info()
price_data.duplicated()
price_data.count()
price_data.dropna()

# Creating sidebar widget filters from price dataset
year_list = price_data['Year'].unique().tolist()
# increasing prediction year up to 2026,
x = len(year_list)
year_list.insert(x, 2024)
year_list.insert(x + 1, 2025)
year_list.insert(x + 2, 2026)
price_rating = price_data['unit_price'].unique().tolist()
category_list = price_data['category'].unique().tolist()
commodity_list = price_data['commodity'].unique().tolist()
priceflag_list = price_data['priceflag'].unique().tolist()

def name_to_code(commodity):
    #commodity = "Sugar food aid"
    commodity_list = price_data['commodity'].unique().tolist()
    if commodity == "Beans red":
        x = 2
    elif commodity == "Cassava":
        x = 3
    elif commodity == "Cassava dry":
        x = 4
    elif commodity == "Charcoal":
        x = 5
    elif commodity == "Chicken":
        x = 6
    elif commodity == "Cowpeas":
        x = 7
    elif commodity == "Exchange rate":
        x = 8
    if commodity == "Exchange rate unofficial":
        x = 9
    elif commodity == "Fish dry":
        x = 10
    elif commodity == "Fish fresh":
        x = 11
    elif commodity == "Fuel diesel":
        x = 12
    elif commodity == "Fuel diesel parallel market":
        x = 13
    elif commodity == "Fuel petrol-gasoline":
        x = 14
    elif commodity == "Fuel petrol-gasoline parallel market":
        x = 15
    elif commodity == "Groundnuts shelled":
        x = 16
    if commodity == "Groundnuts unshelled":
        x = 17
    elif commodity == "Livestock cattle":
        x = 18
    elif commodity == "Livestock goat":
        x = 19
    elif commodity == "Livestock sheep":
        x = 20
    elif commodity == "Maize food aid":
        x = 21
    elif commodity == "Maize meal":
        x = 22
    elif commodity == "Maize white":
        x = 23
    elif commodity == "Meat beef":
        x = 24
    if commodity == "Meat goat":
        x = 25
    elif commodity == "Milk fresh":
        x = 26
    elif commodity == "Millet white":
        x = 27
    elif commodity == "Milling cost Maize":
        x = 28
    elif commodity == "Milling cost sorghum":
        x = 29
    elif commodity == "Oil vegetable":
        x = 30
    elif commodity == "Okra dry":
        x = 31
    elif commodity == "Peas yellow":
        x = 32
    if commodity == "Potatoes Irish":
        x = 33
    elif commodity == "Rice":
        x = 34
    elif commodity == "Salt":
        x = 35
    elif commodity == "Sesame":
        x = 36
    elif commodity == "Sorghum":
        x = 37
    elif commodity == "Sorghum brown":
        x = 38
    elif commodity == "Sorghum flour":
        x = 39
    elif commodity == "Sorghum food aid":
        x = 40
    elif commodity == "Sorghum red":
        x = 41
    elif commodity == "Sorghum white":
        x = 42
    elif commodity == "Sugar brown":
        x = 43
    elif commodity == "Sugar food aid":
        x = 44
    elif commodity == "Wage":
        x = 45
    elif commodity == "Wheat flour":
        x = 46
    else:
        x = 0
    return x


# Add the filters. Every widget goes in here
with st.sidebar:
    year_option=st.selectbox('Select Prediction year', (year_list))
    commodity_option=st.selectbox('Select commodity to Predict Price', (commodity_list))
    price_flag_option=st.selectbox('Select Price Type', (priceflag_list))
    if st.button('Click to Predict'):
        #st.write(name_to_code(commodity_option))
        st.write(commodity_list)
    else:
        st.write("yes")
    st.write(
        "Select a range on the slider (it represents prices) to view the total number of commodities that falls within that range")
    # create a slider to hold user scores
    new_price_rating = st.slider(label="Choose a value:",
                                 min_value=1.0,
                                 max_value=35000.0,
                                 value=(3.0, 4.0))

    st.write("Select your preferred commodity categories and year to view the commodity prices that year")
    # create a multiselect option that holds genre
    new_category_list = st.multiselect('Choose Genre:',
                                       category_list,
                                       default=['cereals and tubers', 'pulses and nuts', 'non-food', 'oil and fats'])

    # create a selectbox option that holds all unique years
    year = st.selectbox('Choose a Year', year_list, 0)

# Configure the slider widget for interactivity
commodity_info = (price_data['unit_price'].between(*new_price_rating))

# Configure the selectbox and multiselect widget for interactivity
new_category_year = (price_data['category'].isin(new_category_list)) & (price_data['Year'] == year)

# VISUALIZATION SECTION
# group the columns needed for visualizations
col1, col2 = st.columns([2, 3])
with col1:
    st.write("""#### Lists of commodities filtered by year and categories """)
    dataframe_price_year = price_data[new_category_year].groupby(['commodity', 'unit_price'])['Year'].sum()
    dataframe_price_year = dataframe_price_year.reset_index()
    st.dataframe(dataframe_price_year, width=400)

with col2:
    st.write("""#### User score of movies and their genre """)
    rating_count_year = price_data[commodity_info].groupby('category')['unit_price'].count()
    rating_count_year = rating_count_year.reset_index()
    figpx = px.line(rating_count_year, x='category', y='unit_price')
    st.plotly_chart(figpx)

# creating a bar graph with matplotlib
st.write("""
Average Movie Budget, Grouped by Genre
    """)
# avg_budget = movies_data.groupby('genre')['budget'].mean().round()
# avg_budget = avg_budget.reset_index()
# genre = avg_budget['genre']
# avg_bud = avg_budget['budget']

# fig = plt.figure(figsize = (19, 10))

# plt.bar(genre, avg_bud, color = 'maroon')
# plt.xlabel('genre')
# plt.ylabel('budget')
# plt.title('Matplotlib Bar Chart Showing The Average Budget of Movies in Each Genre')
# st.pyplot(fig)
