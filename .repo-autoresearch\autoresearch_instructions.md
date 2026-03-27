# Autoresearch â€” active instructions
# Variant : compact_diff_v1
# Task    : automate validation checks

# Compact Diff Instructions â€” Challenger Variant v1

You are an AI coding agent contributing to this repository.
This variant tests whether stricter diff-size and description rules
reduce review round trips.

## Hard Rules (no exceptions)

1. **Diff limit: under 200 lines changed.** If your task requires more,
   split it into multiple PRs â€” one logical concern per PR.

2. **Title format:** `<type>(<scope>): <what changed>`
   Examples:
   - `fix(checkout): reject expired discount codes before payment`
   - `feat(auth): add OAuth token refresh on expiry`
   - `refactor(api): centralise error response format`

3. **Description must include all three:**
   - **What changed** â€” 1â€“2 sentences describing the change
   - **Why** â€” 1 sentence explaining the reason
   - **How to verify** â€” specific test names or exact steps a reviewer
     can follow to confirm it works

4. **Tests are mandatory.** If you have not modified or added a test
   file, do not open the PR. Add the tests first.

## Code Quality

- Match the style of the surrounding code exactly.
  No style migrations bundled into logic PRs.
- Remove all debug/temporary code before opening the PR.
- If the evidence block flags missing tests or a large diff,
  fix those issues before requesting review.

## Reviewer Expectation

A reviewer should be able to understand the full change in under
5 minutes. If that is not possible with your current diff, split it.

---
Include this tag in your PR body:
[autoresearch:task=automate validation checks:variant=compact_diff_v1]
