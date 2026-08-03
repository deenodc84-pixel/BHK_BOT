# Basketball data (all hardcoded, no API needed)

NBA_CHAMPIONS = {
    2023: 'Denver Nuggets',
    2022: 'Golden State Warriors',
    2021: 'Milwaukee Bucks',
    2020: 'Los Angeles Lakers',
    2019: 'Toronto Raptors',
    2018: 'Golden State Warriors',
    2017: 'Golden State Warriors',
    2016: 'Cleveland Cavaliers',
    2015: 'Golden State Warriors',
    2014: 'San Antonio Spurs',
    2013: 'Miami Heat',
    2012: 'Miami Heat',
    2011: 'Dallas Mavericks',
    2010: 'Los Angeles Lakers'
}

ALL_TIME_POINTS = [
    ('LeBron James', 38652),
    ('Kareem Abdul-Jabbar', 38387),
    ('Karl Malone', 36928),
    ('Kobe Bryant', 33643),
    ('Michael Jordan', 32292)
]

ALL_TIME_REBOUNDS = [
    ('Wilt Chamberlain', 23924),
    ('Bill Russell', 21620),
    ('Kareem Abdul-Jabbar', 17440),
    ('Karl Malone', 14968),
    ('Dennis Rodman', 13912)
]

ALL_TIME_ASSISTS = [
    ('John Stockton', 15806),
    ('Jason Kidd', 12091),
    ('Chris Paul', 11762),
    ('Steve Nash', 10335),
    ('Magic Johnson', 10141)
]

NBA_TEAMS = [
    'Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 
    'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers',
    'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons',
    'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers',
    'LA Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies',
    'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves',
    'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder',
    'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns',
    'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs',
    'Toronto Raptors', 'Utah Jazz', 'Washington Wizards'
]

TRIVIA_QUESTIONS = [
    {
        'question': 'Who holds the record for most points in a single NBA game?',
        'answer': 'Wilt Chamberlain (100 points)'
    },
    {
        'question': 'Which team has won the most NBA championships?',
        'answer': 'Los Angeles Lakers (17) and Boston Celtics (17)'
    },
    {
        'question': 'Who is the youngest player to score 10,000 NBA points?',
        'answer': 'LeBron James'
    },
    {
        'question': 'What is the NBA three-point line distance?',
        'answer': '23.75 feet at top of arc'
    },
    {
        'question': 'Which player has the most career assists?',
        'answer': 'John Stockton (15,806)'
    }
]

BASKETBALL_FACTS = [
    "The NBA was founded in 1946 as the Basketball Association of America (BAA)",
    "The first NBA game was played on November 1, 1946",
    "The three-point line was introduced in 1979",
    "Michael Jordan has a 61.9% career win percentage",
    "LeBron James is the only player with 30,000+ points, 10,000+ rebounds, and 10,000+ assists",
    "The shortest NBA player was Muggsy Bogues at 5'3\"",
    "The tallest NBA player was Gheorghe Muresan at 7'7\""
]

def get_player_stats(player_name):
    """Mock function for player stats lookup"""
    player_name = player_name.lower().strip()
    
    if player_name in ['lebron', 'lebron james']:
        return {
            'name': 'LeBron James',
            'points': 38652,
            'rebounds': 10667,
            'assists': 10420,
            'championships': 4,
            'mvp_awards': 4
        }
    elif player_name in ['jordan', 'michael jordan']:
        return {
            'name': 'Michael Jordan',
            'points': 32292,
            'rebounds': 6672,
            'assists': 5633,
            'championships': 6,
            'mvp_awards': 5
        }
    elif player_name in ['kobe', 'kobe bryant']:
        return {
            'name': 'Kobe Bryant',
            'points': 33643,
            'rebounds': 7047,
            'assists': 6306,
            'championships': 5,
            'mvp_awards': 1
        }
    elif player_name in ['curry', 'stephen curry']:
        return {
            'name': 'Stephen Curry',
            'points': 23161,
            'rebounds': 4442,
            'assists': 5838,
            'championships': 4,
            'mvp_awards': 2
        }
    else:
        return None

def get_upcoming_games():
    """Mock function for upcoming games"""
    return [
        "Lakers vs Celtics - Tomorrow 8:00 PM EST",
        "Warriors vs Bulls - Tomorrow 8:30 PM EST",
        "Nets vs Knicks - Day after 7:30 PM EST",
        "Bucks vs Heat - Day after 8:00 PM EST",
        "Suns vs Mavericks - In 3 days 8:30 PM EST"
    ]
