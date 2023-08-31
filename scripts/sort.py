from pathlib import Path
from frontmatter import Frontmatter

base = Path(__file__).parent.parent / 'content'/ 'ideas'

print(base)
for src in base.glob('**/*.md'):
    src.rename(src.with_suffix('.markdown'))

