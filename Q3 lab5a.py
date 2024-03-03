#1. Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty':30}
dict2 = {'Thirty': 30, 'Fourty': 40,'Fifty': 50}
dict3 = (dict1 | dict2)
print(dict3)
#2.Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])
#3 Initialize dictionary with default values
employees = ['Kelly','Emma']
defaults = {"designation": 'Developer',"salary":8000}
res = dict.fromkeys(employees, defaults)
print(res)
        
        
       
    
    
    