#!/usr/bin/env node
// Norwegian Altinn 2 → Altinn 3 migration map (zero-auth, free).
const APIER_BASE_URL = process.env.APIER_BASE_URL ?? 'https://www.apier.no';
const res = await fetch(`${APIER_BASE_URL}/api/v1/tools/altinn-migration`);
if (!res.ok) { console.error(`HTTP ${res.status} from ${res.url}`); process.exit(1); }
const body = await res.json();
if (!body?.data?.mappings?.length) { console.error('No mappings in response'); process.exit(1); }
console.log(JSON.stringify(body, null, 2));
// Production integration: https://apier.no/docs
