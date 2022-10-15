import streamlit as st
import pandas as
import numpy as np
Argentina= pd.read_csv('sources\Worldcups_History_Argentina.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Australia =pd.read_csv('sources\Worldcups_History_Australia.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Belgium = pd.read_csv('sources\Worldcups_History_Belguim.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Brazil = pd.read_csv('sources\Worldcups_History_Brazil.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
cameroon = pd.read_csv('sources\Worldcups_History_Cameroon.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Canada = pd.read_csv('sources\Worldcups_History_Canada.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Costarica = pd.read_csv('sources\Worldcups_History_Costa_Rica.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Croatia = pd.read_csv('sources\Worldcups_History_Croatia.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Denemark = pd.read_csv('sources\Worldcups_History_Denmark.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Ecuador = pd.read_csv('sources\Worldcups_History_Ecuador.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
England = pd.read_csv('sources\Worldcups_History_England.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
France = pd.read_csv('sources\Worldcups_History_France.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Germany = pd.read_csv('sources\Worldcups_History_Germany.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Ghana = pd.read_csv('sources\Worldcups_History_Ghana.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Iran = pd.read_csv('sources\Worldcups_History_Iran.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Japan = pd.read_csv('sources\Worldcups_History_Japan.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Korea = pd.read_csv('sources\Worldcups_History_Korea.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Mexico = pd.read_csv('sources\Worldcups_History_Mexico.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Morocco = pd.read_csv('sources\Worldcups_History_Morocco.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Netherlands = pd.read_csv (r'sources\Worldcups_History_N.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Poland= pd.read_csv('sources\Worldcups_History_Poland.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Portugal = pd.read_csv('sources\Worldcups_History_Portugal.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Qatar = pd.read_csv('sources\Worldcups_History_Qatar.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Saudi_Arabia = pd.read_csv('sources\Worldcups_History_Saudi.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Senegal = pd.read_csv('sources\Worldcups_History_Senegal.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Serbia = pd.read_csv('sources\Worldcups_History_Serbia.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Spain = pd.read_csv('sources\Worldcups_History_Spain.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Switzerland = pd.read_csv('sources\Worldcups_History_Switzerland.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Tunisia = pd.read_csv('sources\Worldcups_History_Tunisia.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
United_States = pd.read_csv(r'sources\Worldcups_History_USA.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Uruguay = pd.read_csv(r'sources\Worldcups_History_Uruguay.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)
Wales = pd.read_csv('sources\Worldcups_History_Wales.csv').drop(['Squad','Comp','Top Team Scorer', 'Goalkeeper', 'Notes'],axis=1)







st.title('world cup 2022 ')
st.markdown('This app performs simple Analysis on participants country of world cup 2022')
st.image('worldcup.png',width=450)
st.markdown('''the analysis is based on the data of fifa world cup 2022 participants 
countries only which are 32 countries so some countries are not included in 
this analysis which are not participating in world cup 2022\n''')


