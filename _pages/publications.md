---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find these publications on my **[Google Scholar profile](https://scholar.google.com/citations?user=YguEIS4AAAAJ&hl=en)**. 
The following publications are listed in reverse chronological order (most recent first).

{% include base_path %}

## Journal articles

{% assign articles = site.publications | where_exp: "p", "p.pubtype != 'proceedings'" | reverse %}
{% for post in articles %}
  {% include archive-single.html %}
{% endfor %}

## Conference proceedings

{% assign proceedings = site.publications | where: "pubtype", "proceedings" | reverse %}
{% for post in proceedings %}
  {% include archive-single.html %}
{% endfor %}
 