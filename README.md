# Norwegian <!-- VERIFY VS NORWEGIAN: Altinn 2 -->Altinn 2 → <!-- VERIFY VS NORWEGIAN: Altinn 3 -->Altinn 3 migration, in 10 lines

<!-- VERIFY VS NORWEGIAN: Altinn 2 -->Altinn 2 shuts down 2026-06-19. Every Norwegian developer with <!-- VERIFY VS NORWEGIAN: Altinn 2 -->Altinn 2 role-based integrations must remap to <!-- VERIFY VS NORWEGIAN: Altinn 3 -->Altinn 3 access packages (<!-- VERIFY VS NORWEGIAN: tilgangspakker -->tilgangspakker). This repo shows how — free, zero-auth, no signup.

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

## What's next

- Production integration: see https://apier.no/docs
- Auth-gated endpoints (company context, deadlines, obligations) require an API key — sign up at https://apier.no
- For OAuth2 server-to-server flows against Norwegian government, see <!-- VERIFY VS NORWEGIAN: Maskinporten -->Maskinporten guide at https://apier.no/docs (PR-089)
- Once `@apier/mcp` npm package ships (PR-083), replace the curl flow with `npx @apier/mcp` (TODO)

## Security

Found a vulnerability? See SECURITY.md.

## License

MIT
