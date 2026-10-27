# Engineering Skills

Useful lessons can disappear when a task ends, and a pull request can leave reviewers guessing about the decisions that matter. This collection gives coding agents two complementary workflows:

| Skill | Helps with |
| --- | --- |
| [Prepare Code Self-Review](skills/prepare-code-self-review/SKILL.md) | Explain consequential choices on the current diff, report verification honestly, and request focused human feedback. Publish actual review comments when authorized. |
| [Repository Learning](skills/repository-learning/SKILL.md) | Capture evidence-backed, reusable lessons in the right repository guidance in the same PR. Make no edit when there is no durable lesson. |

Self-review helps the human reviewing this change. Repository Learning helps contributors doing future work. Neither replaces independent review or grants permission to expand the task.

See the fictional [self-review example](examples/self-review.md) and [repository-learning examples](examples/repository-learning.md), including the no-learning case.

## Install one or both

Requires Git, network access, Node.js 22.20 or later, and npm/npx. Run from the project where you want to install:

```sh
# Code Self-Review only
npx skills@1.7.4 add pmcelhaney/engineering-skills --skill prepare-code-self-review

# Repository Learning only
npx skills@1.7.4 add pmcelhaney/engineering-skills --skill repository-learning

# Both skills in this collection
npx skills@1.7.4 add pmcelhaney/engineering-skills --skill prepare-code-self-review repository-learning
```

The CLI prompts for an agent and installation method. Project installation is the default; inspect the destination before proceeding. Add `-g` only to install across projects. The CLI version is pinned; repository content follows the default branch. Review the source and select a reviewed Git revision when reproducibility matters.

See the third-party CLI's [command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) and [telemetry controls](https://github.com/vercel-labs/skills#telemetry). Public GitHub availability is not a claim of skills.sh listing, OpenAI curation, or universal agent compatibility.

## Manual setup

```sh
git clone https://github.com/pmcelhaney/engineering-skills.git
```

Inspect the desired `skills/<name>/SKILL.md`, then copy its whole directory to the skill location documented by your agent. Keep the folder name and `SKILL.md` intact. Copy both directories for the collection. Review any existing installation before replacing it. If your agent has no skill loader, explicitly supply the chosen file as task instructions; this does not add native discovery or PR tools.

The directories use the [Agent Skills format](https://agentskills.io/specification). No executable skill helpers or tokens are bundled. Agents need access to the task, relevant code, guidance, and test evidence. Posting PR comments additionally needs authenticated PR tooling and authority on the exact destination; otherwise self-review produces drafts. Repository Learning requires edit authority for guidance changes; otherwise it proposes them.

## Use

> Use prepare-code-self-review on my current change. Return draft review comments and an honest verification summary without publishing.

> Before opening the PR for this implementation, use repository-learning. Capture any durable lesson in the existing canonical guidance within this task's scope, or report no learning and make no guidance edit.

> Create a PR for this change in the current repository, use both skills, and publish the self-review comments on that PR before handoff.

Installing or invoking these skills grants no blanket authority to edit instructions, post, push, merge, deploy, or share private information. Follow repository instructions and the user's action and destination scope. A learning check is an author workflow, not a new requirement for reviewing unrelated PRs.

## Existing Code Self-Review users

The [standalone code-self-review repository](https://github.com/pmcelhaney/code-self-review) and its installation links remain available. This is a new shared collection; existing installations do not migrate automatically. Choose one source for a given skill to avoid duplicate installations. No installed skills are changed by publishing this repository.

## Validation and license

Run `python3 scripts/validate.py` for dependency-free packaging checks; CI runs the same command. These checks cover layout, metadata, links, safeguards, and fictional example anchors. They do not establish real-world agent behavior or code correctness.

MIT licensed, with Patrick McElhaney's 2022 and 2026 notices preserved in [LICENSE](LICENSE). See [ATTRIBUTION.md](ATTRIBUTION.md) for pinned sources and the distinction between inherited behavior and standalone enhancements.
