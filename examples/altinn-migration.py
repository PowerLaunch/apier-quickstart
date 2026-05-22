#!/usr/bin/env python3
# Norwegian Altinn 2 → Altinn 3 migration map (zero-auth, free).
import json, os, sys, urllib.parse, urllib.request
APIER_BASE_URL = os.environ.get('APIER_BASE_URL', 'https://www.apier.no')
# Reject non-HTTPS APIER_BASE_URL so a user who's exported a key
# can't be social-engineered into sending it to an attacker-
# controlled host. localhost loopback stays usable for local dev.
_u = urllib.parse.urlparse(APIER_BASE_URL)
_is_https = _u.scheme == 'https'
_is_local_http = _u.scheme == 'http' and _u.hostname in ('localhost', '127.0.0.1')
if not (_is_https or _is_local_http):
    raise ValueError(f'APIER_BASE_URL must use https:// (or http://localhost for local dev). Got: {APIER_BASE_URL}')
try:
    with urllib.request.urlopen(f'{APIER_BASE_URL}/api/v1/tools/altinn-migration') as r:
        body = json.load(r)
except Exception as e:
    print(f'Request failed: {e}', file=sys.stderr); sys.exit(1)
if not body.get('data', {}).get('mappings'):
    print('No mappings in response', file=sys.stderr); sys.exit(1)
print(json.dumps(body, indent=2))
# Production integration: https://apier.no/docs
