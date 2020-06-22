skills = ['python', 'djano', 'flask', 'machine learning', 'artificial intellegence',
 'neural network', 'deep learning', 'ml', 'ai', 'c',
  'c++', 'cpp', 'c#','visual basic', 'r','clojure', 'julia',
   'mysql', 'mongodb', 'android', 'java', 'block chain',
    'git', 'github', 'cloud computing', 'analytical reasoning',
     'mobile application development', 'vedio production', 'sales leadership',
      'data science', 'natural language processing', 'nlp', 'cyber security']  

new_skill = []

def skill_extract(arg_skill):

    for i in arg_skill:
        
        if i.lower() in skills:
            
            new_skill.append(i)
          
    return new_skill
            

    