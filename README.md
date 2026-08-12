# Norwegian Altinn 2 → Altinn 3 migration, in 10 lines

> **The Altinn 2 shutdown deadline was June 19, 2026 — it has passed.**
> If you still have integrations built against Altinn 2 service codes,
> this quickstart hits Apier's free, zero-auth Altinn 2 → Altinn 3
> migration bridge to map each legacy code to its Altinn 3 replacement,
> with migration notes per service. Node and Python examples both run
> against production with no setup.

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

## Get a key in 30 seconds

The sandbox above is enough to explore. Sign up when you want the production
test-mode surface.

1. Open https://apier.no/sign-up
2. Verify your email → you'll see an API key starting with `apier_test_`
3. Export it:
   ```bash
   export APIER_TEST_KEY=apier_test_xxxxxxxxxxxx
   ```
4. Run the example below.

Two prefixes, two different things: `apier_test_` is the production test-mode
key and requires signup, while `apier_sandbox_test_` is the self-generated
keyless sandbox bearer used in the section above.

Free tier: 100 calls / hour. No credit card. The Altinn 2 → Altinn 3
migration bridge example below is zero-auth — you can run it without
a key to see the shape, then bring your key for the rest.

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

Install + run the official Apier MCP server with one command:

```bash
npx @apier-no/mcp@latest --header "X-Apier-Key: $APIER_TEST_KEY"
```

The server speaks the [Model Context Protocol](https://modelcontextprotocol.io)
and exposes Norwegian compliance tools (Brønnøysund, Maskinporten,
Skatteetaten). Wire it into Claude Desktop, Cursor, or any MCP client
via stdio.

Full setup: https://apier.no/docs/mcp

## What's next

- Production integration: see https://apier.no/docs
- Auth-gated endpoints (company context, deadlines, obligations) require an API key — sign up at https://apier.no
- For OAuth2 server-to-server flows against Norwegian government, see the Maskinporten guide at https://apier.no/docs

## Security

Found a vulnerability? See SECURITY.md.

## License

MIT
