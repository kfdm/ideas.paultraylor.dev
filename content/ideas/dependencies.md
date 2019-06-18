---
title: Project Dependencies
date: '2019-06-10'
mermaid: true
---

```mermaid
graph RL
worklog-->libgit2((libgit2))
worklog-->caldav((caldav))
django-pomodoro-->caldav
todo-bridge-->caldav
worklog-->django((django))


django-pomodoro-->django
ios-pomodoro-->django-pomodoro
server-map-->d3js
salt-bot-->django
export-me-->django
todo-bridge-->django

git-bridge-->django
quickstats-django-->django
quickstats-ios-->quickstats-django
quickstats-bitbar-->quickstats-django

click worklog "http://example.com"
click export-me "https://github.com/kfdm/export-me"
```
