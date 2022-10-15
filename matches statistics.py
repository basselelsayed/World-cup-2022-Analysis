import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



Argentina= pd.read_csv('.\sources\Worldcups_History_Argentina.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Australia =pd.read_csv('.\sources\Worldcups_History_Australia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Belgium = pd.read_csv('.\sources\Worldcups_History_Belguim.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Brazil = pd.read_csv('.\sources\Worldcups_History_Brazil.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
cameroon = pd.read_csv('.\sources\Worldcups_History_Cameroon.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Canada = pd.read_csv('.\sources\Worldcups_History_Canada.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Costarica = pd.read_csv('.\sources\Worldcups_History_Costa_Rica.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Croatia = pd.read_csv('.\sources\Worldcups_History_Croatia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Denemark = pd.read_csv('.\sources\Worldcups_History_Denmark.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Ecuador = pd.read_csv('.\sources\Worldcups_History_Ecuador.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
England = pd.read_csv('.\sources\Worldcups_History_England.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
France = pd.read_csv('.\sources\Worldcups_History_France.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Germany = pd.read_csv('.\sources\Worldcups_History_Germany.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Ghana = pd.read_csv('.\sources\Worldcups_History_Ghana.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Iran = pd.read_csv('.\sources\Worldcups_History_Iran.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Japan = pd.read_csv('.\sources\Worldcups_History_Japan.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Korea = pd.read_csv('.\sources\Worldcups_History_Korea.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Mexico = pd.read_csv('.\sources\Worldcups_History_Mexico.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Morocco = pd.read_csv('.\sources\Worldcups_History_Morocco.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Netherlands = pd.read_csv (r'.\sources\Worldcups_History_N.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Poland= pd.read_csv('.\sources\Worldcups_History_Poland.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Portugal = pd.read_csv('.\sources\Worldcups_History_Portugal.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Qatar = pd.read_csv('.\sources\Worldcups_History_Qatar.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Saudi_Arabia = pd.read_csv('.\sources\Worldcups_History_Saudi.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Senegal = pd.read_csv('.\sources\Worldcups_History_Senegal.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Serbia = pd.read_csv('.\sources\Worldcups_History_Serbia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Spain = pd.read_csv('.\sources\Worldcups_History_Spain.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Switzerland = pd.read_csv('.\sources\Worldcups_History_Switzerland.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Tunisia = pd.read_csv('.\sources\Worldcups_History_Tunisia.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
United_States = pd.read_csv(r'.\sources\Worldcups_History_USA.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Uruguay = pd.read_csv(r'.\sources\Worldcups_History_Uruguay.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Wales = pd.read_csv('.\sources\Worldcups_History_Wales.csv').drop(['Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
player_trophies = pd.read_csv(r'.\sources\\award_winners.csv')
world_cup2022= pd.concat([Argentina, Australia, Belgium, Brazil, cameroon, Canada, Costarica, Croatia, Denemark, Ecuador, England, France, Germany, Ghana, Iran, Japan, Korea, Mexico, Morocco, Netherlands, Poland, Portugal, Qatar, Saudi_Arabia, Senegal, Serbia, Spain, Switzerland, Tunisia, United_States, Uruguay, Wales]).drop([0],axis=0).reset_index()
world_cup2022.Squad =world_cup2022.Squad.str.replace('West Germany','Germany')
##
statistics=world_cup2022.groupby('Squad').sum().reset_index()
statistics.drop('Season',axis=1,inplace=True)
n = statistics.sort_values(by='MP',ascending=False).reset_index().drop('index',axis=1)
figure1 = px.histogram(n , x="Squad" , y="MP" ,color= "W", title="Matches Played")
st.plotly_chart(figure1)
##
st.markdown('Which country scored most goales in world cup')
best_attack = statistics.sort_values(by='GF',ascending=False)[['Squad','GF']].reset_index()
best_attack.drop('index',axis=1,inplace=True)
st.dataframe(best_attack)
figure2 = px.histogram(best_attack , x="Squad" , y="GF" , title="Best Attack in World Cup")
st.plotly_chart(figure2)
##
st.markdown('Which country has the best defense in world cup')
statistics ['avg_recived_goals_per_match'] = statistics['GA'] / statistics['MP']
best_defense = statistics.sort_values(by='avg_recived_goals_per_match',ascending=True)[['Squad','avg_recived_goals_per_match']].reset_index()
best_defense.drop('index',axis=1,inplace=True)
st.dataframe(best_defense)
figure3 = px.histogram(best_defense , x="Squad" , y="avg_recived_goals_per_match" , title="Best Defense in World Cup")
st.plotly_chart(figure3)

## goals
st.markdown('what is goal statistics in world cup')
goals = pd.read_csv(r'.\sources\\goals.csv')

goals_on_first_half = goals[(goals['minute_regulation']>0) & (goals['minute_regulation']<=45)].reset_index()
goals_on_first_half = goals_on_first_half.count()[0]
p = 2549
first_half_percentage = goals_on_first_half/p*100

goals_on_second_half = goals[(goals['minute_regulation']>45) & (goals['minute_regulation']<=90)].reset_index()
goals_on_second_half = goals_on_second_half.count()[0]
second_half_percentage = round(goals_on_second_half/p*100 , 2)


goals_on_extra_time = goals[(goals['minute_regulation']>90) ].reset_index()
goals_on_extra_time = goals_on_extra_time.count()[0]
extra_time_percentage =  round (goals_on_extra_time/p*100 , 2)

##plot data
values = ['first half percentage' , 'second half percentage' , 'extra time percentage ']
number = [first_half_percentage , second_half_percentage , extra_time_percentage ]
figure4 = px.pie(goals ,values , number )
st.plotly_chart(figure4)




