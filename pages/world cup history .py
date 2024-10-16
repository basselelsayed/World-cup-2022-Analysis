import streamlit as st
import pandas as pd
import numpy as np
import plotly.express   as px
Argentina= pd.read_csv('./sources/Worldcups_History_Argentina.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Australia =pd.read_csv('./sources/Worldcups_History_Australia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Belgium = pd.read_csv('./sources/Worldcups_History_Belguim.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Brazil = pd.read_csv('./sources/Worldcups_History_Brazil.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
cameroon = pd.read_csv('./sources/Worldcups_History_Cameroon.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Canada = pd.read_csv('./sources/Worldcups_History_Canada.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Costarica = pd.read_csv('./sources/Worldcups_History_Costa_Rica.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Croatia = pd.read_csv('./sources/Worldcups_History_Croatia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Denemark = pd.read_csv('./sources/Worldcups_History_Denmark.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Ecuador = pd.read_csv('./sources/Worldcups_History_Ecuador.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
England = pd.read_csv('./sources/Worldcups_History_England.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
France = pd.read_csv('./sources/Worldcups_History_France.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Germany = pd.read_csv('./sources/Worldcups_History_Germany.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Ghana = pd.read_csv('./sources/Worldcups_History_Ghana.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Iran = pd.read_csv('./sources/Worldcups_History_Iran.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Japan = pd.read_csv('./sources/Worldcups_History_Japan.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Korea = pd.read_csv('./sources/Worldcups_History_Korea.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Mexico = pd.read_csv('./sources/Worldcups_History_Mexico.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Morocco = pd.read_csv('./sources/Worldcups_History_Morocco.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Netherlands = pd.read_csv ('./sources/Worldcups_History_N.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Poland= pd.read_csv('./sources/Worldcups_History_Poland.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Portugal = pd.read_csv('./sources/Worldcups_History_Portugal.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Qatar = pd.read_csv('./sources/Worldcups_History_Qatar.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Saudi_Arabia = pd.read_csv('./sources/Worldcups_History_Saudi.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Senegal = pd.read_csv('./sources/Worldcups_History_Senegal.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Serbia = pd.read_csv('./sources/Worldcups_History_Serbia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Spain = pd.read_csv('./sources/Worldcups_History_Spain.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Switzerland = pd.read_csv('./sources/Worldcups_History_Switzerland.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Tunisia = pd.read_csv('./sources/Worldcups_History_Tunisia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
United_States = pd.read_csv('./sources/Worldcups_History_USA.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Uruguay = pd.read_csv('./sources/Worldcups_History_Uruguay.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Wales = pd.read_csv('./sources/Worldcups_History_Wales.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)

player_trophies = pd.read_csv('./sources//award_winners.csv')
world_cup2022= pd.concat([Argentina, Australia, Belgium, Brazil, cameroon, Canada, Costarica, Croatia, Denemark, Ecuador, England, France, Germany, Ghana, Iran, Japan, Korea, Mexico, Morocco, Netherlands, Poland, Portugal, Qatar, Saudi_Arabia, Senegal, Serbia, Spain, Switzerland, Tunisia, United_States, Uruguay, Wales]).drop([0],axis=0).reset_index()
world_cup2022.Squad =world_cup2022.Squad.str.replace('West Germany','Germany')
## all countries history
countries = ['Argentina', 'Australia', 'Belgium', 'Brazil', 'cameroon', 'Canada', 'Costarica', 'Croatia', 'Denemark', 'Ecuador', 'England', 'France', 'Germany', 'Ghana', 'Iran', 'Japan', 'Korea', 'Mexico', 'Morocco', 'Netherlands', 'Poland', 'Portugal', 'Qatar', 'Saudi_Arabia', 'Senegal', 'Serbia', 'Spain', 'Switzerland', 'Tunisia', 'United_States', 'Uruguay', 'Wales']
st.subheader('Here  is  the  history of all 32 countries')
col1 , col2 = st.columns([5,1])
with col1:
    selection = st.selectbox('please select a country', countries)
    
    if selection == 'Argentina':
        st.write(Argentina)
    elif selection == 'Australia':
        st.write(Australia) 
    elif selection == 'Belgium':
        st.write(Belgium)       
    elif selection == 'Brazil':
        st.write(Brazil)        
    elif selection == 'cameroon':
        st.write(cameroon)
    elif selection == 'Canada':
        st.write(Canada)
    elif selection == 'Costarica':
        st.write(Costarica)
    elif selection == 'Croatia':
        st.write(Croatia)
    elif selection == 'Denemark':
        st.write(Denemark)
    elif selection == 'Ecuador':
        st.write(Ecuador)
    elif selection == 'England':
        st.write(England)
    elif selection == 'France':
        st.write(France)
    elif selection == 'Germany':
        st.write(Germany)
    elif selection == 'Ghana':
        st.write(Ghana)
    elif selection == 'Iran':
        st.write(Iran)
    elif selection == 'Japan':
        st.write(Japan)
    elif selection == 'Korea':
        st.write(Korea)
    elif selection == 'Mexico':
        st.write(Mexico)
    elif selection == 'Morocco':
        st.write(Morocco)
    elif selection == 'Netherlands':
        st.write(Netherlands)
    elif selection == 'Poland':
        st.write(Poland)
    elif selection == 'Portugal':
        st.write(Portugal)
    elif selection == 'Qatar':
        st.write(Qatar)
    elif selection == 'Saudi_Arabia':
        st.write(Saudi_Arabia)
    elif selection == 'Senegal':
        st.write(Senegal)
    elif selection == 'Serbia':
        st.write(Serbia)
    elif selection == 'Spain':
        st.write(Spain)
    elif selection == 'Switzerland':
        st.write(Switzerland)
    elif selection == 'Tunisia':
        st.write(Tunisia)
    elif selection == 'United_States':
        st.write(United_States)
    elif selection == 'Uruguay':
        st.write(Uruguay)
    elif selection == 'Wales':
        st.write(Wales)

with col2:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.write("MP = matchplayed") 
    st.write("W = win")
    st.write("D = draw")
    st.write("L = lose")
    st.write("GF = goal for")
    st.write("GA = goal against")
    st.write("GD = goal difference")
    st.write("PTS = points")
 

##countries statistics
st.subheader(' Countries Statistics')
statistics=world_cup2022.groupby('Squad').sum().reset_index()
statistics.drop(['Season', 'index'] , axis=1,inplace=True)

col1 , col2 = st.columns([5,1])
with col1:
    st.dataframe(statistics)
with col2:
   
    st.write("MP = matchplayed") 
    st.write("W = win")
    st.write("D = draw")
    st.write("L = lose")
    st.write("GF = goal for")
    st.write("GA = goal against")
    st.write("GD = goal difference")
    st.write("PTS = points")




##most participants in worldcup
st.subheader('History of countries participate in the world cup ')
col1 , col2 = st.columns([1,2])
with col1:
    
    nopiwc = world_cup2022[['Squad','Season']].groupby('Squad').count().sort_values(by='Season',ascending=False).reset_index().head(10)
    st.dataframe(nopiwc)
with col2:

    figure0 = px.funnel(nopiwc , x="Squad" , y="Season")
    st.plotly_chart(figure0)




##1st place
table_1st = world_cup2022[world_cup2022['LgRank']=='1st'].Squad.value_counts().reset_index()
most_1st_years =world_cup2022[(world_cup2022['LgRank']=='1st')& (world_cup2022['Squad']=='Brazil') ]["Season"].sort_values(ascending=True).tolist()
st.subheader('History of champions in the world cup ')
col1 , col2 = st.columns([1,2])
with col1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.dataframe(table_1st)
with col2:
    first = px.bar(table_1st , x='count', y='Squad' )
    st.plotly_chart(first)

##2nd place
table_2nd = world_cup2022[world_cup2022['LgRank']=='2nd'].Squad.value_counts().reset_index()
most_2nd_years =world_cup2022[(world_cup2022['LgRank']=='2nd')& (world_cup2022['Squad']=='Germany') ]["Season"].sort_values(ascending=True).tolist()
st.subheader('History of countries runner-up in the world cup ')
col1 , col2 = st.columns([1,2])
with col1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.dataframe(table_2nd)
with col2:
    second = px.bar(table_2nd , x='count', y='Squad' )
    st.plotly_chart(second)


## 3rd place
table_3rd = world_cup2022[world_cup2022['LgRank']=='3rd'].Squad.value_counts().reset_index()
most_3rd_years =world_cup2022[(world_cup2022['LgRank']=='3rd')& (world_cup2022['Squad']=='Italy') ]["Season"].sort_values(ascending=True).tolist()
st.subheader('History of countries third place in the world cup ')
col1 , col2 = st.columns([1,2])
with col1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.dataframe(table_3rd)
with col2:
    third = px.bar(table_3rd , x='count', y='Squad' )
    st.plotly_chart(third)

##4th place
table_4th = world_cup2022[world_cup2022['LgRank']=='4th'].Squad.value_counts().reset_index()
most_4th_years =world_cup2022[(world_cup2022['LgRank']=='4th')& (world_cup2022['Squad']=='Netherlands') ]["Season"].sort_values(ascending=True).tolist()
st.subheader('History of countries fourth place in the world cup ')
col1 , col2 = st.columns([1,2])
with col1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.dataframe(table_4th)
with col2:
    fourth = px.bar(table_4th , x='count', y='Squad' , title='World Cup fourth place 1930-2018')
    st.plotly_chart(fourth)
