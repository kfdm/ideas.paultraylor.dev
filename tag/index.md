---
title: Tags
path: /tag/
---

{% assign tags = site.tags | sort %}
{% for tag in tags %}
 <span class="site-tag">
    <a href="/tag/{{ tag | first | slugify | downcase }}/"
        style="font-size: {{ tag | last | size  |  times: 4 | plus: 80  }}%">
            {{ tag[0] | replace:'-', ' ' | downcase }} ({{ tag | last | size }})
    </a>
</span>
{% endfor %}
