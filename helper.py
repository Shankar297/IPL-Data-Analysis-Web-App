def season_wise_data(data, season):
    new_data = data[data['Season']==season][['Season','City','Date','Team1','Team2','Winner','Player_of_match','Venue']]
    new_data.reset_index(drop=True,inplace=True)
    return new_data

def fetch_team_wise(data,selected_team1,selected_team2):
    two_team_data = data[(data['Team1'] == selected_team1) & (data['Team2']== selected_team2)]
    two_team_data=two_team_data[['Season','City','Date','Team1','Team2','Winner','Player_of_match','Venue']]
    two_team_data.sort_values(by='Season',ascending=False,inplace=True)
    two_team_data.reset_index(drop=True,inplace=True)
    return two_team_data


def fetch_answer(data,question):
    if question=='Options':
        answer = ''
    if question=='How many matches (in total) were played in IPL':
        answer = 756
    elif question == 'Which IPL team won by scoring the maximum runs?':
        answer = data.iloc[data['win_by_runs'].idxmax()]
    elif question=='Which IPL team won by consuming maximum wickets?':
        answer = data.iloc[data['win_by_wickets'].idxmax()]
    elif question == 'Which IPL team won by taking minimum wickets?':
        answer=data.iloc[data['win_by_wickets'].idxmin()]
    elif question == 'Which season consisted of the highest number of matches ever played?':
        answer='IPL-2013'
    elif question == 'Which is the most successful IPL team (Highest winner)?':
        data4 = data['Winner'].value_counts().reset_index()
        data4.rename(columns={'index':'Team','Winner':'Match Win'},inplace=True)
        answer = data4.loc[0]
    elif question=='Highest wins by teams per season':
        answer = data.groupby('Season')['Winner'].value_counts()
    return answer

def most_successful_team(data):
    new_data = data['Winner'].value_counts().reset_index()
    new_data.rename(columns={'index':'Team Name','Winner':'No of Matches Win'},inplace=True)
    return new_data

def fetch_venue_data(data):
    venue_data = data['Venue'].value_counts().reset_index()
    venue_data.rename(columns={'index':'Stadium Name','Venue':'No of Matches'},inplace=True)
    return venue_data

def fetch_player_data(data):
    player_data = data['Player_of_match'].value_counts()[0:55].reset_index()
    player_data.rename(columns={'index':'Player Name','Player_of_match':'No of Times Man Of The Match'},inplace=True)
    return player_data