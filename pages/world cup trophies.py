import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
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
Netherlands = pd.read_csv (r'./sources/Worldcups_History_N.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Poland= pd.read_csv('./sources/Worldcups_History_Poland.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Portugal = pd.read_csv('./sources/Worldcups_History_Portugal.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Qatar = pd.read_csv('./sources/Worldcups_History_Qatar.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Saudi_Arabia = pd.read_csv('./sources/Worldcups_History_Saudi.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Senegal = pd.read_csv('./sources/Worldcups_History_Senegal.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Serbia = pd.read_csv('./sources/Worldcups_History_Serbia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Spain = pd.read_csv('./sources/Worldcups_History_Spain.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Switzerland = pd.read_csv('./sources/Worldcups_History_Switzerland.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Tunisia = pd.read_csv('./sources/Worldcups_History_Tunisia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
United_States = pd.read_csv(r'./sources/Worldcups_History_USA.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Uruguay = pd.read_csv(r'./sources/Worldcups_History_Uruguay.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Wales = pd.read_csv('./sources/Worldcups_History_Wales.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
player_trophies = pd.read_csv(r'./sources//award_winners.csv')
world_cup2022= pd.concat([Argentina, Australia, Belgium, Brazil, cameroon, Canada, Costarica, Croatia, Denemark, Ecuador, England, France, Germany, Ghana, Iran, Japan, Korea, Mexico, Morocco, Netherlands, Poland, Portugal, Qatar, Saudi_Arabia, Senegal, Serbia, Spain, Switzerland, Tunisia, United_States, Uruguay, Wales]).drop([0],axis=0).reset_index()
world_cup2022.Squad =world_cup2022.Squad.str.replace('West Germany','Germany')

## clean data
world_cup2022.Squad =world_cup2022.Squad.str.replace('West Germany','Germany')
player_trophies.tournament_id =player_trophies.tournament_id.str.replace('WC-','').astype(int)
player_trophies['fullname'] = player_trophies['given_name'] + ' ' + player_trophies['family_name']
player_trophies['given_name'] = player_trophies.given_name.str.replace("not applicable" , "name unknown")
player_trophies['family_name'] = player_trophies.family_name.str.replace("not applicable" , "family name unknown")

## golden boot player
st.subheader('History of world cup golden boot') 
golden_boot =player_trophies[['fullname' , 'team_name' , 'tournament_id']][player_trophies['award_name']=='Golden Boot'].sort_values(by='tournament_id',ascending=False).reset_index().drop('index',axis=1, inplace=False)
st.dataframe(golden_boot)

## golden ball country
most_country_golden_boot = golden_boot.team_name.value_counts().reset_index().head(5)
st.subheader('which country has the most golden boot winners ?')
col1 , col2 = st.columns([1,2])
with col1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.dataframe(most_country_golden_boot)
with col2:
    figure4 = px.bar(most_country_golden_boot, x='count', y='team_name')
    st.plotly_chart(figure4)

## golden glove
golden_Glove =player_trophies[[ 'fullname','team_name' , 'tournament_id']][player_trophies['award_name']=='Golden Glove'].sort_values(by='tournament_id',ascending=False).reset_index().drop('index',axis=1, inplace=False)
st.subheader('History of world cup golden glove')
st.dataframe(golden_Glove)

st.subheader('which country has the most golden glove winners ?')
most_country_golden_Glove = golden_Glove.team_name.value_counts().reset_index()
col1 , col2 = st.columns([1,2])
with col1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.dataframe(most_country_golden_Glove)
with col2:
    figure6 = px.bar(most_country_golden_Glove, x='count', y='team_name')
    st.plotly_chart(figure6)

## most young promising player
st.subheader('History of world cup young promising player')
young_player = player_trophies[['fullname' , 'team_name' , 'tournament_id']][player_trophies['award_name']=='Best Young Player'].sort_values(by='tournament_id',ascending=False).reset_index().drop('index',axis=1, inplace=False)
st.dataframe(young_player)

st.subheader('which country has the most young promising player ?')

col1 , col2 = st.columns([1,2])
with col1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    most_country_young_player = young_player.team_name.value_counts().reset_index()
    st.dataframe(most_country_young_player)
with col2:


    figure8 = px.bar(most_country_young_player, x='count', y='team_name')
    st.plotly_chart(figure8)



