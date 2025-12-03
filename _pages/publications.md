---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find these publications on my **[Google Scholar profile](https://scholar.google.com/citations?user=YguEIS4AAAAJ&hl=en)**. 
The following publications are listed in reverse chronological order (most recent first).

---

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
 