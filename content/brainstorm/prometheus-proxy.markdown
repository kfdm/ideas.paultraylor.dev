---
aliases:
  - /ideas/prometheus-proxy
date: 2019-01-30 00:00:00+00:00
tags:
  - golang
  - prometheus
title: Prometheus Proxy
---

```mermaid
graph LR
grafana --> prometheus
prometheus --> alertmanager
alertmanager --> webhook
```

# Grafana -> Prometheus

- Parse PromQL add labels

```yaml
- hostname: customer.example.com
  plugin: promql
  add_labels:
    service: customer
```

# Prometheus -> Alertmanager

- Parse alert rewrite annotations

# Alertmanager -> Webhook

- Parse alert rewrite annotations

```yaml
- hostname: webhook.example.com
  plugin: alert
  add_label:
    foo: bar
```
