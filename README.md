# Norwegian <!-- VERIFY VS NORWEGIAN: Altinn 2 -->Altinn 2 → <!-- VERIFY VS NORWEGIAN: Altinn 3 -->Altinn 3 migration, in 10 lines

> **June 19, 2026 — Altinn 2 shuts down.** This quickstart hits
> Apier's free, zero-auth Altinn 2 → Altinn 3 migration bridge so
> you can ship the upgrade before the deadline. Node and Python
> examples both run against production with no setup.

## Get a key in 30 seconds

1. Open https://apier.no/sign-up
2. Verify your email → you'll see an API key starting with `apier_test_`
3. Export it:
   ```bash
   export APIER_TEST_KEY=apier_test_xxxxxxxxxxxx
   ```
4. Run the example below.

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

Input is no parameter; output is the full migration map of <!-- VERIFY VS NORWEGIAN: Altinn 2 -->Altinn 2 service codes (e.g. `A0208`, `A0212`) and their <!-- VERIFY VS NORWEGIAN: Altinn 3 -->Altinn 3 replacements, with migration notes, verification flags, and the deadline in `days_remaining`. Filter to one entry with `?altinn2_code=A0208`.

## Self-hosted or staging

Both examples honor an `APIER_BASE_URL` environment variable. To
point at your own instance or a staging environment:

```bash
export APIER_BASE_URL=https://staging.apier.no
node examples/altinn-migration.mjs
```

Default: `https://www.apier.no` (production).

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
- For OAuth2 server-to-server flows against Norwegian government, see <!-- VERIFY VS NORWEGIAN: Maskinporten -->Maskinporten guide at https://apier.no/docs (PR-089)

## Security

Found a vulnerability? See SECURITY.md.

## License

MIT
