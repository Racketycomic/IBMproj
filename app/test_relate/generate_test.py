from app.dbservices import crud
import random


def gettestdata(key, dbname, c):
    db = crud()
    doc = db.search_feature(key, 'test_question')
    print(type(doc))
    print(doc)
    l = doc['questions']
    shuffled_doc = random.sample(l, k=c)
    doc = shuffled_doc

    return doc


def gettest(username):
    db = crud()
    doc = []
    docfinal = []
    skillss = []
    dicto = {}
    skill = ["c", "cpp", "c++", "java", "python"]
    dicto = db.search_feature(username, 'candidate_features')

    skills = dicto["Skill"]
    for i in skills:
        if i in skill:
            skillss.append(i)
    length = len(skillss)


    if length == 4:
        doc = gettestdata("C", 'test_question', 5)
        doc1 = gettestdata("CPP", 'test_question', 5)
        doc2 = gettestdata("Java", 'test_question', 5)
        doc3 = gettestdata("python", 'test_question', 5)
        docfinal = doc+doc1+doc2+doc3
        return (docfinal)
    elif length == 3:
        j = 0
        for i in skillss:
            if j == 12:
                if i == "c":
                    doc = gettestdata("C", 'test_question', 8)
                elif i == "cpp" or i == "c++":
                    doc = gettestdata("CPP", 'test_question', 8)
                elif i == "java":
                    doc = gettestdata("Java", 'test_question', 8)
                elif i == "python":
                    doc = gettestdata("python", 'test_question', 8)
            else:
                if i == "c":
                    doc = gettestdata("C", 'test_question', 6)
                elif i == "cpp" or i == "c++":
                    doc = gettestdata("CPP", 'test_question', 6)
                elif i == "java":
                    doc = gettestdata("Java", 'test_question', 6)
                elif i == "python":
                    doc = gettestdata("python", 'test_question', 6)
            j = j+6
            docfinal += doc
        return (docfinal)
    elif length == 2:
        for i in skillss:
            if i == "c":
                doc = gettestdata("C", 'test_question', 10)
            elif i == "cpp" or i == "c++":
                doc = gettestdata("CPP", 'test_question', 10)
            elif i == "java":
                doc = gettestdata("Java", 'test_question', 10)
            elif i == "python":
                doc = gettestdata("python", 'test_question', 10)
            docfinal += doc
        return (docfinal)
    else:
        doc = gettestdata(skillss[0], 'test_question', 20)
        return doc
