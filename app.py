import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import helper

data = pd.read_csv('matches.csv')

data = data.rename(columns={'city':'City','date':'Date','team1':'Team1','team2':'Team2','winner':'Winner','player_of_match':'Player_of_match','venue':'Venue'})

st.sidebar.title('IPL(Indian Premier League) Analysis')
st.sidebar.image('1.jpg')

st.sidebar.header('Created by Shankar Wagh')
st.sidebar.markdown('  Machine Learning Engineer')
url1 = 'https://www.github.com/Shankar297'
url2 = 'https://www.linkedin.com/in/shankar-wagh'

user_menu = st.sidebar.radio(
    'select an option',
    ('Season Wise Analysis','Team Wise Analysis','Overall Analysis','Graphical Analysis'))


if st.sidebar.button('Connect Me'):
    st.sidebar.header('Created by Shankar Wagh')
    st.sidebar.markdown('  Machine Learning Engineer')
    st.sidebar.markdown('Contact No. :- +91 8329471855')
    st.sidebar.markdown('Github Profile')
    st.sidebar.markdown(url1,unsafe_allow_html=True)
    st.sidebar.markdown('LinkedIn Profile')
    st.sidebar.markdown(url2,unsafe_allow_html=True)

if user_menu=='Season Wise Analysis':
    st.title('Season Wise Analysis')

    season_list = (data['Season'].value_counts().index).tolist()
    season_list.sort()

    selected_season = st.selectbox('Select Season', season_list)
    st.subheader(selected_season)
    season_wise_data = helper.season_wise_data(data,selected_season)

    st.table(season_wise_data)

if user_menu=='Team Wise Analysis':
    st.title('Team Wise Analysis')

    team1_list = data['Team1'].unique().tolist()
    team2_list = team1_list.sort()

    team2_list = data['Team2'].unique().tolist()

    selected_team1 = st.selectbox('Select First Team', team1_list)
    selected_team2 = st.selectbox('Select Second Team', team2_list)

    st.subheader(selected_team1 +" Vs "+ selected_team2)

    two_team_data = helper.fetch_team_wise(data=data,selected_team1=selected_team1,selected_team2=selected_team2)
    st.table(two_team_data)

if user_menu=='Overall Analysis':
    st.title('Overall Analysis')
    questions = ['Options',
 'Which IPL team won by scoring the maximum runs?',
 'Which IPL team won by consuming maximum wickets?',
 'Which IPL team won by taking minimum wickets?',
 'Highest wins by teams per season']

    questions2 = ['Options',
        'How many matches (in total) were played in IPL',
    'Which season consisted of the highest number of matches ever played?',
    'Which is the most successful IPL team (Highest winner)?']

    selected_question2 = st.selectbox('Select a Question',questions2)
    if selected_question2=='How many matches (in total) were played in IPL':
        st.markdown(756)
    if selected_question2=='Which season consisted of the highest number of matches ever played?':
        st.markdown('IPL Season -2013')
    if selected_question2=='Which is the most successful IPL team (Highest winner)?':
        st.markdown('Team - Mumbai Indians') 
        st.markdown('Match Win - 109')


    selected_question = st.selectbox('Select a Question',questions)

    data=data[['Season','City','Date','Team1','Team2','win_by_runs','win_by_wickets','Winner','Player_of_match','Venue']]
    
    answer = helper.fetch_answer(data,selected_question)

    if selected_question=='Highest wins by teams per season':
        answer = helper.fetch_answer(data,selected_question)
        st.table(answer)
    else:
         st.text(answer)

if user_menu=='Graphical Analysis':
    st.title('Most Succesful Teams(Most Time Winner)')
    team_data = helper.most_successful_team(data)
    fig =px.bar(team_data,x='No of Matches Win',y='Team Name')
    fig.update_layout(barmode='stack',yaxis={'categoryorder':'total ascending'})
    fig.update_layout(autosize=False,width=950,height=550)
    st.plotly_chart(fig)

    st.title('Stadium wrt Matches')
    venue_data = helper.fetch_venue_data(data)
    fig = px.bar(venue_data, y='Stadium Name', x='No of Matches')
    fig.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})
    fig.update_layout(autosize=False,width=1000,height=700)
    st.plotly_chart(fig)

    st.title('Man Of The Match')
    player_data = helper.fetch_player_data(data)
    fig = px.line(player_data,x='Player Name',y='No of Times Man Of The Match')
    fig.update_layout(autosize=False,width=900,height=600)
    st.plotly_chart(fig)