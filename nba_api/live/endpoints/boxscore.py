from nba_api.live.endpoints._base import Endpoint
from nba_api.live.library.http import NBAStatsHTTP

class BoxScore(Endpoint):
    endpoint_url = 'boxscore/boxscore_{game_id}.json'
    expected_data = {'meta', {'version', 'code','request', 'time'}, 
    'game', {'gameId', 'gameTimeLocal','gameTimeUTC','gameTimeHome','gameTimeAway','gameEt','duration','gameCode',
    'gameStatusText','gameStatus','regulationPeriods','period','gameClock','attendance','sellout','arena',
    {'arenaId','arenaName','arenaCity','arenaState','arenaCountry','arenaTimezone'},'officials', ['personId','name',
    'nameI','firstName','familyName','jerseyNum','assignment'], 'homeTeam', {'teamId','teamName','teamCity','teamTricode',
    'score','inBonus','timeoutsRemaining','periods',['period','periodType','score'],"players", ['status','order','personId',
    'jerseyNum','position','starter','oncourt','played','statistics',['assists','blocks','blocksReceived',
    'fieldGoalsAttempted','fieldGoalsMade','fieldGoalsPercentage','foulsOffensive','foulsDrawn','foulsPersonal',
    'foulsTechnical','freeThrowsAttempted','freeThrowsMade','freeThrowsPercentage','minus','minutes','minutesCalculated',
    'plus','plusMinusPoints','points','pointsFastBreak','pointsInThePaint','pointsSecondChance','reboundsDefensive',
    'reboundsOffensive','reboundsTotal','steals','threePointersAttempted','threePointersMade','threePointersPercentage',
    'turnovers','twoPointersAttempted','twoPointersMade','twoPointersPercentage'],'name','nameI','firstName','familyName'],
    'statistics',{'assists','assistsTurnoverRatio','benchPoints','biggestLead','biggestLeadScore','biggestScoringRun',
    'biggestScoringRunScore','blocks','blocksReceived','fastBreakPointsAttempted','fastBreakPointsMade','fastBreakPointsPercentage',
    'fieldGoalsAttempted','fieldGoalsEffectiveAdjusted','fieldGoalsMade','fieldGoalsPercentage','foulsOffensive','foulsDrawn',
    'foulsPersonal','foulsTeam','foulsTechnical','foulsTeamTechnical','freeThrowsAttempted','freeThrowsMade','freeThrowsPercentage',
    'leadChanges','minutes','minutesCalculated','points','pointsAgainst','pointsFastBreak','pointsFromTurnovers','pointsInThePaint',
    'pointsInThePaintAttempted','pointsInThePaintMade','pointsInThePaintPercentage','pointsSecondChance','reboundsDefensive',
    'reboundsOffensive','','','','',''}}}}
    


    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 game_id,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.game_id = game_id
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        if get_request:
            self.get_request()
 
    def get_request(self):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint_url.format(game_id=self.game_id),
            parameters = {},
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout
        )
        #self.load_response()
        
    def load_response(self):
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.meta = Endpoint.DataSet(data=data_sets['meta'])
        self.game = Endpoint.DataSet(data=data_sets['game'])
