from nba_api.live.endpoints._base import Endpoint
from nba_api.live.library.http import NBAStatsHTTP

class GameOdds(Endpoint):
    endpoint_url = 'gameOdds/{game_id}.json'
    expected_data = {'odds': {'gameId', 'team', 'odds', 'suspended'}}

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
