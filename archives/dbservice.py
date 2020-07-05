from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result,ResultByKey


credentials = {
  "apikey": "ZwD4EUWQHzQHqqnYt7elJHpfNjtfQkeQLqChMu3p5b6E",
  "host": "1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key 9a542a33-f85e-4345-bdd0-8c97e3d73333",
  "iam_apikey_name": "Developers",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/2e7b263041e54839957b91b386c66514::serviceid:ServiceId-d5321ec7-2380-426c-bed7-084291cc9f4e",
  "password": "a3eb3e22cddda14a068eef718f2921048e550f059a6c6e3230e42c51c08a5249",
  "port": 443,
  "url": "https://1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix:a3eb3e22cddda14a068eef718f2921048e550f059a6c6e3230e42c51c08a5249@1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix.cloudantnosqldb.appdomain.cloud",
  "username": "1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix"
}

client = Cloudant(credentials["username"], credentials["password"], url=credentials["url"])
client.connect()

database_name = "login_credentials"
my_database = client.create_database(database_name)

user = {'name': 'Jatin Rajpal 2',
        '_id':"Jatin Rajpal 2",
        'email': 'jatinrajpal57@gmail.com',
        'mobile_number': '017-2019',
        'skills': ['Php', 'Engineering', 'Mobile', 'Communication', 'Hospital',
                   'Android', 'Css', 'Coding', 'Analysis', 'Programming', 'C++',
                   'Java', 'Algorithms', 'Robot', 'C', 'Unix', 'Html', 'Reports',
                   'Design', 'Research', 'System', 'Database', 'Mysql', 'Windows', 'Matlab', 'Os'],
                   'college_name': None, 'degree': ['BE IN INFORMATION SCIENCE AND\nENGINEERING'],
                   'designation': None,
                   'experience': ['AREMA TECHNOLOGIES | ANDROID APPLICATION DEVELOPMENT',
                   'INTERN', 'July - Nov 2019', '• Worked as a full stack developer, using Firebase Real Time Database and',
                     'designed the user interface.', '• Successfully completed the full working of the application with its own',
                      'customized speech recognizer which can accept multiple languages.', 'K.V.NO.1 ,UDAIPUR',
                      '2016 | Rajasthan, India', 'Percentage:82', 'LINKS',
                      'Github:// Jatinrajpal', 'LinkedIn:// Jatinrajpal', 'COURSEWORK', 'UNDERGRADUATE',
                      'Discrete Mathematical Sciencees', 'Unix', 'Object Oriented Analysis Design', 'Data Structures Algorithms',
                      'Theory of Computation', 'Software Engineering', 'Artiﬁcial Intelligence', 'DBMS', 'Algorithm Design and Analysis',
                       'Computer Networks', 'Operating Systems', 'Linear Algebra'],
                    'company_names': None, 'no_of_pages': 1, 'total_experience': 0.0}

my_database = client['login_credentials']

print(my_database)

result = Result(my_database.all_docs,include_docs=True)
print(result)
for i in result:
    print(i)
result[ResultByKey('wanto@wait.com')]

user={'_id':'wanto@wait.com','username':'wanton','passsword':'wanton@123','email':'wanton@wait.com'}
my_document = my_database.create_document(user)

my_document = my_database['Jatin Rajpal']

my_document['email'] = "newemail@emailer.com"
print(my_document)
my_document.save()

result_collection = Result(my_database.all_docs,include_docs=True)

print(result_collection)
for i in result_collection:
    print(i)

print(result_collection[ResultByKey('Jatin Rajpal')])
