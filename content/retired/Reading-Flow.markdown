---
aliases:
  - /ideas/Reading-Flow
date: "2019-06-18"
status: retired
summary: Thinking about how bookmarks and links flow and are organized
title: Reading Flow
toc: true
---

```mermaid
graph LR

rss((rss))
exportme((ExportMe))

rss-->feedly
feedly-->ifttt
pocket-->ifttt
owntracks-->mqtt
mqtt-->django
ifttt-->django
django-->report
feedly-->pocket
feedly-->exportme
pocket-->exportme

click owntracks "https://owntracks.org/"
click feedly "https://feedly.com/"
click pocket "https://app.getpocket.com/"
click exportme "https://github.com/kfdm/exportme/"
click ifttt "https://github.com/kfdm/exportme/"
```

# ExportMe

[exportme] provides metrics of the various feeds being read

# Pocket

- Useful for collecting links
- Leaves room for improvement when it comes to organizing
- No way to share list

[exportme]: https://github.com/kfdm/exportme/
