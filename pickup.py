#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 14:02:09 2018

@author: Nik
"""
from operator import attrgetter
import pickle
import random

def main():
    
    choice = input("To see players enter 1,\nTo add players enter 2,\
                   \nTo temp remove players and then make teams enter 3,\
                   \nTo make a random team enter 4,\
                   \nTo permenently remove players enter 5,\
                   \nTo edit a player enter 6\
                   \nTo make teams enter 7,\
                   \nTo make random fair teams enter 8\
                   \nTo exit enter exit:")
    
    if choice == "1":
        
        print("\nForwards"+"("+str(len(open_forwards()))+")")
        print("\nName \t\t Skill \t Speed \t Position\n"+"-"*38)
        for i in open_forwards():
            print(i.get_name(),"\t\t",i.get_skill(),"\t",i.get_speed(),"\t",i.get_position())
        
        print("\nDefensemen"+"("+str(len(open_defense()))+")")
        print("\nName \t\t Skill \t Speed \t Position\n"+"-"*38)
        for i in open_defense():
            print(i.get_name(),"\t\t",i.get_skill(),"\t",i.get_speed(),"\t",i.get_position())
            
    elif choice == "2":
        make_list()
        
    elif choice == "3":
        offense_list, defense_list = temp_remove_player()
        
        team1,team1_score,team1_d_score,team2,team2_score,team2_d_score = make_fair_teams(
                offense_list,defense_list)
        
        print("Team 1\n"+"-"*10)
        for i in team1:
            print(i)
        print("\nOffense Score:",team1_score,"Defense Score:",team1_d_score)
        
        print("\nTeam 2\n"+"-"*10)
        for i in team2:
            print(i)
        print("\nOffense Score:",team2_score,"Defense Score:",team2_d_score)
    
    elif choice == "4":
    
        team1,team2 = make_random_teams(open_forwards(),open_defense())
        
        team1_score,team1_d_score,team2_score,team2_d_score = team_score(team1,team2)
        
        print("Team 1\n"+"-"*10)
        for i in team1:
            print(i)
        print("\nOffense Score:",team1_score,"Defense Score:",team1_d_score)
        
        print("\nTeam 2\n"+"-"*10)
        for i in team2:
            print(i)
        print("\nOffense Score:",team2_score,"Defense Score:",team2_d_score)
    
    elif choice == "5":
        remove_player()
        
    elif choice == "6":
        edit_player()
 
    elif choice == "7":
    
        team1,team2 = make_teams(open_forwards(),open_defense())
        team1_score,team1_d_score,team2_score,team2_d_score = team_score(team1,team2)
    
        print("Team 1\n"+"-"*10)
        for i in team1:
            print(i)
        print("\nOffense Score:",team1_score,"Defense Score:",team1_d_score)
        
        print("\nTeam 2\n"+"-"*10)
        for i in team2:
            print(i)
        print("\nOffense Score:",team2_score,"Defense Score:",team2_d_score)
        
    elif choice == "8":
        
        
        team1, team1_score,team1_d_score, team2, team2_score,team2_d_score = make_fair_teams(
                open_forwards(),open_defense())
        
        print("Team 1\n"+"-"*10)
        for i in team1:
            print(i)
        print("\nOffense Score:",team1_score,"Defense Score:",team1_d_score)
        
        print("\nTeam 2\n"+"-"*10)
        for i in team2:
            print(i)
        print("\nOffense Score:",team2_score,"Defense Score:",team2_d_score)
    
    else:
        print("Invalid entry")

class Player:
    def __init__(self,name,position,skill,speed):
        self.name = name
        self.position = position
        self.skill = skill
        self.speed = speed
    
    def get_name(self):
        return(self.name)
    def get_position(self):
        return(self.position)
    def get_skill(self):
        return(self.skill)
    def get_speed(self):
        return(self.speed)

    def set_name(self,name):
        self.name = name
    def set_position(self,position):
        self.position = position
    def set_skill(self,skill):
        self.skill = skill
    def set_speed(self,speed):
        self.speed = speed
        
    def __repr__(self):
        return self.name

def make_list():     
    offense_list = open_forwards()
    defense_list = open_defense()
    
    while True:
        name = input("Name of player:")
        skill = int(input("Skill level (0-10):"))
        speed = int(input("What is the players speed (0-10):"))
        position = input("Is the player a foward or a defenseman(D or F):")
        position = position.upper()
        
        if position == "D":
            position = "Defenseman"
        elif position == "F":
            position = "Forward"
        
        end = input("Enter another player(y/n):")
        name = Player(name,position,skill,speed)

        if name.get_position() == "Defenseman":
            defense_list.append(name)
            
        elif name.get_position() == "Forward":
            offense_list.append(name)

        if end == "n":
            break
    
    file1 = open("forwards","wb")
    pickle.dump(offense_list,file1)
    file1.close()
    
    file2 = open("defense","wb")
    pickle.dump(defense_list,file2)
    file2.close()
    
    return(offense_list,defense_list)
    
    
def make_teams(offense_list,defense_list):
    team1_offense = []
    team1_defense = []
    team2_offense = []
    team2_defense = []
    count = 1

    
    offense_list = sorted(offense_list, key =attrgetter("skill"))
    defense_list = sorted(defense_list, key =attrgetter("skill"))
    
    for i in offense_list:
        if count % 2 == 0:
            team1_offense.append(i)
        else:
            team2_offense.append(i)
        count+=1

    for i in defense_list:
        if count % 2 == 1:
            team1_defense.append(i)
        else:
            team2_defense.append(i)
        count+=1
    
   
    team1 = team1_offense + team1_defense
    team2 = team2_offense + team2_defense
    
    return(team1,team2)

def open_forwards():
    try:
        file = open("forwards","rb")
        list1 = pickle.load(file)
        file.close()
    except:
        list1 = []
    return(list1)
    
def open_defense():
    try:
        file = open("defense","rb")
        list1 = pickle.load(file)
        file.close()
    except:
        list1 = []
    return(list1)
    
def temp_remove_player():
    offense_list = open_forwards()
    defense_list = open_defense()
    
    name = input("Enter a player to remove:")
    
    for i in range(len(offense_list)):
        try:
            if str(offense_list[i]) == name:
                del offense_list[i]
                
        except:
            continue
        
    for i in range(len(defense_list)):
        try:
            if str(defense_list[i]) == name:
                del defense_list[i]
        except:
            continue

    return(offense_list,defense_list)
        
    
def remove_player():
    offense_list = open_forwards()
    defense_list = open_defense()
    
    name = input("Enter a player to remove:")
    
    for i in range(len(offense_list)):
        try:
            if str(offense_list[i]) == name:
                del offense_list[i]

        except:
            continue
        
    for i in range(len(defense_list)):
        try:
            if str(defense_list[i]) == name:
                del defense_list[i]
        except:
            continue
    
    for i in offense_list:
        print(offense_list)
        
    file1 = open("forwards","wb")
    pickle.dump(offense_list,file1)
    file1.close()
    
    file2 = open("defense","wb")
    pickle.dump(defense_list,file2)
    file2.close()
    
def edit_player():
    offense_list = open_forwards()
    defense_list = open_defense()
    done = False
    
    name = input("What is the name of the player you want to edit:")
    choice = input("what would you like to edit(Enter: 1 for name, 2 for skill, 3 for speed,\
4 to switch position):")
    
    if choice == "1":
        new_name = input("Enter the new name:")
        for i in range(len(offense_list)):
            try:
                if str(offense_list[i]) == name:
                    offense_list[i].set_name(new_name)
                
            except:
                continue
        
        for i in range(len(defense_list)):
            try:
                if str(defense_list[i]) == name:
                    defense_list[i].set_name(new_name)
            except:
                continue

    elif choice == "2":
        new_skill = int(input("Enter the new skil level(0-10):"))
        for i in range(len(offense_list)):
            try:
                if str(offense_list[i]) == name:
                    offense_list[i].set_name(new_skill)
                
            except:
                continue
        
        for i in range(len(defense_list)):
            try:
                if str(defense_list[i]) == name:
                    defense_list[i].set_name(new_skill)
            except:
                continue
                    
    elif choice == "3":
        new_speed = int(input("Enter the new speed (0-10):"))
        for i in range(len(offense_list)):
            try:
                if str(offense_list[i]) == name:
                    offense_list[i].set_name(new_speed)
                
            except:
                continue
        
        for i in range(len(defense_list)):
            try:
                if str(defense_list[i]) == name:
                    defense_list[i].set_name(new_speed)    
            except:
                continue    
                    
    elif choice == "4":
        for i in range(len(offense_list)):
            try:
                if str(offense_list[i]) == name:
                    offense_list[i].set_position("Defenseman")
                    defense_list.append(offense_list[i])
                    print(i)
                    del offense_list[i]
                    done = True
            except:
                continue

            
        
        for i in range(len(defense_list)):
            if done == True:
                break
            try:
                if str(defense_list[i]) == name:
                    defense_list[i].set_position("Forward")
                    offense_list.append(defense_list[i])
                    del defense_list[i]
            except:
                
                continue
                
    
    file1 = open("forwards","wb")
    pickle.dump(offense_list,file1)
    file1.close()
    
    file2 = open("defense","wb")
    pickle.dump(defense_list,file2)
    file2.close()    
    
def make_random_teams(offense_list,defense_list):
    sorted_offense_list = []
    sorted_defense_list = []
    
    rand_o_list = []
    rand_d_list = []
    
    team1_offense = []
    team1_defense = []
    team2_offense = []
    team2_defense = []
    count = 1
    
    
    for i in range(len(offense_list)):
        rand_o_list.append(i)
    
    for i in range(len(defense_list)):
        rand_d_list.append(i)
       
    for i in range(len(offense_list)):
        sorted_offense_list.append(i)
    
    for i in range(len(defense_list)):
        sorted_defense_list.append(i)
    
    for i in defense_list:
        rand1 = random.randint(0,len(rand_d_list)-1)
        rand2 = rand_d_list[rand1]
        del rand_d_list[rand1]
        sorted_defense_list[rand2]=i

    for i in offense_list:
        rand1 = random.randint(0,len(rand_o_list)-1)
        rand2 = rand_o_list[rand1]
        del rand_o_list[rand1]
        sorted_offense_list[rand2]=i
        
    for i in sorted_offense_list:
        if count % 2 == 0:
            team1_offense.append(i)
        else:
            team2_offense.append(i)
        count+=1
        
    for i in sorted_defense_list:
        if count % 2 == 0:
            team1_defense.append(i)
        else:
            team2_defense.append(i)
        count+=1
    
   
    team1 = team1_offense + team1_defense
    team2 = team2_offense + team2_defense
    
    return(team1,team2)   
    
    
def team_score(team1,team2):
    team1_score = 0
    team2_score = 0
    team1_d_score = 0
    team2_d_score = 0
    
    for i in team1:
        if str(i.get_position()) == "Forward":
            x = i.get_skill()
            team1_score += x
        elif str(i.get_position()) == "Defenseman":
            x = i.get_skill()
            team1_d_score += x
    
    for i in team2:
        if str(i.get_position()) == "Forward":
            x = i.get_skill()
            team2_score += x
        elif str(i.get_position()) == "Defenseman":
            x = i.get_skill()
            team2_d_score += x
            
    return(team1_score,team2_score,team1_d_score,team2_d_score)
    
def make_fair_teams(o_list,d_list):

    while True:
        team1, team2 = make_random_teams(o_list,d_list)
        team1_score,team2_score,team1_d_score,team2_d_score = team_score(team1,team2)
        
        d_score_difference = team1_d_score - team2_d_score
        o_score_difference = team1_score - team2_score
        
        if abs(o_score_difference) < 3 and abs(d_score_difference) < 3:
            break
   

    return(team1,team1_score,team1_d_score,team2,team2_score,team2_d_score)
    
main() 
    
    
    
    
    
    
    
    
    
    
    