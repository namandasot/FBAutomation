import argparse
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def main(query):
  credentials = GoogleCredentials.get_application_default()
  service = discovery.build('language', 'v1', credentials=credentials)
  service_request = service.documents().analyzeSentiment( body={
        'document': {
          'type': 'PLAIN_TEXT',
          'content': query,
        }
      }
    )
  response = service_request.execute()
  print response
  return response

if __name__ == '__main__':
  query = "This is a very bad project"
  main(query)
