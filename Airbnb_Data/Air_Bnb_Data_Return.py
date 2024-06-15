import json
def Air_Bnb_Data_Return():
    json_file_path = "/Users/shashankkaundal/Downloads/AirBnbAnalysis/Airbnb_Data/sample_airbnb.json"
    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())
    #val=json.dumps(contents[0])
    return contents