(function () {
  'use strict';

  var initialView = { x: 0, y: 0, scale: 1 };
  var view = { x: 0, y: 0, scale: 1 };
  var render = function () {};

  var nodes = [
    { id: 'tuan', label: 'Topophilia', author: 'Yi-Fu Tuan', group: 'Spatial theory', x: 0.50, y: 0.48 },
    { id: 'lefebvre', label: 'The Production\nof Space', author: 'Henri Lefebvre', group: 'Critical theory', x: 0.27, y: 0.30 },
    { id: 'lynch', label: 'The Image\nof the City', author: 'Kevin Lynch', group: 'Urban perception', x: 0.25, y: 0.68 },
    { id: 'place', label: 'Space and Place', author: 'Yi-Fu Tuan', group: 'Spatial theory', x: 0.49, y: 0.18 },
    { id: 'psychology', label: 'Environmental\nPsychology', author: 'Selected research concepts', group: 'Human–environment relations', x: 0.72, y: 0.31 },
    { id: 'personality', label: 'Geography and\nPersonality', author: 'Selected empirical studies', group: 'Spatial behavior', x: 0.76, y: 0.65 },
    { id: 'geoai', label: 'GeoAI', author: 'Computational geography', group: 'Methods', x: 0.51, y: 0.80 }
  ];

  var links = [
    ['tuan', 'place'], ['tuan', 'lefebvre'], ['tuan', 'lynch'],
    ['tuan', 'psychology'], ['tuan', 'geoai'], ['lefebvre', 'lynch'],
    ['lynch', 'psychology'], ['psychology', 'personality'],
    ['personality', 'geoai'], ['psychology', 'geoai']
  ];

  var colors = {
    'Spatial theory': '#9a7b2f',
    'Critical theory': '#75558f',
    'Urban perception': '#397e8c',
    'Human–environment relations': '#4f7f58',
    'Spatial behavior': '#ad633f',
    'Methods': '#3d6590'
  };

  window.resetView = function () {
    view.x = initialView.x;
    view.y = initialView.y;
    view.scale = initialView.scale;
    render();
  };

  function initializeKnowledgeWeb() {
    var host = document.getElementById('knowledge-web');
    var info = document.getElementById('paper-info');
    var title = document.getElementById('paper-title');
    var details = document.getElementById('paper-details');
    if (!host || !info || !title || !details) return;

    host.innerHTML = '';
    var canvas = document.createElement('canvas');
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Interactive map connecting readings and concepts in spatial theory, environmental psychology, and GeoAI.');
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.display = 'block';
    canvas.style.cursor = 'grab';
    canvas.style.touchAction = 'none';
    host.appendChild(canvas);

    var context = canvas.getContext('2d');
    if (!context) {
      host.innerHTML = '<p style="padding: 2rem; text-align: center; color: #666;">The interactive map is not supported in this browser. The selected reading list remains available below.</p>';
      return;
    }

    var size = { width: 1, height: 1, ratio: 1 };
    var radius = 43;
    var hovered = null;
    var dragging = false;
    var lastPointer = { x: 0, y: 0 };
    var moved = false;

    function resize() {
      var rect = host.getBoundingClientRect();
      size.width = Math.max(320, rect.width);
      size.height = Math.max(420, rect.height);
      size.ratio = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.round(size.width * size.ratio);
      canvas.height = Math.round(size.height * size.ratio);
      render();
    }

    function screenPosition(node) {
      return {
        x: (node.x * size.width - size.width / 2) * view.scale + size.width / 2 + view.x,
        y: (node.y * size.height - size.height / 2) * view.scale + size.height / 2 + view.y
      };
    }

    function findNode(x, y) {
      for (var i = nodes.length - 1; i >= 0; i -= 1) {
        var point = screenPosition(nodes[i]);
        var dx = x - point.x;
        var dy = y - point.y;
        if (dx * dx + dy * dy <= Math.pow(radius * view.scale, 2)) return nodes[i];
      }
      return null;
    }

    function drawLabel(node, point) {
      var lines = node.label.split('\n');
      context.fillStyle = '#fff';
      context.font = '600 ' + Math.max(10, 12 * view.scale) + 'px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif';
      context.textAlign = 'center';
      context.textBaseline = 'middle';
      lines.forEach(function (line, index) {
        context.fillText(line, point.x, point.y + (index - (lines.length - 1) / 2) * 15 * view.scale);
      });
    }

    render = function () {
      context.setTransform(size.ratio, 0, 0, size.ratio, 0, 0);
      context.clearRect(0, 0, size.width, size.height);

      var gradient = context.createLinearGradient(0, 0, size.width, size.height);
      gradient.addColorStop(0, '#f7f8fa');
      gradient.addColorStop(1, '#eef2f3');
      context.fillStyle = gradient;
      context.fillRect(0, 0, size.width, size.height);

      links.forEach(function (link) {
        var a = screenPosition(nodes.find(function (node) { return node.id === link[0]; }));
        var b = screenPosition(nodes.find(function (node) { return node.id === link[1]; }));
        context.beginPath();
        context.moveTo(a.x, a.y);
        context.lineTo(b.x, b.y);
        context.strokeStyle = 'rgba(77, 91, 101, 0.30)';
        context.lineWidth = Math.max(1, 1.4 * view.scale);
        context.stroke();
      });

      nodes.forEach(function (node) {
        var point = screenPosition(node);
        var nodeRadius = radius * view.scale;
        context.beginPath();
        context.arc(point.x, point.y, nodeRadius, 0, Math.PI * 2);
        context.fillStyle = colors[node.group] || '#526777';
        context.fill();
        context.lineWidth = node === hovered ? 4 : 2;
        context.strokeStyle = node === hovered ? '#24333d' : 'rgba(255,255,255,0.9)';
        context.stroke();
        drawLabel(node, point);
      });
    };

    function pointerPosition(event) {
      var rect = canvas.getBoundingClientRect();
      return { x: event.clientX - rect.left, y: event.clientY - rect.top };
    }

    canvas.addEventListener('pointerdown', function (event) {
      dragging = true;
      moved = false;
      lastPointer = pointerPosition(event);
      canvas.setPointerCapture(event.pointerId);
      canvas.style.cursor = 'grabbing';
    });

    canvas.addEventListener('pointermove', function (event) {
      var point = pointerPosition(event);
      if (dragging) {
        var dx = point.x - lastPointer.x;
        var dy = point.y - lastPointer.y;
        if (Math.abs(dx) + Math.abs(dy) > 2) moved = true;
        view.x += dx;
        view.y += dy;
        lastPointer = point;
      }
      hovered = findNode(point.x, point.y);
      canvas.style.cursor = dragging ? 'grabbing' : (hovered ? 'pointer' : 'grab');
      render();
    });

    canvas.addEventListener('pointerup', function (event) {
      dragging = false;
      canvas.releasePointerCapture(event.pointerId);
      canvas.style.cursor = hovered ? 'pointer' : 'grab';
      if (!moved && hovered) {
        title.textContent = hovered.label.replace('\n', ' ');
        details.textContent = hovered.author + ' · ' + hovered.group;
        info.style.display = 'block';
      }
    });

    canvas.addEventListener('pointerleave', function () {
      if (!dragging) {
        hovered = null;
        render();
      }
    });

    canvas.addEventListener('wheel', function (event) {
      event.preventDefault();
      var point = pointerPosition(event);
      var previousScale = view.scale;
      var nextScale = Math.min(1.8, Math.max(0.65, previousScale * (event.deltaY < 0 ? 1.08 : 0.92)));
      view.x = point.x - (point.x - view.x - size.width / 2) * nextScale / previousScale - size.width / 2;
      view.y = point.y - (point.y - view.y - size.height / 2) * nextScale / previousScale - size.height / 2;
      view.scale = nextScale;
      render();
    }, { passive: false });

    if ('ResizeObserver' in window) {
      new ResizeObserver(resize).observe(host);
    } else {
      window.addEventListener('resize', resize);
    }
    resize();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeKnowledgeWeb);
  } else {
    initializeKnowledgeWeb();
  }
}());
