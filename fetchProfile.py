#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fetchProfile(curs, email):
    matchProfiles = {}
    vList =[]
    for emailID in email:
        query=f'''SELECT emailID, firstName, lastName, profile 
        FROM singleAnswers sA 
        INNER JOIN labProfile lP ON sA.id=lP.id 
        WHERE sA.emailID=="{emailID}"'''
        curs.execute(query)
        x = curs.fetchall()
        vList=[x[0][1], x[0][2], x[0][3]]
        matchProfiles.update({x[0][0]:vList})
    return(matchProfiles)