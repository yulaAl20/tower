import sqlite3
import pandas as pd
from datetime import datetime

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect('tower_of_hanoi.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS game_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT,
        disk_count INTEGER,
        moves_count INTEGER,
        move_sequence TEXT,
        algorithm TEXT,
        execution_time REAL,
        timestamp TEXT
    )
    ''')
    conn.commit()
    conn.close()

def save_result(player_name, disk_count, moves_count, move_sequence, algorithm, execution_time):
    """Save game results to the database."""
    conn = sqlite3.connect('tower_of_hanoi.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO game_results (player_name, disk_count, moves_count, move_sequence, algorithm, execution_time, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (player_name, disk_count, moves_count, move_sequence, algorithm, execution_time, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_leaderboard():
    """Retrieve leaderboard data from the database."""
    conn = sqlite3.connect('tower_of_hanoi.db')
    df = pd.read_sql_query('''
    SELECT player_name, disk_count, moves_count, algorithm, execution_time 
    FROM game_results 
    ORDER BY execution_time ASC
    LIMIT 10
    ''', conn)
    conn.close()
    return df