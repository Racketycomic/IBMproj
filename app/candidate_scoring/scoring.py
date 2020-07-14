from app.dbservices import crud

def score_skills(score,username):
    db=crud()
    dicto={}
    dicto = db.search_feature(username, 'candidate_features')
    skill = ["c", "cpp", "c++", "java", "python","SQL"]
    skills=dicto["Skill"]
    for i in skills:
        if i.lower() in skill:
            score=score+100
        else:
            score = score+200
    return score

def score_internships(score,username):
    db = crud()
    companies1=['amazon','google','iisc','microsoft','apple']
    companies2=['tcs','wipro','infosys','mindtree','l&t infotec']
    intern={}
    dicto={}
    dicto=db.search_feature(username,'candidate_features')
    intern=dicto["internship"]
    compney=intern.keys()
    for i in compney:
        if i.lower() in companies1:
            score=score+300
        elif i.lower() in companies2:
            score=score+200
        else:
            score=score+100
    return score

def project_scoring(score,username):
    db = crud()
    proj={}
    dicto={}
    tecnologies1=["ai","ml","deep learning","neural network","clojure"]
    tecnologies2=["flask","django","node js","angular js","react js","ruby","R"]
    dicto=db.search_feature(username,'candidate_features')
    proj=dicto["Project"]
    for i in proj:
        tech=i[0]
        tech=tech.split(",")
        for j in tech:
            if j in tecnologies1:
                score=score+300
            elif i[0].lower() in tecnologies2:
                score=score+200
            else:
                score=score+100
    return score

def achievement_scoring(score,username):
    db=crud()
    dicto={}
    dicto=db.search_feature(username,'candidate_features')
    achivement=dicto["Achievement"]
    score=score+len(achivement)*50
    return score


def hobbi_scoring(score,username):
    db=crud()
    dicto={}
    dicto=db.search_feature(username,'candidate_features')
    hobbi=dicto["Hobbies"]
    score=score+len(achivement)*30
    return score

def totalscoring(username):
    score=0
    score=score_skills(score,username)
    score=score_internships(score,username)
    score=project_scoring(score,username)
    score=achievement_scoring(score,username)
    score=hobbi_scoring(score,username)
    return score
