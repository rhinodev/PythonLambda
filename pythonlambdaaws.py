import boto3

client = boto3.resource('dynamodb')
table = client.Table('phone_numbers')

def lambda_handler(event, context):
    address = event\
        .get("Details", {})\
        .get("ContactData", {})\
        .get("CustomerEndpoint", {})\
        .get("Address", None)
    version  = ['01','02','03','04','05']
    letterscan = {'+':'','0':'0','1':'1','2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PQRS','8':'TUV','9':'W',}
    vanitynum = [""]
    for num in address: 
       store=[]
       for search in letterscan[num]:
           for letter in vanitynum:
               store.append(letter+search)
       vanitynum=store
    first = vanitynum[0]
    second = vanitynum[1]
    third = vanitynum[2]
    results = {"id_1":first,"id_2":second,"id_3":third}
    return results
    for x in range(5):
       table.put_item(
       Item={'version':version[x],'phone': vanitynum[x]}
       );
       
    