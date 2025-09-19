---
layout: archive
title: "Connecting the dots"
permalink: /connecting-the-dots/
author_profile: true
---

{% include base_path %}

## Connecting the dots

Welcome to "Connecting the dots" - a space where I explore the intersections between different aspects of my research and how various projects, ideas, and experiences come together to form a cohesive vision.

### Interactive Knowledge Web

<div id="knowledge-web-container" style="width: 100%; height: 600px; border: 1px solid #ddd; border-radius: 8px; margin: 20px 0; position: relative;">
  <div id="knowledge-web" style="width: 100%; height: 100%;"></div>
  <div id="web-controls" style="position: absolute; top: 10px; right: 10px; background: rgba(255,255,255,0.9); padding: 10px; border-radius: 5px; font-size: 12px;">
    <button onclick="resetView()" style="margin: 2px; padding: 5px;">Reset View</button><br>
    <button onclick="addRandomPaper()" style="margin: 2px; padding: 5px;">Add Paper</button><br>
    <span style="color: #666;">Drag to rotate • Scroll to zoom</span>
  </div>
  <div id="paper-info" style="position: absolute; bottom: 10px; left: 10px; background: rgba(255,255,255,0.9); padding: 10px; border-radius: 5px; font-size: 12px; max-width: 300px; display: none;">
    <div id="paper-title"></div>
    <div id="paper-details"></div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>

<script>
// Knowledge Web 3D Visualization
let scene, camera, renderer, controls;
let papers = [];
let connections = [];
let raycaster, mouse;

// Sample papers data - you can easily expand this
const samplePapers = [
  {
    id: 0,
    title: "Topophilia: A Study of Environmental Perceptions, Attitudes, and Values",
    author: "Yi-Fu Tuan",
    type: "book",
    field: "Human Geography",
    position: { x: 0, y: 0, z: 0 }, // Central position
    color: 0xD4AF37, // Gold color for this foundational work
    connections: [1, 3, 5], // Connected to perception-related papers
    isCenter: true,
    file: "/files/papers/topophilia.rtf"
  },
  {
    id: 1,
    title: "Deep Learning for Urban Land Cover Classification",
    type: "paper",
    field: "GeoAI",
    position: { x: -3, y: 1, z: 2 }, // Moved away from center
    color: 0x4CAF50,
    connections: [0, 2, 3]
  },
  {
    id: 2,
    title: "LiDAR Processing for Microclimate Analysis",
    type: "paper",
    field: "Remote Sensing",
    position: { x: 2, y: 3, z: -1 },
    color: 0x2196F3,
    connections: [1, 4]
  },
  {
    id: 3,
    title: "Human Perception of Urban Environments",
    type: "paper",
    field: "Human-Environment",
    position: { x: 3, y: -2, z: 1 },
    color: 0xFF9800,
    connections: [0, 1, 5] // Connected to Topophilia
  },
  {
    id: 4,
    title: "Climate Resilience Planning",
    type: "book",
    field: "Urban Planning",
    position: { x: -2, y: -2, z: -2 },
    color: 0x9C27B0,
    connections: [2, 5]
  },
  {
    id: 5,
    title: "Ecosystem Services Assessment",
    type: "paper",
    field: "Environmental Science",
    position: { x: 1, y: -3, z: 2 },
    color: 0xF44336,
    connections: [0, 3, 4] // Connected to Topophilia
  }
];

function initKnowledgeWeb() {
  const container = document.getElementById('knowledge-web');
  
  // Scene setup
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0xf8f9fa);
  
  // Camera setup
  camera = new THREE.PerspectiveCamera(75, container.offsetWidth / container.offsetHeight, 0.1, 1000);
  camera.position.set(5, 5, 5);
  
  // Renderer setup
  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(container.offsetWidth, container.offsetHeight);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  container.appendChild(renderer.domElement);
  
  // Controls
  controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
  
  // Lighting
  const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
  scene.add(ambientLight);
  
  const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
  directionalLight.position.set(10, 10, 5);
  directionalLight.castShadow = true;
  scene.add(directionalLight);
  
  // Raycaster for mouse interaction
  raycaster = new THREE.Raycaster();
  mouse = new THREE.Vector2();
  
  // Create papers and connections
  createPapers();
  createConnections();
  
  // Event listeners
  container.addEventListener('mousemove', onMouseMove, false);
  container.addEventListener('click', onMouseClick, false);
  window.addEventListener('resize', onWindowResize, false);
  
  // Start animation
  animate();
}

function createPapers() {
  samplePapers.forEach(paperData => {
    const paper = createPaperObject(paperData);
    papers.push({ object: paper, data: paperData });
    scene.add(paper);
  });
}

function createPaperObject(paperData) {
  const group = new THREE.Group();
  
  // Create paper/book geometry - special size for central book
  let geometry;
  if (paperData.isCenter) {
    // Make the central book larger and more prominent
    geometry = new THREE.BoxGeometry(0.8, 1.0, 0.25);
  } else if (paperData.type === 'paper') {
    geometry = new THREE.BoxGeometry(0.6, 0.8, 0.05);
  } else {
    geometry = new THREE.BoxGeometry(0.5, 0.7, 0.15);
  }
  
  const material = new THREE.MeshLambertMaterial({ color: paperData.color });
  const mesh = new THREE.Mesh(geometry, material);
  mesh.castShadow = true;
  mesh.receiveShadow = true;
  
  // Add a slight glow effect
  const glowGeometry = new THREE.BoxGeometry(0.65, 0.85, 0.1);
  const glowMaterial = new THREE.MeshBasicMaterial({
    color: paperData.color,
    transparent: true,
    opacity: 0.3
  });
  const glow = new THREE.Mesh(glowGeometry, glowMaterial);
  
  group.add(mesh);
  group.add(glow);
  group.position.set(paperData.position.x, paperData.position.y, paperData.position.z);
  
  // Store reference to data
  group.userData = paperData;
  
  return group;
}

function createConnections() {
  samplePapers.forEach(paper => {
    paper.connections.forEach(connectedId => {
      const connectedPaper = samplePapers.find(p => p.id === connectedId);
      if (connectedPaper && paper.id < connectedId) { // Avoid duplicate connections
        createConnection(paper.position, connectedPaper.position);
      }
    });
  });
}

function createConnection(pos1, pos2) {
  const points = [];
  points.push(new THREE.Vector3(pos1.x, pos1.y, pos1.z));
  points.push(new THREE.Vector3(pos2.x, pos2.y, pos2.z));
  
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ 
    color: 0x999999, 
    transparent: true, 
    opacity: 0.6 
  });
  
  const line = new THREE.Line(geometry, material);
  connections.push(line);
  scene.add(line);
}

function onMouseMove(event) {
  const rect = event.target.getBoundingClientRect();
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
  
  // Highlight hovered papers
  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(papers.map(p => p.object), true);
  
  // Reset all papers
  papers.forEach(paper => {
    paper.object.children[1].material.opacity = 0.3; // Reset glow
  });
  
  if (intersects.length > 0) {
    const hoveredPaper = intersects[0].object.parent;
    hoveredPaper.children[1].material.opacity = 0.6; // Increase glow
    document.body.style.cursor = 'pointer';
    
    // Show paper info
    showPaperInfo(hoveredPaper.userData);
  } else {
    document.body.style.cursor = 'default';
    hidePaperInfo();
  }
}

function onMouseClick(event) {
  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(papers.map(p => p.object), true);
  
  if (intersects.length > 0) {
    const clickedPaper = intersects[0].object.parent;
    const paperData = clickedPaper.userData;
    
    // If the paper has a file, open it
    if (paperData.file) {
      window.open(paperData.file, '_blank');
    }
    console.log('Clicked paper:', paperData.title);
  }
}

function showPaperInfo(paperData) {
  const infoPanel = document.getElementById('paper-info');
  document.getElementById('paper-title').textContent = paperData.title;
  
  let detailsHTML = `<strong>Type:</strong> ${paperData.type}<br><strong>Field:</strong> ${paperData.field}`;
  
  if (paperData.author) {
    detailsHTML += `<br><strong>Author:</strong> ${paperData.author}`;
  }
  
  if (paperData.isCenter) {
    detailsHTML += `<br><em style="color: #D4AF37;">⭐ Central foundational work</em>`;
  }
  
  if (paperData.file) {
    detailsHTML += `<br><a href="${paperData.file}" target="_blank" style="color: #007cba;">📄 View file</a>`;
  }
  
  document.getElementById('paper-details').innerHTML = detailsHTML;
  infoPanel.style.display = 'block';
}

function hidePaperInfo() {
  document.getElementById('paper-info').style.display = 'none';
}

function resetView() {
  camera.position.set(5, 5, 5);
  controls.reset();
}

function addRandomPaper() {
  const newPaper = {
    id: Date.now(),
    title: "New Research Paper",
    type: Math.random() > 0.5 ? 'paper' : 'book',
    field: "New Field",
    position: {
      x: (Math.random() - 0.5) * 8,
      y: (Math.random() - 0.5) * 8,
      z: (Math.random() - 0.5) * 8
    },
    color: Math.random() * 0xffffff,
    connections: []
  };
  
  const paperObject = createPaperObject(newPaper);
  papers.push({ object: paperObject, data: newPaper });
  scene.add(paperObject);
}

function animate() {
  requestAnimationFrame(animate);
  controls.update();
  
  // Gentle rotation of papers
  papers.forEach(paper => {
    paper.object.rotation.y += 0.005;
  });
  
  renderer.render(scene, camera);
}

function onWindowResize() {
  const container = document.getElementById('knowledge-web');
  camera.aspect = container.offsetWidth / container.offsetHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(container.offsetWidth, container.offsetHeight);
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(initKnowledgeWeb, 100); // Small delay to ensure container is ready
});
</script>

### Research Synergies

Here I discuss how my work in GeoAI, remote sensing, and human-environment interactions creates synergies across different domains:

- **Technology meets Environment**: How cutting-edge AI methods can be applied to solve real environmental challenges
- **Data Integration**: Bringing together diverse data sources (satellite imagery, LiDAR, street view, survey data) for comprehensive understanding
- **Scale Connections**: Linking micro-scale observations to macro-scale environmental processes

### Cross-Disciplinary Insights

My interdisciplinary background allows me to see connections between:

- **Geography and Computer Science**: Spatial thinking enhanced by computational methods
- **Environmental Science and AI**: Using machine learning to understand ecosystem dynamics
- **Planning and Technology**: How geospatial technologies inform better urban planning decisions

### Future Directions

This page will evolve to showcase:

- **Emerging Research Themes**: New directions where my interests are converging
- **Collaborative Opportunities**: How different research streams can be combined
- **Innovation Potential**: Where the intersection of my skills and interests might lead to breakthrough insights

---

*This page represents my ongoing effort to synthesize knowledge across domains and identify novel research opportunities at the intersections of my expertise.*