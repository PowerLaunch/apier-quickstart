# Changelog

All notable changes to apier-quickstart are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] — 2026-05-22

### Added
- "Get a key in 30 seconds" onboarding section in README
- APIER_BASE_URL self-hosted / staging documentation
- Working `npx @apier-no/mcp` one-shot MCP server example
- Dependabot config (.github/dependabot.yml) — weekly npm + pip +
  github-actions
- `.venv/`, `dist/`, `build/` added to `.gitignore`
- CHANGELOG.md (this file)

### Changed
- Stale `@apier/mcp` references corrected to `@apier-no/mcp` (the
  published npm package name as of PR-083 v0.1.1, 2026-05-20)
- June 19, 2026 Altinn 2 shutdown deadline elevated to above-the-fold
  urgency framing

### Fixed
- Removed "Once PR-083 ships" TODO — PR-083 shipped 2026-05-21,
  working `npx @apier-no/mcp` example now in place

## [0.1.0] — 2026-05-11

### Added
- Initial scaffold: Node.js + Python examples hitting the Altinn
  migration bridge at /api/v1/tools/altinn-migration
- GitHub Actions sanity-check workflow with positive-control assertion
- MIT LICENSE
- SECURITY.md → security@apier.no
