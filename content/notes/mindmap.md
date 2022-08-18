---
title: Mindmap
date: "2019-06-13"
summary: Various connected ideas
toc: true
tags:
  - caldav
  - django
  - ios
  - markdown
  - mqtt
  - prometheus
  - map
---

```mermaid
graph LR

ios-pomodoro((<center>Pomodoro<br>App</center>))
ios-quickstats((<center>QuickStats<br>App</center>))
ios-todo((<center>Markdown<br>Todo</center>))
salt-master{salt-master}

mqtt>MQTT]
grafana>Grafana]
prometheus>Prometheus]
github>GitHub]
jira>JIRA]
fluentd>fluentd]
line>LINE Notify]
slack>Slack]

quickstats-django[QuickStats API]

caldav-github-.->github
caldav-jira-.->jira
django-pomodoro-->commit-proxy
django-pomodoro-->mqtt
ios-pomodoro-->django-pomodoro
ios-pomodoro-->mqtt
ios-quickstats-->quickstats-django
ios-todo-->caldav-github
ios-todo-->caldav-jira
ios-todo-->django-pomodoro

prometheus-->quickstats-django
grafana-->quickstats-django
grafana-->django-pomodoro

salt-master-->fluentd
fluentd-->salt-bot
salt-bot-->slack
salt-bot-->line


click ios-pomodoro "https://github.com/kfdm/ios-pomodoro"
click ios-quickstats "https://github.com/quickstats/ios-quickstats"
click mqtt "https://ideas.paultraylor.dev/tags/mqtt"
click quickstats-django "https://github.com/quickstats/quickstats-django"
click commit-proxy "https://github.com/kfdm/commit-proxy"
click github "https://developer.github.com/v3/"
click jira "https://developer.atlassian.com/cloud/jira/platform/rest/v3/"
click prometheus "https://prometheus.io"
click grafana "https://grafana.net"
click line "https://notify-bot.line.me/"
click slack "https://slack.dev/"

classDef pomodoro-project fill:#f9f,stroke:#333,stroke-width:4px;
class ios-pomodoro,django-pomodoro pomodoro-project

classDef stats-project fill:#ff9,stroke:#333,stroke-width:4px;
class ios-quickstats,quickstats-django stats-project

classDef todo-project fill:#9ff,stroke:#333,stroke-width:4px;
class ios-todo todo-project
class caldav-github todo-project
class caldav-jira todo-project

classDef git-project fill:#9f9,stroke:#333,stroke-width:4px;
class commit-proxy git-project

class quickstats-django personal-project
```
