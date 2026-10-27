# Repository Learning: fictional examples

These scenarios, paths, and observations are invented. They do not describe a real project or test run.

## A durable domain lesson

During an authorized generator fix, an agent reproduces a bug: a local schema reference is resolved relative to the process directory instead of the schema file. A focused regression check verifies the corrected behavior. The repository's existing generator skill has no rule about reference roots.

The agent makes this minimal addition to the existing `.agents/skills/schema-generator/SKILL.md` in the same PR:

> Resolve relative schema references from the containing schema file's directory. Include a case where the process directory differs from the schema directory when changing reference resolution.

The PR description records:

```markdown
## Repository learning check

- Learning found: Yes
- Guidance updated: Yes
- Updated file(s): .agents/skills/schema-generator/SKILL.md
- Rationale: The reproduced reference-root bug and focused regression check establish a reusable generator constraint missing from canonical guidance.
```

This belongs to the generator skill. It does not establish a rule for all file paths throughout the repository.

## Cross-cutting convention

An authorized repository-wide maintenance task establishes that all documentation links must be relative to their source file, and the repository's link checker confirms that convention. If existing guidance does not already cover it, a concise rule belongs in `AGENTS.md`. A generator-only observation would not justify that repository-wide rule.

## No learning, no edit

A task changes one button label to approved copy. The agent finds no reusable constraint or missing guidance. It does not invent a skill update:

```markdown
## Repository learning check

- Learning found: No
- Guidance updated: No
- Updated file(s): N/A
- Rationale: This copy change introduced no durable repository lesson.
```

## Already covered, or outside scope

If the generator skill already states the reference-root rule, report learning found but guidance unchanged, and identify the existing section. If the user requested a proposal only, return the suggested guidance as a draft; do not edit the skill, open a PR, or publish the text.

An agent reviewing an unrelated PR does not demand a learning section or count its absence as a defect. It can still report concrete code defects within the authorized review scope.
