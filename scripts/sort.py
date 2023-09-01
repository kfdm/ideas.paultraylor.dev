from pathlib import Path

import frontmatter

content = Path(__file__).parent.parent / "content"
ideas = content / "ideas"
retired = content / "retired"

for src in content.glob("**/*.md"):
    print("Fixing file extension for", src.relative_to(content))
    src.rename(src.with_suffix(".markdown"))

for src in ideas.glob("**/*.markdown"):
    update = False
    print("Checking frontmatter for", src.relative_to(ideas))
    post = frontmatter.load(src)
    if "status" not in post:
        post["status"] = "missing"

    if post["status"] == "retired":
        post.metadata.setdefault("aliases", []).append(f"/ideas/{src.stem}")
        src = src.rename(retired / src.name)
        update = True

    if update:
        with src.open("w", encoding="utf8") as fp:
            fp.write(frontmatter.dumps(post, indent=4))
            fp.write("\n")
        print("Updated", src.relative_to(content))
