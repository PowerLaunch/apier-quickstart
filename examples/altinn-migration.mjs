#!/usr/bin/env node
// Norwegian Altinn 2 → Altinn 3 migration map (zero-auth, free).
const APIER_BASE_URL = process.env.APIER_BASE_URL ?? 'https://www.apier.no';
// Reject non-HTTPS APIER_BASE_URL so a user who's exported a key
// can't be social-engineered into sending it to an attacker-
// controlled host. localhost loopback stays usable for local dev.
const _u = new URL(APIER_BASE_URL);
const _isHttps = _u.protocol === 'https:';
const _isLocalHttp = _u.protocol === 'http:' && (_u.hostname === 'localhost' || _u.hostname === '127.0.0.1');
if (!_isHttps && !_isLocalHttp) {
  throw new Error(`APIER_BASE_URL must use https:// (or http://localhost for local dev). Got: ${APIER_BASE_URL}`);
}
const res = await fetch(`${APIER_BASE_URL}/api/v1/tools/altinn-migration`);
if (!res.ok) { console.error(`HTTP ${res.status} from ${res.url}`); process.exit(1); }
const body = await res.json();
if (!body?.data?.mappings?.length) { console.error('No mappings in response'); process.exit(1); }
console.log(JSON.stringify(body, null, 2));
// Production integration: https://apier.no/docs
