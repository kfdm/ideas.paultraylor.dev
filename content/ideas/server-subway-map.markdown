---
title: Server Subway Map
date: 2019-05-21T05:13:05.000Z
status: missing
summary: Visualizing Server layout as a subway map
tags:
  - hackathon
  - javascript
---

# Example Mermaid

```mermaid
graph LR
subgraph Prometheus Server
    Thanos-Sidecar -.-> Prometheus
end

subgraph Web Server
    Grafana>Grafana]
    Grafana --> Promgen
    Grafana --> Thanos-Query
end

subgraph Database
    Alertmanager
    Database
    Redis
end

Grafana --> Prometheus
Promgen --> Prometheus
Thanos-Query -.-> Thanos-Sidecar
Thanos-Sidecar-->S3
Promgen ==> Prometheus
Prometheus -.-> Alertmanager{AM}
Alertmanager --> Promgen
Promgen-->LINE>LINE]
Promgen-->Slack>Slack]
Promgen-->Email>Email]
Thanos-Query-.->Thanos-Storage
Thanos-Storage-->S3((S3))
Promgen---Database((MySQL))
Promgen---Redis((Redis))
```

# Example Javascript

```javascript
var chart = new SubwayDiagram("document-id");
var prometheus = chart.addNode("Prometheus");
var grafana = chart.addNode("Grafana");
var promgen = chart.addNode("Promgen", { "popover-id": "promgen-popover" });
var alertmanager = chart.addNode("AlertManager");

var line1 = chart.addConnection(prometheus, alertmanager, { style: "dashed" });
chart.addConnection(alertmanager, promgen, { style: "dashed" });
chart.addConnection(promgen, prometheus, { color: "yellow" });

chart.addGroup("Web Server", promgen, grafana);
chart.addGroup("Data Server", prometheus);
chart.addGroup("Misc Server", am, db, redis);

grafana.addPopup("#grafana-info");
line1.addPopup("#alertflow");
```

# References

- <http://memoryunderground.com/>
- <https://en.wikipedia.org/wiki/Wikipedia:Route_diagram_template>
- <https://mermaidjs.github.io>
