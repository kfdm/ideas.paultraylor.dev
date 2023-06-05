---
title: Apply Repo Settings from a Config File
date: "2022-09-28"
tags:
  - github
---

Similar to the [repository-settings] app, there should be a way to apply specific repository settings across multiple apps.

```python

@click.argument('org/user')
@click.argument('repo?')
def webhook(org, repo):
    present('http://webhook', kwargs={})
    absent('http://webhook)
    # loop through webhooks
```

[repository-settings]: https://github.com/repository-settings/app
