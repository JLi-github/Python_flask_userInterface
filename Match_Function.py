# -*- coding: utf-8 -*-

def findMatch(student,faculty):
    '''Matching Mentors main function. This function takes in a dictionary from the student responses and a nested
    dictionary of faculty responses. Returns the top five matched faculty based on jaccard index of their total 
    match.'''
    dict_keys= ['Interest','Data','Skills','Sys']
    faculty_tot={}
    matched={}
    y=(len(student['Interest']))+(len(student['Data']))+(len(student['Skills']))+(len(student['Sys']))
    for fac in faculty:
        f=faculty[fac]
        x=(len(f['Interest']))+(len(f['Data']))+(len(f['Skills']))+(len(f['Sys']))+y
        faculty_tot.setdefault(fac,[]).append(x)
        for key in dict_keys:
            try:
                match_level_fac=f[key]
                match_level_fac=set(match_level_fac)
            except KeyError:
                continue
            try:
                match_level_student=student[key]
                match_level_student=set(match_level_student)
                if len(match_level_student) <2 and not isinstance(match_level_student,set):
                    match_level_student=set(match_level_student)
            except KeyError:
                continue
            res= match_level_student.intersection(match_level_fac)
            matched.setdefault(fac,[]).append(len(res))
    ret=dict()
    x= dict([(key, sum(values)) for key, values in matched.items()]) #sum of matched values
    d3 = dict((k, float(x[k]) / float(faculty_tot[k][0])-float(x[k])) for k in x) #calculates jaccard index
    s = [(k, d3[k]) for k in sorted(d3, key=d3.get, reverse=True)]
    top_five= s[0:5]
    emails=[]
    score=[]
    for k,v in top_five:
        emails.append(k)
        score.append(v)
    email_score= tuple((emails,score)) #returns typle of emails and scores
    return email_score

