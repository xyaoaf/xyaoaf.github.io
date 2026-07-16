---
layout: archive
permalink: /
# title: "Xihan Yao, UT Austin"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


I am a PhD student in Geography and the Environment at The University of Texas at Austin, where I work in the [GISense Lab](https://sites.utexas.edu/gisense/) with Professor [Yuhao Kang](https://scholar.google.com/citations?user=amySMvcAAAAJ&hl=en). My research examines how built and natural environments change and interact through GeoAI, spatial analysis, and multimodal geospatial data.

I work with satellite and aerial imagery, LiDAR, street-level imagery, and human mobility data to study environmental processes, ecosystem services, and human–environment interactions. My broader goal is to develop scalable and interpretable methods that support climate resilience, urban sustainability, and equitable environmental planning.

## Recent News

{% for post in site.posts limit:3 %}
**{{ post.date | date: "%B %Y" }}**  
[{{ post.title }}]({{ post.url }}) ... [Read More]({{ post.url }})

{% endfor %}

[See All News](/News-Posts/)

---

## Highlighted Research

{% assign highlighted_publications = site.publications | where: "highlighted", true | sort: "date" | reverse %}
{% for pub in highlighted_publications %}
### {{ pub.title }}
*{{ pub.venue }}*  
[View publication]({{ pub.paperurl }})

{% endfor %}

[View all publications](/publications/)

---

© {{ site.time | date: "%Y" }} Xihan Yao. All rights reserved.
