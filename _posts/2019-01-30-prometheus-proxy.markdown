---
layout: post
title: Prometheus Proxy
mermaid: true
tags:
  - golang
  - prometheus
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
