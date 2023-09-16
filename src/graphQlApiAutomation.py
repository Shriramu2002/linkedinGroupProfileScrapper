import requests
import json
from lilogin import linkedInLogger
import time


def getPublicIdentifiers(groupNum, headers):
    url = f'https://www.linkedin.com/voyager/api/graphql?variables=(groupUrn:urn%3Ali%3Afsd_group%3A{groupNum},filters:List(),typeaheadQuery:%27%27,start:0,count:10,membershipStatuses:List(OWNER,MANAGER,MEMBER))&&queryId=voyagerGroupsDashGroupMemberships.761e33cf5b40d3dd11120cc27500f62d'
    
    response = requests.get(url, headers=headers)
    total_count = 0

    if response.status_code == 200:
        data = response.json()
        total_count = data["data"]["groupsDashGroupMembershipsByTypeahead"]["paging"]["total"]



    for i in range(0, total_count, 10):
        url = f'https://www.linkedin.com/voyager/api/graphql?variables=(groupUrn:urn%3Ali%3Afsd_group%3A{groupNum},filters:List(),typeaheadQuery:%27%27,start:{i},count:10,membershipStatuses:List(OWNER,MANAGER,MEMBER))&&queryId=voyagerGroupsDashGroupMemberships.761e33cf5b40d3dd11120cc27500f62d'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()  # Assuming the response contains JSON data
            # Specify the file name
            people = data["data"]["groupsDashGroupMembershipsByTypeahead"]["elements"];

            for person in people:
                if(person is not None and person['profile'] is not None and person['profile']['publicIdentifier'] is not None):
                    print(person['profile']['publicIdentifier'])
        
        else:
            print(f"Request failed with status code {response.status_code}:")
            print(response.text)  # Print the response content for debugging

    


if __name__ == "__main__":

    myLogger = linkedInLogger()
    time.sleep(2)
    myLogger.login_to_linkedin('shriramuar.201me155@nitk.edu.in', 'Linkedin@2020')
    time.sleep(4)
    groupNum = myLogger.getGroupNum('NIT (KREC) Surathkal')
    time.sleep(6)
    [cookie, csrfToken] = myLogger.getCreds()
    time.sleep(8)


    headers = {
        'Cookie':cookie,
        'Csrf-Token' :csrfToken
    }

    getPublicIdentifiers(groupNum, headers)



