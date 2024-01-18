---
aliases:
  - /ideas/markdowntodo
date: 2018-12-18 00:00:00+00:00
references:
  - http://www.karelia.com/products/the-hit-list/mac.html
  - http://www.karelia.com/products/the-hit-list/iphone.html
  - https://taskwarrior.org/
tags:
  - todo
  - markdown
title: Todo List using Markdown Database
---

Frontmatter could be used for basic Metadata

```yaml
---
title: Todo title
start: 2018-12-18
complete: true
external: http://example.com/..
tags:
  - foo
  - bar
---
```

- Body of the document corresponds to the detailed description of the todo
- Body is interpreted as Markdown (same as Jekyll)
- Provide some kind of simple mapping to iCalendar format
- Cache some of the metadata in another format for faster reporting
