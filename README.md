# Agent Prompt Autoresearch

Multivariate testing for AI-generated pull requests.

## How it works

1. Agent calls `python scripts/get_variant.py --task "TICKET-123"` before writing code
2. Agent follows the returned instructions and includes the tracking tag in the PR body
3. GitHub Action scores CI result, review rounds, and merge outcomes
4. After 20 PRs per variant, the system evaluates and recommends a winner

## Quick start

```bash
# Local simulation (no token needed)
python scripts/setup_test_repo.py --simulate

# Real repo
export GITHUB_TOKEN=ghp_your_token
python scripts/setup_test_repo.py --repo yourname/test-autoresearch
```

## Files

```
.github/
  workflows/autoresearch.yml     GitHub Action trigger
  copilot-instructions.md        Permanent agent instructions

.repo-autoresearch/
  experiment.yaml                Edit this to configure the experiment
  variants/
    baseline.md                  Control group instructions
    compact-diff.md              Challenger instructions
  evidence-templates/
    standard.md                  Evidence block field reference
  reports/
    state.json                   Accumulated PR run data (auto-generated)
    latest-summary.md            Latest experiment report (auto-generated)

scripts/
  get_variant.py                 Agent calls this before writing code
  autoresearch.py                GitHub Action engine
  setup_test_repo.py             This file

skill/
  SKILL.md                       Claude Code skill for automatic integration
  scripts/get_variant.py         Bundled script for the skill
  references/fallback.md         Manual variant assignment instructions
```

https://github.com/surajitkar/autoresearch-smoke-test
