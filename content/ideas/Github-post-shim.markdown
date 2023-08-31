---
title: Github Post Shim
date: 2019-05-20T23:46:42.000Z
tags:
  - github
---

Using [this] post as a reference it should be easy to create a simple API to post files to Github

The api I'm considering would look something like this

```bash
curl -u username:token -X POST bridge.example.com/<user>/<repo>/path/to/file < file
```

The Authorization [token] will be passed along with each request

[this]: http://www.levibotelho.com/development/commit-a-file-with-the-github-api/
[token]: https://developer.github.com/v3/auth/#via-oauth-tokens