# Norwegian Altinn 2 → Altinn 3 migration, in 10 lines

This quickstart calls Apier's free, zero-auth Altinn 2 → Altinn 3
migration map: each legacy Altinn 2 service code with its Altinn 3
replacement and migration notes. The Node and Python examples both run
against production with no setup and no key.

## Try it now — no key needed

No signup, no email, no human in the loop. Everything under
`/api/v1/sandbox/*` answers immediately.

**1. List the test data.** Zero auth. Returns the machine-readable table of
everything the sandbox understands — synthetic orgs, magic scenarios, error
tokens and query knobs — so you can see what to call before you call it.

```bash
curl -sSL 'https://apier.no/api/v1/sandbox/fixtures' | jq .
```

```json
{
  "success": true,
  "data": {
    "schema_version": "1.0.0",
    "public_sandbox_org": "999999999",
    "reserved_test_orgs": [{ "org_number": "999000001", "name": "Sandbox AS", "entity_type": "AS", "data_tier": "tier_1" }],
    "magic_scenarios": [{ "org_number": "999660010", "state": "konkurs", "expected": { "verify_verdict": "fail" } }]
    ...
```

**2. Verify a company.** Org `999660010` is the bankrupt magic-state fixture,
so verification comes back `fail`. The bearer needs no signup — you invent the
suffix after `apier_sandbox_test_` yourself, and it becomes your own isolated
sandbox session.

```bash
curl -sS 'https://www.apier.no/api/v1/sandbox/company/999660010/verify' \
  -H 'Authorization: Bearer apier_sandbox_test_my_first_run' | jq .
```

```json
{
  "success": true,
  "data": {
    "org_number": "999660010",
    "name": "Sandbox Konkurs AS",
    "verification_status": "fail",
    "signals": { "is_active": false, "not_bankrupt": false }
    ...
```

`apier.no` permanently redirects to `www.apier.no`, and cURL drops the
`Authorization` header across that host change — so authenticated calls should
target `www.apier.no` directly.

## Get a key

The sandbox above is enough to explore, and the migration map below needs
no key at all. Sign up when you want real company data.

1. Sign up at https://www.apier.no/sign-up. Sign-up sends a magic link to
   your inbox and issues no key by itself.
2. Open the link. On that first sign-in Apier creates your first key, a
   free-tier key starting with `apr_free_`, and shows it once. Manage your
   keys at https://www.apier.no/dashboard.
3. Export it:
   ```bash
   export APIER_API_KEY=apr_free_<your_key_here>
   ```
4. Send it as a bearer token, with `{org}` replaced by a real 9-digit
   organisation number:
   ```bash
   curl -sS -H "Authorization: Bearer $APIER_API_KEY" \
     'https://www.apier.no/api/v1/company/{org}/summary' | jq .
   ```

Two prefixes, two different things: a real API key is `apr_<tier>_…`
(`apr_free_`, `apr_starter_`, `apr_pro_` or `apr_ent_`) and comes from
sign-up, while `apier_sandbox_test_` is the self-generated keyless sandbox
bearer used in the section above. No key of the older `apier_test_` /
`apier_live_` shape was ever issued. The full key flow, including headless
keys for agents, is at https://www.apier.no/docs/authentication.

## Run it

cURL one-liner:

```bash
curl -sS 'https://www.apier.no/api/v1/tools/altinn-migration' | jq .
```

Node.js:

```bash
node examples/altinn-migration.mjs
```

Python:

```bash
python examples/altinn-migration.py
```

## What it does

Input is no parameter; output is the full migration map of Altinn 2 service codes (e.g. `A0208`, `A0212`) and their Altinn 3 replacements, with migration notes, verification flags, and the cutover status (`deadline_passed`, plus `days_remaining` relative to the 2026-06-19 deadline). Filter to one entry with `?altinn2_code=A0208`.

## Self-hosted or staging

Both examples honor an `APIER_BASE_URL` environment variable. To
point at your own instance or a staging environment:

```bash
export APIER_BASE_URL=https://staging.apier.no
node examples/altinn-migration.mjs
```

Default: `https://www.apier.no` (production).

Only `https://` URLs (or `http://localhost` / `http://127.0.0.1` for local dev) are accepted — the examples reject other schemes so your key is never sent to an untrusted host.

## Try the MCP server (one-shot)

Run the official Apier MCP stdio proxy with one command. It reads
`APIER_API_KEY` from your environment and sends it as
`Authorization: Bearer …`:

```bash
APIER_API_KEY=apr_free_<your_key_here> npx -y @apier-no/mcp@latest
```

The server speaks the [Model Context Protocol](https://modelcontextprotocol.io)
and serves Norwegian company data from open public registers such as
Brønnøysund. Wire it into Claude Desktop, Cursor, or any MCP client via
stdio. The current tool list is served by the keyless discovery endpoint
`GET https://www.apier.no/api/mcp`.

Full setup: https://www.apier.no/docs/mcp

## What's next

- Production integration: see https://www.apier.no/docs
- Auth-gated endpoints (company context, deadlines, obligations) require an API key: see "Get a key" above
- Apier reads open public registers; it submits nothing to government and brokers no government access

## Security

Found a vulnerability? See SECURITY.md.

## License

MIT
