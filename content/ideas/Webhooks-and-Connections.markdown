---
title: Webhooks and Connections
date: "2019-06-18"
status: missing
summary: Thinking through various interconnected systems
---

```mermaid
graph LR

slack((slack))
line((Line))
blink((blink))
email((email))

github>GitHub]
docker>DockerHub]
salt-master{salt-master}
promgen[Promgen]

github==>docker
github==>salt-master
docker==>salt-master
salt-master-->slack
salt-master-->line
github-->slack
docker-->slack
prometheus-->alertmanager
alertmanager==>promgen
alertmanager==>outalator
promgen-->slack
promgen-->line
promgen-->email
pomodoro-->blink
pomodoro-->line
alertmanager-->slack

click github "https://developer.github.com/v3/"
click docker "https://hub.docker.com/"
click slack "https://slack.dev/"
click promgen "https://github.com/line/promgen/"
click line "https://notify-bot.line.me/"
click salt-master "/tags/saltstack/"
click prometheus "/tags/prometheus/"
click alertmanager "/tags/prometheus/"
```
