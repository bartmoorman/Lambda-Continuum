import requests

def lambda_handler(event, context):
  method = event['method'] if 'method' in event else head
  timeout = event['timeout'] if 'timeout' in event else 1.0
  allow_redirects = event['allow_redirects'] if 'allow_redirects' in event else True
  verify = event['verify'] if 'verify' in event else True
  try:
    r = requests.request(method, event['url'], timeout=timeout, allow_redirects=allow_redirects, verify=verify)
    return {'success': True, 'total_seconds': r.elapsed.total_seconds(), 'status_code': r.status_code, 'reason': r.reason}
  except requests.exceptions.ReadTimeout:
    return {'success': False, 'reason': 'ReadTimeout'}
  except requests.exceptions.ConnectTimeout:
    return {'success': False, 'reason': 'ConnectTimeout'}
  except requests.exceptions.TooManyRedirects:
    return {'success': False, 'reason': 'TooManyRedirects'}
  except requests.exceptions.URLRequired:
    return {'success': False, 'reason': 'URLRequired'}
  except requests.exceptions.HTTPError:
    return {'success': False, 'reason': 'HTTPError'}
  except requests.exceptions.ConnectionError:
    return {'success': False, 'reason': 'ConnectionError'}
  except requests.exceptions.RequestException:
    return {'success': False, 'reason': 'RequestException'}
