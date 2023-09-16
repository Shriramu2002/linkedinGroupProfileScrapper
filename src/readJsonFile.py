import json
data = {}

with open('data.json', 'r') as json_file:
    data = json_file.read()

data = json.loads(data)
people = data["data"]["groupsDashGroupMembershipsByTypeahead"]["elements"];

for person in people:
    print(person['profile']['publicIdentifier'])



