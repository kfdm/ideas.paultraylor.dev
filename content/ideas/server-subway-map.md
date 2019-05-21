---
title: Server Subway Map
date: 2019-05-21T05:13:05.000Z
tags:
  - hackathon
  - javascript
---

# Example API

```javascript
var chart = new SubwayDiagram('document-id')
var prometheus = chart.addNode('Prometheus')
var promgen = chart.addNode('Promgen', {'popover-id': 'promgen-popover'})
var alertmanager = chart.addNode('AlertManager')
chart.addConnection(prometheus, alertmanager, {'style':'dashed'})
chart.addConnection(alertmanager, promgen, {'style':'dashed'})
chart.addConnection(promgen, prometheus, {'color':'yellow'})
```

# References

- <http://memoryunderground.com/>
- <https://en.wikipedia.org/wiki/Wikipedia:Route_diagram_template>
- <https://mermaidjs.github.io>
