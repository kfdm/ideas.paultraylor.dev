from pathlib import Path

import frontmatter

content = Path(__file__).parent.parent / "content"
ideas = content / "projects"
retired = content / "retired"


def move(post, src):
    section = src.relative_to(content).parent
    alias = f"/{section}/{src.stem}"
    dst = content / post["status"] / src.name
    print(alias, dst)

    post.metadata.setdefault("aliases", []).append(f"/{section}/{src.stem}")


for src in content.glob("**/*.md"):
    print("Fixing file extension for", src.relative_to(content))
    src.rename(src.with_suffix(".markdown"))

for src in ideas.glob("**/*.markdown"):
    update = False
    print("Checking frontmatter for", src.relative_to(ideas))
    post = frontmatter.load(src)

    if "status" not in post:
        post["status"] = "brainstorm"
    if post["status"] == "missing":
        post["status"] = "brainstorm"

    # Move
    section = src.relative_to(content).parent
    alias = f"/{section}/{src.stem}"
    dst = content / post["status"] / src.name
    post.metadata.setdefault("aliases", []).append(f"/{section}/{src.stem}")
    post.metadata.pop("status", None)
    if "aliases" in post.metadata:
        post["aliases"] = list(set(post["aliases"]))
    update = True

    dst.parent.mkdir(exist_ok=True)
    src.rename(dst)

    if update:
        with dst.open("w", encoding="utf8") as fp:
            fp.write(frontmatter.dumps(post, indent=4))
            fp.write("\n")
        print("Updated", src.relative_to(content))
