import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

match = '''
CREATE TABLE IF NOT EXISTS match (
Player TEXT ,
Scored INTEGER,
Faced INTEGER,
Fours INTEGER,
Sixes INTEGER,
Bowled INTEGER,
Maiden INTEGER,
Given INTEGER,
Wkts INTEGER,
Catches INTEGER ,
Stumping INTEGER,
RO INTEGER
);
'''

teams = '''
CREATE TABLE IF NOT EXISTS teams (
    name TEXT,
    players TEXT,
    value INTEGER
);
'''
stats = '''
CREATE TABLE IF NOT EXISTS stats (
player TEXT,
matches INTEGER,
runs INTEGER,
"100s" INTEGER,
"50s" INTEGER,
value INTEGER,
ctg TEXT
);
'''

def insert_new_team(name,  players, value):
    db = sqlite3.connect('database.db')
    query = """
    INSERT INTO teams(name, players, value)
    VALUES (?,?,?)
    """
    cur = db.cursor()
    cur.execute(query, (name, players, value))
    db.commit()
    db.close()

def insert_new_stats(player, matches,runs,hundreds,fifties,value,ctg):
    db = sqlite3.connect('database.db')
    query = """
    INSERT INTO stats(player,matches,runs,"100s","50s",value,ctg)
    VALUES (?,?,?,?,?,?,?)
    """
    cur = db.cursor()
    cur.execute(query, (player, matches,runs,hundreds,fifties,value,ctg))
    db.commit()
    db.close()

def insert_new_match(player, scored,faced,fours,sixes,bowled,maiden,given,wkts,catches,stumping,ro):
    db = sqlite3.connect('database.db')
    query = """
    INSERT INTO match(Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RO)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """
    cur = db.cursor()
    cur.execute(query, (player, scored,faced,fours,sixes,bowled,maiden,given,wkts,catches,stumping,ro))
    db.commit()
    db.close()

def display_all_players_name():
    db = sqlite3.connect('database.db')
    query = """
    SELECT name from teams
    """
    cur = db.cursor()
    items_io = cur.execute(query).fetchall()
    item_lst = [i[0] for i in items_io]
    return item_lst


def display_BAT_players_specific_data():
    db = sqlite3.connect('database.db')
    query = """
    SELECT player ,value,matches ,runs FROM stats WHERE ctg="BAT"
    """
    cur = db.cursor()
    data = cur.execute(query).fetchall()
    db.close()
    return data



def display_BWL_players_name():
     db = sqlite3.connect('database.db')
     query = """
    SELECT player ,value,matches ,runs FROM stats WHERE ctg="BWL"
    """
     cur = db.cursor()
     data = cur.execute(query).fetchall()
     db.close()
     return data

def display_AR_players_name():
     db = sqlite3.connect('database.db')
     query = """
    SELECT player ,value,matches ,runs FROM stats WHERE ctg="AR"
    """
     cur = db.cursor()
     data = cur.execute(query).fetchall()
     db.close()
     return data

def display_WK_players_name():
    db = sqlite3.connect('database.db')
    query = """
    SELECT player ,value,matches ,runs FROM stats WHERE ctg="WK"
    """
    cur = db.cursor()
    data = cur.execute(query).fetchall()
    db.close()
    return data


def check_player_role(player):
    db = sqlite3.connect('database.db')
    query="""
    SELECT ctg FROM stats WHERE player=?
    """
    cur = db.cursor()
    cur.execute(query,(player,))
    row=cur.fetchone()
    db.close()
    return row[0]

def get_player_value(player):
    db = sqlite3.connect('database.db')
    query="""
        SELECT value FROM stats where player=?
    """
    cur = db.cursor()
    cur.execute(query,(player,))
    row=cur.fetchone()
    db.close()
    return row[0]


cursor.execute(match)
cursor.execute(teams)
cursor.execute(stats)


conn.close()
