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


## merging data

booking = pd.read_csv('./sources/bookings.csv')
team_name = pd.read_csv('./sources/teams.csv')
world_cup_booking = pd.merge(booking,team_name,how='outer',on='team_id')
world_cup_booking['fullname'] = world_cup_booking['given_name'] + ' ' + world_cup_booking['family_name']

## cleaning data
world_cup_booking = world_cup_booking[['fullname','yellow_card','red_card', 'team_name_y']]
yellow_cards = world_cup_booking[['team_name_y', 'fullname']][world_cup_booking['yellow_card'] == 1]
red_cards = world_cup_booking[['team_name_y', 'fullname']][world_cup_booking['red_card'] == 1].reset_index().drop(['index'],axis=1)
most_country_yc = yellow_cards['team_name_y' ].value_counts().reset_index().head(10)
most_country_rc = red_cards['team_name_y' ].value_counts().reset_index().head(10)


## plotting data
st.subheader('who is the most countries have yellow cards')
st.dataframe(yellow_cards)
figure10 = px.histogram(most_country_yc , x="count" ,y = "team_name_y"  )
st.plotly_chart(figure10)

st.subheader('who is the most countries have red cards')
st.dataframe(red_cards)
figure11 = px.histogram(most_country_rc , x="count" ,y = "team_name_y")
st.plotly_chart(figure11)
