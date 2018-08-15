import requests, json

def lambda_handler(event, context):
  print(event)
  timeout = event['timeout'] if 'timeout' in event else 5.0
  allow_redirects = event['allow_redirects'] if 'allow_redirects' in event else True
  verify = event['verify'] if 'verify' in event else True
  try:
    r = requests.get(event['url'], timeout=timeout, allow_redirects=allow_redirects, verify=verify)
    return json.dumps({'total_seconds': r.elapsed.total_seconds(), 'status_code': r.status_code})
  except requests.exceptions.RequestException as exception:
    print(exception)
    return False
