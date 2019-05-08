---
date: 2018-12-19
title: Caldav to Github/Jira Proxy
status: prototype
tags:
  - todo
  - caldav
---

<div class="mermaid">
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
</div>

<script src="https://unpkg.com/mermaid@8.0.0/dist/mermaid.min.js">
<script>mermaid.initialize({startOnLoad:true});</script>
