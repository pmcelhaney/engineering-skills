"""Validate this collection's plain-scalar metadata and packaging without dependencies."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
expected = {"prepare-code-self-review", "repository-learning"}
skills = list((ROOT / "skills").glob("*/SKILL.md"))
assert {p.parent.name for p in skills} == expected
for skill in skills:
    text = skill.read_text()
    assert text.startswith("---\n"), skill
    front, body = text[4:].split("\n---\n", 1)
    fields = dict(line.split(": ", 1) for line in front.splitlines())
    assert set(fields) == {"name", "description"}
    name = fields["name"]
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
    assert len(name) <= 64 and name == skill.parent.name
    assert 1 <= len(fields["description"]) <= 1024
    assert len(text.splitlines()) < 500
    license_text = (skill.parent / "LICENSE").read_text()
    assert license_text.startswith("MIT License\n")
    assert "Copyright (c) 2026 Patrick McElhaney" in license_text

self_review = (ROOT / "skills/prepare-code-self-review/SKILL.md").read_text()
for safeguard in (
    "grants no blanket permission", "share private information",
    "comment-only review", "Never approve your own PR",
    "Read existing self-review comments first", "Read back the published review",
    "If only preparation or drafting is authorized", "exact current path",
    "Distinguish passed, failed, and not run",
):
    assert safeguard in self_review, safeguard
learning = (ROOT / "skills/repository-learning/SKILL.md").read_text()
for safeguard in (
    "No learning and no guidance edit", "same PR", "AGENTS.md",
    "temporary workarounds", "unrelated PR", "Do not invent a lesson",
    "grants no blanket authority", "private transcripts", "canonical",
    "Learning found: No", "Guidance updated: No",
):
    assert safeguard in learning, safeguard

for doc in ROOT.rglob("*.md"):
    if ".git" in doc.parts:
        continue
    for link in re.findall(r"\]\(([^)]+)\)", doc.read_text()):
        if "://" not in link and not link.startswith("#"):
            target = (doc.parent / link.split("#", 1)[0]).resolve()
            assert target.is_relative_to(ROOT) and target.exists(), (doc, link)
example = (ROOT / "examples/self-review.md").read_text()
patch = example.split("```diff\n", 1)[1].split("```", 1)[0]
old, new = [], []
for line in patch.splitlines():
    if line.startswith(("diff ", "---", "+++", "@@")):
        continue
    if line.startswith((" ", "-")):
        old.append(line[1:])
    if line.startswith((" ", "+")):
        new.append(line[1:])
assert len(old) == 3 and len(new) == 12
assert "method ===" in new[2] and "response.status" in new[6]
assert "src/catalog.ts:3" in example and "src/catalog.ts:7" in example
assert "fictional" in example and "Not run" in example
learning_example = (ROOT / "examples/repository-learning.md").read_text()
assert "Learning found: No" in learning_example
assert "Guidance updated: No" in learning_example
readme = (ROOT / "README.md").read_text()
for name in expected:
    assert f"skills@1.7.4 add pmcelhaney/engineering-skills --skill {name}" in readme
assert "Copyright (c) 2022 Patrick McElhaney" in (ROOT / "LICENSE").read_text()
print("PASS: two skills, metadata, bundled licenses, links, examples, safeguards")
