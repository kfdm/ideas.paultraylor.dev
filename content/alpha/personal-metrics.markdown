---
aliases:
  - /ideas/personal-metrics
date: 2019-01-08
external:
  server: https://github.com/quickstats/quickstats-django
tags:
  - postgres
  - prometheus
  - grafana
  - django
  - golang
title: Personal Metrics
---

Personal metrics based on Prometheus and Grafana inspired by [numerous]

![image](/images/personal-metrics.svg)

# API Support

- Support [pushgateway] as a writer
- Support [grafana-simple-json] as a reader
- Support [django-rest-framework] as read/write API
- Support Prometheus [remote_storage] adapter

[django-rest-framework]: https://www.django-rest-framework.org/
[grafana-simple-json]: https://github.com/grafana/simple-json-datasource
[numerous]: https://www.youtube.com/watch?v=c0A9hEUnAOM
[pushgateway]: https://github.com/prometheus/pushgateway
[remote_storage]: https://github.com/prometheus/prometheus/tree/main/documentation/examples/remote_storage/remote_storage_adapter
