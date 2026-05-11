#!/usr/bin/env python3
# Norwegian Altinn 2 → Altinn 3 migration map (zero-auth, free).
import json, os, sys, urllib.request
APIER_BASE_URL = os.environ.get('APIER_BASE_URL', 'https://www.apier.no')
try:
    with urllib.request.urlopen(f'{APIER_BASE_URL}/api/v1/tools/altinn-migration') as r:
        body = json.load(r)
except Exception as e:
    print(f'Request failed: {e}', file=sys.stderr); sys.exit(1)
if not body.get('data', {}).get('mappings'):
    print('No mappings in response', file=sys.stderr); sys.exit(1)
print(json.dumps(body, indent=2))
# Production integration: https://apier.no/docs
