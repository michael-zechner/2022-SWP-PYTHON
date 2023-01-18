from random import randint, choice
import sqlite3
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import webbrowser
import requests
from matplotlib import pyplot as plt  

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html', symbols=symbols)

@app.route('/game/<int:code>')
def solve_game(code=-1):
    user_choice, com_choice, result = web_play("WebUser",code)
    return render_template('after_game.html',user=user_choice,com=com_choice,result=result)

@app.route('/statistic')
def statistic():
    stats = ret_stats()
    return render_template('statistic.html',stats=stats)

@app.route('/analyse')
def analyse():
    stats = ret_stats_name()
    return render_template('analyse.html', stats=stats)

@app.route('/stats')
def web_stats():
    pie()
    return render_template('index.html')

def init_db():
    connection = sqlite3.connect('SchereSteinPapier/stats.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Stats
              (Name Text, Win INT, Draw INT, Lose INT, Rock INT,''' +
            '''Spok INT, Paper INT, Lizzard INT, Siccors INT)''')
    return connection, cursor

def save_to_db(name):
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

def play(name):
    user_choice = input("Type in your input (Rock,Paper,Siccors,Lizzard,Spok)\n")
    com_choice = com()
    print(symbols[com_choice] + '\n')
    result = check(int(symbols.index(user_choice)),com_choice)
    count(user_result(result),user_choice)
    save_to_db(name)
    print('Result: ' + who_is_winner(result,name))

def hard(name):
    choices = []
    sql_stmt = "SELECT SUM(Rock), SUM(Spok), SUM(Paper), SUM(Lizzard), SUM(Siccors) FROM Stats Where Name = ?"
    sql_data = [name]
    cursor.execute(sql_stmt,sql_data)
    sql_data = cursor.fetchone()
    for i in range(len(sql_data)):
        for j in range(sql_data[i]):
            choices.append(symbols[i])
    user_choice = input("Type in your input (Rock,Paper,Siccors,Lizzard,Spok)\n")
    com_choice = symbols.index(choice(choices))
    print(symbols[com_choice] + '\n')
    result = check(int(symbols.index(user_choice)),com_choice)
    count(user_result(result),user_choice)
    save_to_db(name)
    print('Result: ' + who_is_winner(result,name))

def impossible(name):
    user_choice = input("Type in your input (Rock,Paper,Siccors,Lizzard,Spok)\n")
    com_choice = int(symbols.index(user_choice)) + 1
    com_choice = 0 if com_choice == 5 else com_choice
    result = check(int(symbols.index(user_choice)),com_choice)
    print('Result: ' + who_is_winner(result,name))

def upload(name):
    sql_stmt = "SELECT SUM(Rock), SUM(Spok), SUM(Paper), SUM(Lizzard), SUM(Siccors) FROM Stats Where Name = ?"
    sql_data = [name]
    cursor.execute(sql_stmt,sql_data)
    sql_data = cursor.fetchone()
    print(sql_data)
    print(symbols)
    data = {'rock' : sql_data[0],
            'spok' : sql_data[1],
            'paper' : sql_data[2],
            'lizzard' : sql_data[3],
            'siccors' : sql_data[4]}
    response = requests.put('%s%s' % (host, name), data=data)
    print(response)


def web_play(name, user_choice):
    com_choice = com()
    print(symbols[com_choice] + '\n')
    result = check(user_choice,com_choice)
    count(user_result(result),symbols[user_choice])

    connection = sqlite3.connect('SchereSteinPapier/stats.db')
    cursor = connection.cursor()
    stmt = """INSERT INTO Stats
                (Name, Win, Draw, Lose, Rock, Spok, Paper, Lizzard, Siccors) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data = [name]
    for val in user_stats.values():
        data.append(val)
    cursor.execute(stmt,data)
    connection.commit()

    return symbols[user_choice],symbols[com_choice],who_is_winner(result,name)

def ret_stats():
    connection = sqlite3.connect('SchereSteinPapier/stats.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Stats")
    stats = cursor.fetchall()
    return stats

def ret_stats_name():
    connection = sqlite3.connect('SchereSteinPapier/stats.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Name,SUM(Win) as Wins, SUM(Draw) as Draws,"+
        "SUM(Lose) as Loses, SUM(Rock) as Rock, SUM(Spok) as Spok, Sum(Paper) as Paper,"+
        "Sum(Lizzard) as Lizzard, SUM(Siccors) as Siccors "+
        "FROM Stats GROUP BY Name")
    stats = cursor.fetchall()
    return stats

def highscore():
    print(pd.read_sql_query("SELECT Name, SUM(Win) as Wins FROM Stats GROUP BY Name ORDER BY Wins DESC ", connection))

def console():
    menu = input("Choose a menu point:\n- Back to First Menu (0)\n- Game (1)\n- Statistic (2)\n- Analyse (3)\n- Upload(4)\n- Piechart (5)\n- Hightscore (6)\n\n")
    if menu == "0":
        start()
    elif menu == "1":
        mode = input("Choose a game mode:\n- Normal (1)\n- Hard (2)\n- Impossible (3)\n\n")
        name = input("What is your name?\n")
        if mode == "1":
            play(name)
        elif mode == "2":
            hard(name)
        elif mode == "3":
            impossible(name)
            print("\nMode is just for fun and won't be stored in the database")
    elif menu == "2":
        print(pd.read_sql_query("SELECT * FROM Stats", connection))
    elif menu == "3":
        print(pd.read_sql_query("SELECT DISTINCT(Name) as Alle_Namen FROM Stats", connection))
        name = input("\nWhat is your name?\n")
        print(pd.read_sql_query("SELECT Name,SUM(Win) as Wins, SUM(Draw) as Draws,"+
        "SUM(Lose) as Loses, SUM(Rock) as Rock, SUM(Spok) as Spok, Sum(Paper) as Paper,"+
        "Sum(Lizzard) as Lizzard, SUM(Siccors) as Siccors "+
        "FROM Stats WHERE Name='" + name + "'", connection))
    elif menu == "4":
        name = input("\nWhat is your name?\n")
        upload(name)
    elif menu == "5":
        pie()
    elif menu == "6":
        highscore()
    back = str(input("Do you wanna go back to Menu (Y/N)?\n"))
    if back == "Y":
        console()
    elif back == "N":
        print("Thank you for playing!!")

def start():
    which_mode = input("Choose if you want to play on Webpage (1) or in Console (2)?\n"
    +"Upload Data is only in Console possible because there is a port issue!\n")
    if which_mode == "1":
        webbrowser.open('http://127.0.0.1:5000', new=1, autoraise=True)
        app.run()
    elif which_mode == "2":
        console()

def pie():
    connection = sqlite3.connect('SchereSteinPapier/stats.db')
    cursor = connection.cursor()
    percent = []
    names = []
    cursor.execute("SELECT SUM(WIN) FROM Stats")
    cnt = cursor.fetchone()[0]   
    cursor.execute("SELECT SUM(WIN) FROM Stats GROUP BY Name")
    cnt_user = cursor.fetchall()
    for i in cnt_user:
        percent.append(i[0]/cnt)
    cursor.execute("SELECT DISTINCT(Name) FROM Stats")
    database_names = cursor.fetchall()
    for i in database_names:
        names.append(i[0])

    fig = plt.figure(figsize=(10,7))
    plt.pie(percent,labels=names,autopct='%1.2f%%')
    plt.title("Most Wins!")
    plt.show()

if __name__ == "__main__":
    used_web_name = ""
    host = 'http://127.0.0.1:5000/handling/'
    symbols, user_stats = init()
    connection, cursor = init_db()
    start()