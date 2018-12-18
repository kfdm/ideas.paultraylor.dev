---
layout: post
title: Todo List using Markdown Database
tags:
- todo
- markdown
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

* Body of the document corresponds to the detailed description of the todo
* Body is interpreted as Markdown (same as Jekyll)
* Provide some kind of simple mapping to iCalendar format
* Cache some of the metadata in another format for faster reporting
