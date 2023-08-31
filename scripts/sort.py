from pathlib import Path

import frontmatter

base = Path(__file__).parent.parent / "content" / "ideas"

for src in base.glob("**/*.md"):
    print("Fixing file extension for", src.relative_to(base))
    src.rename(src.with_suffix(".markdown"))

for src in base.glob("**/*.markdown"):
    update = False
    print("Checking frontmatter for", src.relative_to(base))
    post = frontmatter.load(src)
    if "status" not in post:
        print('Missing status for ',src)
        post["status"] = "missing"
        
    if update:
        with src.open("w", encoding="utf8") as fp:
            fp.write(frontmatter.dumps(post))
        print("Updated", src.relative_to(base))
