---
aliases:
- /ideas/caldav-proxy
date: 2018-12-19
tags:
- todo
- caldav
title: Caldav to Github/Jira Proxy
---

Proxying different services, so they can be registered in a caldav compatible client

<!--more-->

Intial Prototype

- <https://github.com/kfdm/caldavframework>

```mermaid
sequenceDiagram
    participant Client
    participant Cache
    participant Server

    Note right of Client: Basic Fetch

    Client->>Server: Proxy Request
    Activate Cache
    Server->>Cache: Update cache with values
    Cache->>Client: Return updated cache
    Deactivate Cache

    Note right of Client: Basic PUT
    Client->>Cache: HTTP PUT
    Activate Cache
    Cache->>Server: Post to Server
    Server->>Cache: Update cache
    Cache->>Client: Return to Client
    Deactivate Cache
```
