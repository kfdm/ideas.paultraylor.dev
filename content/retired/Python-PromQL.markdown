---
aliases:
- /ideas/Python-PromQL
date: '2020-10-05'
status: retired
tags:
- python
- prometheus
- golang
title: PromQL Parser in Python
---

How difficult it would be to re-use some of the yacc stuff for Prometheus' go parser, and make a proper parser for Python.

Alternatively could use setuptools-golang to build a go library that can be exported and used with Python to make a kind of `promtool` Python library. This would mostly be useful for things like checking rules or queries for syntax errors.

# References

- <https://github.com/messense/py-promql-parser>
- <https://github.com/go-python/gopy>
- <https://github.com/asottile/setuptools-golang>
