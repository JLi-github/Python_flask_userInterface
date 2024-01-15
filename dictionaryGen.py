#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

from sqlite3 import connect
#import re
from collections import defaultdict

def OpenGradDict(curs):
    
    sql10 = '''select at.emailID, ft.ResearchInterests from 
    singleAnswers at join labResearchInterests ft  where at.id=ft.id 
    and openingGrad = "Yes"'''
    curs.execute(sql10)
    results=curs.fetchall()
    res=[['Interest']+list(tup) for tup in results]
    interest_dic={}
    for c,a,b in res:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
   
    
    
    sql9 = '''select at.emailID, data.datatypes from singleAnswers at 
    join labDatatypes data where at.id=data.id and openingGrad = "Yes" ''' 
    curs.execute(sql9)
    results=curs.fetchall()
    
    adding=[['Data']+list(tup) for tup in results]
    for c,a,b in adding:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
        
        
    sql10 = '''select at.emailID, sys.expSystems from 
    singleAnswers at join labexpSystems sys where at.id=sys.id and 
    openingGrad = "Yes"'''
    curs.execute(sql10)
    exp_sys=curs.fetchall()
    exp_sys=[['Sys']+list(tup) for tup in exp_sys]
    
    for c,a,b in exp_sys:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
        
    sql10 = '''select at.emailID, rot.rotStudQual from 
    singleAnswers at join rotStudentQuality rot where at.id=rot.id and 
    openingGrad = "Yes"'''
    curs.execute(sql10)
    skill=curs.fetchall()
    skill=[['Skills']+list(tup) for tup in skill]
    
    for c,a,b in skill:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
    return interest_dic
    
    
    #for key, value in interest_dic.items():
        
        #print(key, value)
        #print('\n')

def ThesisDict(curs):
    #conn = connect('DCMB_Faculty-3.db')
    #curs = conn.cursor()
    
    sql10 = '''select at.emailID, ft.ResearchInterests from 
    singleAnswers at join labResearchInterests ft  where at.id=ft.id 
    and thesisComm = "Yes"'''
    curs.execute(sql10)
    results=curs.fetchall()
    res=[['Interest']+list(tup) for tup in results]
    interest_dic={}
    for c,a,b in res:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
   
    
    
    sql9 = '''select at.emailID, data.datatypes from singleAnswers at 
    join labDatatypes data where at.id=data.id and thesisComm = "Yes" ''' 
    curs.execute(sql9)
    results=curs.fetchall()
    
    adding=[['Data']+list(tup) for tup in results]
    for c,a,b in adding:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
        
        
    sql10 = '''select at.emailID, sys.expSystems from 
    singleAnswers at join labexpSystems sys where at.id=sys.id and 
    thesisComm = "Yes"'''
    curs.execute(sql10)
    exp_sys=curs.fetchall()
    exp_sys=[['Sys']+list(tup) for tup in exp_sys]
    
    for c,a,b in exp_sys:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
        
    sql10 = '''select at.emailID, rot.rotStudQual from 
    singleAnswers at join rotStudentQuality rot where at.id=rot.id and 
    thesisComm = "Yes"'''
    curs.execute(sql10)
    skill=curs.fetchall()
    skill=[['Skills']+list(tup) for tup in skill]
    
    for c,a,b in skill:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
    return interest_dic
        
        
def PrelimDict(curs):
    
    sql10 = '''select at.emailID, ft.ResearchInterests from 
    singleAnswers at join labResearchInterests ft  where at.id=ft.id 
    and prelimsComm = "Yes"'''
    curs.execute(sql10)
    results=curs.fetchall()
    res=[['Interest']+list(tup) for tup in results]
    interest_dic={}
    for c,a,b in res:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
   
    
    
    sql9 = '''select at.emailID, data.datatypes from singleAnswers at 
    join labDatatypes data where at.id=data.id and prelimsComm = "Yes" ''' 
    curs.execute(sql9)
    results=curs.fetchall()
    
    adding=[['Data']+list(tup) for tup in results]
    for c,a,b in adding:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
        
        
    sql10 = '''select at.emailID, sys.expSystems from 
    singleAnswers at join labexpSystems sys where at.id=sys.id and 
    prelimsComm = "Yes"'''
    curs.execute(sql10)
    exp_sys=curs.fetchall()
    exp_sys=[['Sys']+list(tup) for tup in exp_sys]
    
    for c,a,b in exp_sys:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
        
    sql10 = '''select at.emailID, rot.rotStudQual from 
    singleAnswers at join rotStudentQuality rot where at.id=rot.id and 
    prelimsComm = "Yes"'''
    curs.execute(sql10)
    skill=curs.fetchall()
    skill=[['Skills']+list(tup) for tup in skill]
    
    for c,a,b in skill:
        if a not in interest_dic:
            interest_dic[a]={}
        if c not in interest_dic[a]:
            interest_dic[a][c]=set()
        interest_dic[a][c].add(b)
    return interest_dic

def main():
    OpenGradDict(curs)
    ThesisDict(curs)
    PrelimDict(curs)

    
if __name__ == "__main__": 
    main()
