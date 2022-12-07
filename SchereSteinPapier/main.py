from random import randint
import sqlite3
import pandas as pd

def init_db():
    connection = sqlite3.connect('SchereSteinPapier/stats.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Stats
              (Name Text, Win INT, Draw INT, Lose INT, Rock INT,''' +
            '''Spok INT, Paper INT, Lizzard INT, Siccors INT)''')
    return connection, cursor

def save_to_db():
    stmt = """INSERT INTO Stats
                (Name, Win, Draw, Lose, Rock, Spok, Paper, Lizzard, Siccors) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data = [name]
    for val in user_stats.values():
        data.append(val)
    cursor.execute(stmt,data)
    connection.commit()

def init():
    user_stats = {
        'Win':0,
        'Draw':0,
        'Lose':0,
        'Rock':0,
        'Spok':0,
        'Paper':0,
        'Lizzard':0,
        'Siccors':0
    }
    return ["Rock","Spok","Paper","Lizzard","Siccors"], user_stats

def com():
    index = randint(0, len(symbols)-1)
    return index

def check(user,com):
    check_value = (user - com) % 5
    if user == com: return -1
    if check_value == 1 or check_value == 2: return 1
    if check_value == 3 or check_value == 4: return 2

def who_is_winner(value,name):
    if value == 1: return name + " has won!"
    if value == 2: return "Computer has won!"
    return "Draw"

def user_result(value):
    if value==1: return 'Win'
    if value==2: return 'Lose'
    return 'Draw'

def count(result, user):
    user_stats[result] += 1
    user_stats[user] += 1
    pass

def play(name):
    user_choice = input("Type in your input (Rock,Paper,Siccors,Lizzard,Spok)\n")
    com_choice = com()
    print(symbols[com_choice] + '\n')
    result = check(int(symbols.index(user_choice)),com_choice)
    count(user_result(result),user_choice)
    save_to_db()
    print('Result: ' + who_is_winner(result,name))

if __name__ == "__main__":
    symbols, user_stats = init()
    connection, cursor = init_db()
    menu = input("Chose a menu point:\n- Game (1)\n- Statistic (2)\n- Analyse (3)\n\n")
    if menu == "1":
        name = input("What is your name?\n")
        play(name)
    elif menu == "2":
        print(pd.read_sql_query("SELECT * FROM Stats", connection))
    elif menu == "3":
        name = input("What is your name?\n")
        print(pd.read_sql_query("SELECT Name,SUM(Win) as Wins, SUM(Draw) as Draws,"+
        "SUM(Lose) as Loses, SUM(Rock) as Rock, SUM(Spok) as Spok, Sum(Paper) as Paper,"+
        "Sum(Lizzard) as Lizzard, SUM(Siccors) as Siccors "+
        "FROM Stats WHERE Name='" + name + "'", connection))