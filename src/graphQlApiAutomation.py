import requests
import json
from lilogin import linkedInLogger
import time
import argparse
import csv


def getPublicIdentifiers(groupNum, headers):
    url = f'https://www.linkedin.com/voyager/api/graphql?variables=(groupUrn:urn%3Ali%3Afsd_group%3A{groupNum},filters:List(),typeaheadQuery:%27%27,start:0,count:10,membershipStatuses:List(OWNER,MANAGER,MEMBER))&&queryId=voyagerGroupsDashGroupMemberships.761e33cf5b40d3dd11120cc27500f62d'
    
    response = requests.get(url, headers=headers)
    total_count = 0

    if response.status_code == 200:
        data = response.json()
        total_count = data["data"]["groupsDashGroupMembershipsByTypeahead"]["paging"]["total"]

    with open('mydata.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
    
        csvwriter.writerow(['Public handle'])

        for i in range(0, 100, 10):
            url = f'https://www.linkedin.com/voyager/api/graphql?variables=(groupUrn:urn%3Ali%3Afsd_group%3A{groupNum},filters:List(),typeaheadQuery:%27%27,start:{i},count:10,membershipStatuses:List(OWNER,MANAGER,MEMBER))&&queryId=voyagerGroupsDashGroupMemberships.761e33cf5b40d3dd11120cc27500f62d'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()  # Assuming the response contains JSON data
                # Specify the file name
                people = data["data"]["groupsDashGroupMembershipsByTypeahead"]["elements"];

                for person in people:
                    if(person is not None and person['profile'] is not None and person['profile']['publicIdentifier'] is not None):
                        print(person['profile']['publicIdentifier'])
                        csvwriter.writerow([person['profile']['publicIdentifier']])
            
            else:
                print(f"Request failed with status code {response.status_code}:")
                print(response.text)  # Print the response content for debugging
            
            time.sleep(2)

        
        csvfile.close()

    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A LinkedinGroupMemberProfileScrapper with command-line arguments")
    parser.add_argument("username", help="Username of your linkedin handle")
    parser.add_argument("password", help="Password of your linkedin handle")
    parser.add_argument("group_name", help="Group to be scrapped")

    args = parser.parse_args()

    # print(f"Username: {args.username}")
    # print(f"Password: {args.password}")
    # print(f"GroupName: {args.group_name}")


    myLogger = linkedInLogger()
    time.sleep(2)
    myLogger.login_to_linkedin(args.username, args.password)
    time.sleep(4)
    groupNum = myLogger.getGroupNum(args.group_name)
    time.sleep(6)
    [cookie, csrfToken] = myLogger.getCreds()
    time.sleep(8)


    headers = {
        'Cookie':cookie,
        'Csrf-Token' :csrfToken
    }

    getPublicIdentifiers(groupNum, headers)



