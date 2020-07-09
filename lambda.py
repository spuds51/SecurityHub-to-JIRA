import json

def lambda_handler(event, context):
    # Pull Title from ASFF, map to JIRA Issue Summary
    issueTitle = str(event['detail']['findings'][0]['Title'])
    # Pull Description from ASFF, map to JIRA Issue Description
    issueDescription = str(event['detail']['findings'][0]['Description'])
    # Pull Resources information from ASFF, add to JIRA Issue Description
    issueFindingDetails = str(event['detail']['findings'][0]['Resources'][0]['Id'])

    print("!!!!===========!")    
    print(issueTitle)
    print(issueDescription)
    print(issueFindingDetails)
    print("===============!")

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
