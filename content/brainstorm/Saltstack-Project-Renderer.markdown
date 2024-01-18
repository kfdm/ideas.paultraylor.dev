---
aliases:
  - /ideas/Saltstack-Project-Renderer
date: 2019-05-19 21:17:42.551725+09:00
tags:
  - saltstack
title: Saltstack Project Renderer
---

Take advantage of Saltstack [Renderers] to reduce the amount of duplicated states

```yaml
#!jinja|custom_render
project:
  user: app-project
  nginx:
    - target: /path/to/nginx.conf/foo
      source: salt://path/to/source
  mysql:
    user: aaa
    database: aaa
    password: aaa
  services:
    web: salt://path/to/web.service
    worker: salt://path/to/worker.service
  repos:
    bar: git@github.com:foo/bar
    baz: git@github.com:foo/baz
  cmd:
    - /path/to/manage
    - /path/to/collect
```

[renderers]: http://docs.saltstack.com/en/latest/ref/renderers/
