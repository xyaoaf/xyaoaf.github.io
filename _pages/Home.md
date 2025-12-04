---
layout: archive
permalink: /
# title: "Xihan Yao, UT Austin"
excerpt: "About me"
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---


I am a PhD student at the Department of Geography and the Environment at The University of Texas at Austin. I work in the [GISense Lab](https://sites.utexas.edu/gisense/) and I am advised by Professor [Yuhao Kang](https://scholar.google.com/citations?user=amySMvcAAAAJ&hl=en). My research develops data-driven and GeoAI-powered approaches to understand how the built and natural environment evolve and interact. I integrate multimodal geospatial data, including satellite and aerial imagery, LiDAR, street-level imagery, and human mobility datasets, with computational modeling to analyze environmental processes, assess ecosystem services, and uncover the dynamics of human–environment interactions.

My work aims to build scalable, interpretable tools that support climate resilience, urban sustainability, and equitable environmental planning across heterogeneous and rapidly changing landscapes.

I received my Master's degree in Environmental Planning at University of California, Berkeley, supervised by Professor [Iryna Dronova](https://scholar.google.com/citations?user=qDUBrUMAAAAJ&hl=en&inst=4034227699702668181). I received my BSc degree from The Hong Kong University of Science and Technology.

## Recent News

{% for post in site.posts limit:3 %}
**{{ post.date | date: "%B %Y" }}**  
[{{ post.title }}]({{ post.url }}) ... [Read More]({{ post.url }})

{% endfor %}

[See All News](/News-Posts/)

---

## Highlighted Research

{% for pub in site.publications limit:3 %}
### {{ pub.title }}
{{ pub.excerpt }}  
[Paper]({{ pub.paperurl }})

**Topics:** Research • GeoAI • Environmental Science

{% endfor %}

[See More Research](/publications/)

---

© 2025 Xihan Yao. All rights reserved.
