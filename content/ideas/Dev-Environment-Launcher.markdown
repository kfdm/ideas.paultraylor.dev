---
title: "Dev Environment Launcher"
date: 2022-08-18
status: beta
tags:
  - django
external:
  project: https://git.tsun.dev/kfdm/dev-proxy
---



The goal to create a simple watcher that could help with running one's dev environment. Similar to something like [xinetd], navigating to `one.local` in the above example, would handle spinning up `django runserver {port}` if it was not already running. This would help with the use case where I might be trying to run _many_ django projects at once, but need to set a different port for each. Something like this may already partially be in [launchd] but I need to do some investigation. Perhaps modifying our environment file would automate pushing the config to launchd that's required.

<!--more-->

```yaml
environment:
  - name: one
    host: one.local
    port: 1234
    command: django runserver {port}
  - name: two
    host: two.local
    command: django runserver {port}
```

[xinetd]: https://en.wikipedia.org/wiki/Xinetd
[launchd]: https://en.wikipedia.org/wiki/Launchd
