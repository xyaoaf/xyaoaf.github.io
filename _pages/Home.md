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


I am a PhD student in Geography and the Environment at The University of Texas at Austin, where I work in the [GISense Lab](https://sites.utexas.edu/gisense/) with Professor [Yuhao Kang](https://scholar.google.com/citations?user=amySMvcAAAAJ&hl=en). My research examines how urban and natural environments relate to the people who live in them.

I trained in environmental management and environmental planning, and I study urban greenery, ecosystem services and local climate: how trees and landscapes shape conditions in neighborhoods, and how those benefits and risks are shared. My broader goal is to support environmental planning that makes cities healthier, more resilient and more equitable.

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
