---
layout: archive
title: "Connecting the dots"
permalink: /connecting-the-dots/
author_profile: true
---

{% include base_path %}

# Mini-Geo Journey: Theories of Space and Place

Welcome to my **Mini-Geo Journey** - an interactive exploration of how theories of space and place shape my intellectual development and research trajectory toward understanding built-environment-personality relationships.

This visualization represents my intellectual roadmap, demonstrating how foundational spatial theories connect to contemporary research in GeoAI and human-environment interactions. Each node in the web below represents a key reading, and the connections show how ideas flow and build upon one another in my scholarly journey.

## 📊 Interactive Analysis Options

### Option 1: Jupyter Notebook Format 
**🎯 Recommended for Deep Exploration**

<div style="background: #e8f5e9; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #4CAF50;">
  <p><strong>🔬 Interactive Data Analysis:</strong> Explore the complete bibliography dataset with Python code, network visualizations, and interactive widgets.</p>
  
  <p><strong>Key Features:</strong></p>
  <ul>
    <li>📈 Interactive network graphs with clickable nodes</li>
    <li>🔍 Filterable paper explorer by domain, year, and keywords</li>
    <li>📊 Timeline analysis of reading progression</li>
    <li>🎛️ Dynamic visualizations with hover details</li>
    <li>💻 Full Python code for reproducible analysis</li>
  </ul>
  
  <p style="margin-top: 15px;">
    <a href="connecting-the-dots.ipynb" style="background: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">
      🚀 Launch Interactive Notebook
    </a>
  </p>
  
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <em>Best viewed in Jupyter Lab or VSCode. Click nodes to see paper properties, use widgets to filter by domain/year.</em>
  </p>
</div>

### Option 2: 3D Web Visualization 
**🌐 Browser-Based Exploration**

## About This Journey

This interactive knowledge web serves as both:
- **Academic Assignment**: First Mini-Geo Journey focusing on space/place theories for my graduate coursework
- **Research Foundation**: Theoretical groundwork for my built-environment-personality study
- **Intellectual Map**: Visual demonstration of how I engage with spatial theory and connect it to methodological approaches

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
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
// Check if Three.js loaded
if (typeof THREE === 'undefined') {
  document.getElementById('knowledge-web').innerHTML = '<p style="text-align: center; padding: 50px; color: #666;">Loading 3D visualization... Please wait or refresh the page if this message persists.</p>';
  console.error('Three.js failed to load');
}

// OrbitControls definition (inline since CDN might not work)
THREE.OrbitControls = function ( object, domElement ) {
  this.object = object;
  this.domElement = ( domElement !== undefined ) ? domElement : document;
  this.enabled = true;
  this.target = new THREE.Vector3();
  this.enableDamping = false;
  this.dampingFactor = 0.25;
  this.enableZoom = true;
  this.zoomSpeed = 1.0;
  this.enableRotate = true;
  this.rotateSpeed = 1.0;
  this.enablePan = true;
  this.panSpeed = 1.0;
  this.screenSpacePanning = false;
  this.keyPanSpeed = 7.0;
  this.autoRotate = false;
  this.autoRotateSpeed = 2.0;
  this.enableKeys = true;
  this.keys = { LEFT: 37, UP: 38, RIGHT: 39, BOTTOM: 40 };
  this.mouseButtons = { LEFT: THREE.MOUSE.LEFT, MIDDLE: THREE.MOUSE.MIDDLE, RIGHT: THREE.MOUSE.RIGHT };
  
  var scope = this;
  var changeEvent = { type: 'change' };
  var startEvent = { type: 'start' };
  var endEvent = { type: 'end' };
  var STATE = { NONE: - 1, ROTATE: 0, DOLLY: 1, PAN: 2, TOUCH_ROTATE: 3, TOUCH_DOLLY_PAN: 4 };
  var state = STATE.NONE;
  var EPS = 0.000001;
  var spherical = new THREE.Spherical();
  var sphericalDelta = new THREE.Spherical();
  var scale = 1;
  var panOffset = new THREE.Vector3();
  var zoomChanged = false;
  var rotateStart = new THREE.Vector2();
  var rotateEnd = new THREE.Vector2();
  var rotateDelta = new THREE.Vector2();
  var panStart = new THREE.Vector2();
  var panEnd = new THREE.Vector2();
  var panDelta = new THREE.Vector2();
  var dollyStart = new THREE.Vector2();
  var dollyEnd = new THREE.Vector2();
  var dollyDelta = new THREE.Vector2();
  
  this.update = function () {
    var offset = new THREE.Vector3();
    var quat = new THREE.Quaternion().setFromUnitVectors( object.up, new THREE.Vector3( 0, 1, 0 ) );
    var quatInverse = quat.clone().inverse();
    var lastPosition = new THREE.Vector3();
    var lastQuaternion = new THREE.Quaternion();
    
    return function update() {
      var position = scope.object.position;
      offset.copy( position ).sub( scope.target );
      offset.applyQuaternion( quat );
      spherical.setFromVector3( offset );
      if ( scope.autoRotate && state === STATE.NONE ) {
        rotateLeft( getAutoRotationAngle() );
      }
      spherical.theta += sphericalDelta.theta;
      spherical.phi += sphericalDelta.phi;
      spherical.theta = Math.max( 0, Math.min( Math.PI, spherical.theta ) );
      spherical.radius *= scale;
      spherical.radius = Math.max( 0.1, Math.min( 100, spherical.radius ) );
      scope.target.add( panOffset );
      offset.setFromSpherical( spherical );
      offset.applyQuaternion( quatInverse );
      position.copy( scope.target ).add( offset );
      scope.object.lookAt( scope.target );
      if ( scope.enableDamping === true ) {
        sphericalDelta.theta *= ( 1 - scope.dampingFactor );
        sphericalDelta.phi *= ( 1 - scope.dampingFactor );
        panOffset.multiplyScalar( 1 - scope.dampingFactor );
      } else {
        sphericalDelta.set( 0, 0, 0 );
        panOffset.set( 0, 0, 0 );
      }
      scale = 1;
      if ( zoomChanged || lastPosition.distanceToSquared( scope.object.position ) > EPS || 8 * ( 1 - lastQuaternion.dot( scope.object.quaternion ) ) > EPS ) {
        scope.dispatchEvent( changeEvent );
        lastPosition.copy( scope.object.position );
        lastQuaternion.copy( scope.object.quaternion );
        zoomChanged = false;
        return true;
      }
      return false;
    };
  }();
  
  this.reset = function () {
    state = STATE.NONE;
    scope.target.copy( scope.target0 );
    scope.object.position.copy( scope.position0 );
    scope.object.zoom = scope.zoom0;
    scope.object.updateProjectionMatrix();
    scope.dispatchEvent( changeEvent );
    scope.update();
  };
  
  function getAutoRotationAngle() {
    return 2 * Math.PI / 60 / 60 * scope.autoRotateSpeed;
  }
  
  function rotateLeft( angle ) {
    sphericalDelta.theta -= angle;
  }
  
  this.target0 = this.target.clone();
  this.position0 = this.object.position.clone();
  this.zoom0 = this.object.zoom;
};

THREE.OrbitControls.prototype = Object.create( THREE.EventDispatcher.prototype );
THREE.OrbitControls.prototype.constructor = THREE.OrbitControls;

<script>
// Knowledge Web 3D Visualization
let scene, camera, renderer, controls;
let papers = [];
let connections = [];
let raycaster, mouse;

// Sample papers data - representing my space/place theory journey
const samplePapers = [
  {
    id: 0,
    title: "Topophilia: A Study of Environmental Perceptions, Attitudes, and Values",
    author: "Yi-Fu Tuan",
    type: "book",
    field: "Humanistic Geography",
    position: { x: 0, y: 0, z: 0 }, // Central position
    color: 0xD4AF37, // Gold color for this foundational work
    connections: [1, 2, 3, 5], // Connected to perception and experience papers
    isCenter: true,
    description: "Foundational work exploring human emotional bonds with place and environment",
    relevance: "Central to understanding how people develop affective relationships with built environments"
  },
  {
    id: 1,
    title: "Space and Place: The Perspective of Experience",
    author: "Yi-Fu Tuan",
    type: "book",
    field: "Phenomenological Geography",
    position: { x: -3, y: 2, z: 1 },
    color: 0x4CAF50,
    connections: [0, 2, 4],
    description: "Explores the phenomenological distinction between space and place",
    relevance: "Key theoretical framework for understanding spatial experience in built environments"
  },
  {
    id: 2,
    title: "The Poetics of Space",
    author: "Gaston Bachelard",
    type: "book", 
    field: "Phenomenology",
    position: { x: 2, y: 3, z: -1 },
    color: 0x2196F3,
    connections: [0, 1, 6],
    description: "Phenomenological investigation of the psychological significance of spatial forms",
    relevance: "Connects spatial psychology to personality through architectural experience"
  },
  {
    id: 3,
    title: "The Production of Space",
    author: "Henri Lefebvre", 
    type: "book",
    field: "Critical Geography",
    position: { x: 3, y: -2, z: 1 },
    color: 0xFF9800,
    connections: [0, 4, 7],
    description: "Theorizes space as socially produced through spatial practices and representations",
    relevance: "Framework for understanding how built environments reflect and shape social relations"
  },
  {
    id: 4,
    title: "The Image of the City",
    author: "Kevin Lynch",
    type: "book",
    field: "Urban Planning",
    position: { x: -2, y: -2, z: -2 },
    color: 0x9C27B0,
    connections: [1, 3, 5, 6],
    description: "Studies how people perceive and navigate urban environments",
    relevance: "Bridge between spatial cognition and environmental psychology in cities"
  },
  {
    id: 5,
    title: "Environmental Psychology and Human Behavior",
    author: "Mehta, Bonnes & Lee",
    type: "book",
    field: "Environmental Psychology",
    position: { x: 1, y: -3, z: 2 },
    color: 0xF44336,
    connections: [0, 4, 7, 8],
    description: "Comprehensive overview of person-environment relationships",
    relevance: "Provides psychological foundation for built-environment-personality connections"
  },
  {
    id: 6,
    title: "Pattern Language",
    author: "Christopher Alexander",
    type: "book",
    field: "Architecture Theory",
    position: { x: -1, y: 2, z: -3 },
    color: 0x795548,
    connections: [2, 4, 8],
    description: "Identifies spatial patterns that support human well-being",
    relevance: "Links architectural design principles to psychological outcomes"
  },
  {
    id: 7,
    title: "Machine Learning for Urban Sensing and Environmental Psychology",
    author: "Current Research Frontier",
    type: "paper",
    field: "GeoAI",
    position: { x: 2, y: 1, z: 3 },
    color: 0x00BCD4,
    connections: [3, 5, 8],
    description: "Emerging field using AI to understand human-environment interactions",
    relevance: "Methodological approach for my built-environment-personality research"
  },
  {
    id: 8,
    title: "Big Five Personality and Urban Environment Preferences",
    author: "My Proposed Research",
    type: "research",
    field: "Environmental Psychology + GeoAI",
    position: { x: 0, y: -1, z: 3 },
    color: 0xE91E63,
    connections: [5, 6, 7],
    description: "Investigating how personality traits relate to built environment preferences",
    relevance: "Central research question emerging from this theoretical foundation",
    isGoal: true
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
  
  let detailsHTML = `<strong>Author:</strong> ${paperData.author || 'Unknown'}<br>`;
  detailsHTML += `<strong>Type:</strong> ${paperData.type}<br>`;
  detailsHTML += `<strong>Field:</strong> ${paperData.field}<br>`;
  
  if (paperData.description) {
    detailsHTML += `<br><strong>About:</strong> ${paperData.description}<br>`;
  }
  
  if (paperData.relevance) {
    detailsHTML += `<br><strong>Relevance:</strong> <em>${paperData.relevance}</em>`;
  }
  
  if (paperData.isCenter) {
    detailsHTML += `<br><br><span style="color: #D4AF37;">⭐ Foundational Work</span>`;
  }
  
  if (paperData.isGoal) {
    detailsHTML += `<br><br><span style="color: #E91E63;">🎯 Research Goal</span>`;
  }
  
  if (paperData.file) {
    detailsHTML += `<br><br><a href="${paperData.file}" target="_blank" style="color: #007cba;">📄 View file</a>`;
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
  // Add a loading message first
  const container = document.getElementById('knowledge-web');
  container.innerHTML = '<div style="display: flex; align-items: center; justify-content: center; height: 100%; color: #666; font-size: 16px;"><div>Loading 3D Knowledge Web... ⚡</div></div>';
  
  // Try to initialize after a short delay
  setTimeout(function() {
    try {
      if (typeof THREE !== 'undefined') {
        initKnowledgeWeb();
      } else {
        // Fallback to 2D visualization
        createFallbackVisualization();
      }
    } catch (error) {
      console.error('Error initializing knowledge web:', error);
      createFallbackVisualization();
    }
  }, 100);
});

function createFallbackVisualization() {
  const container = document.getElementById('knowledge-web');
  container.innerHTML = `
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);">
      <h3 style="color: #333; margin-bottom: 20px;">Space & Place Theory Journey</h3>
      <p style="color: #666; text-align: center; margin-bottom: 30px; max-width: 500px;">
        My intellectual roadmap from foundational spatial theory to contemporary research applications
      </p>
      <div style="position: relative; width: 500px; height: 350px;">
        <!-- Central foundational work -->
        <div style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); background: #D4AF37; color: white; padding: 12px; border-radius: 8px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); z-index: 10; max-width: 140px;">
          <strong>Topophilia</strong><br>
          <small>Yi-Fu Tuan</small><br>
          <em>⭐ Foundation</em>
        </div>
        
        <!-- Theoretical papers arranged around center -->
        <div style="position: absolute; left: 5%; top: 15%; background: #4CAF50; color: white; padding: 8px; border-radius: 5px; font-size: 10px; max-width: 110px; text-align: center;">
          <strong>Space and Place</strong><br>
          <small>Tuan</small>
        </div>
        
        <div style="position: absolute; right: 5%; top: 20%; background: #2196F3; color: white; padding: 8px; border-radius: 5px; font-size: 10px; max-width: 110px; text-align: center;">
          <strong>Poetics of Space</strong><br>
          <small>Bachelard</small>
        </div>
        
        <div style="position: absolute; left: 8%; top: 65%; background: #FF9800; color: white; padding: 8px; border-radius: 5px; font-size: 10px; max-width: 110px; text-align: center;">
          <strong>Production of Space</strong><br>
          <small>Lefebvre</small>
        </div>
        
        <div style="position: absolute; right: 8%; bottom: 15%; background: #9C27B0; color: white; padding: 8px; border-radius: 5px; font-size: 10px; max-width: 110px; text-align: center;">
          <strong>Image of the City</strong><br>
          <small>Lynch</small>
        </div>
        
        <div style="position: absolute; left: 25%; bottom: 5%; background: #F44336; color: white; padding: 8px; border-radius: 5px; font-size: 10px; max-width: 110px; text-align: center;">
          <strong>Environmental Psychology</strong><br>
          <small>Mehta et al.</small>
        </div>
        
        <div style="position: absolute; right: 25%; top: 8%; background: #795548; color: white; padding: 8px; border-radius: 5px; font-size: 10px; max-width: 110px; text-align: center;">
          <strong>Pattern Language</strong><br>
          <small>Alexander</small>
        </div>
        
        <div style="position: absolute; left: 75%; bottom: 35%; background: #00BCD4; color: white; padding: 8px; border-radius: 5px; font-size: 10px; max-width: 110px; text-align: center;">
          <strong>GeoAI Methods</strong><br>
          <small>Current Research</small>
        </div>
        
        <div style="position: absolute; left: 35%; bottom: 25%; background: #E91E63; color: white; padding: 8px; border-radius: 5px; font-size: 10px; max-width: 110px; text-align: center;">
          <strong>My Research Goal</strong><br>
          <small>🎯 Built-Env-Personality</small>
        </div>
        
        <!-- Connection lines -->
        <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;">
          <line x1="50%" y1="50%" x2="12%" y2="22%" stroke="#999" stroke-width="2" opacity="0.6"/>
          <line x1="50%" y1="50%" x2="88%" y2="28%" stroke="#999" stroke-width="2" opacity="0.6"/>
          <line x1="50%" y1="50%" x2="15%" y2="72%" stroke="#999" stroke-width="2" opacity="0.6"/>
          <line x1="50%" y1="50%" x2="85%" y2="78%" stroke="#999" stroke-width="2" opacity="0.6"/>
          <line x1="50%" y1="50%" x2="32%" y2="88%" stroke="#999" stroke-width="2" opacity="0.6"/>
          <line x1="50%" y1="50%" x2="68%" y2="15%" stroke="#999" stroke-width="2" opacity="0.6"/>
          <line x1="50%" y1="50%" x2="80%" y2="65%" stroke="#999" stroke-width="2" opacity="0.6"/>
          <line x1="50%" y1="50%" x2="42%" y2="75%" stroke="#999" stroke-width="2" opacity="0.6"/>
        </svg>
      </div>
      
      <p style="color: #666; margin-top: 20px; text-align: center; max-width: 450px; font-size: 14px;">
        <strong>Mini-Geo Journey 1:</strong> This network maps my engagement with space/place theories, 
        showing the intellectual progression from phenomenological foundations to contemporary GeoAI applications.
      </p>
      
      <div style="margin-top: 15px;">
        <button onclick="location.reload()" style="background: #007cba; color: white; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer;">
          🔄 Try 3D Interactive Version
        </button>
      </div>
    </div>
  `;
}
</script>

## Theoretical Framework Development

### From Phenomenology to Digital Methods

This knowledge web demonstrates my theoretical journey from classical phenomenological approaches to contemporary digital methodologies:

1. **Foundational Spatial Theory**: Starting with Tuan's *Topophilia* and phenomenological geography
2. **Critical Spatial Theory**: Incorporating Lefebvre's production of space and Lynch's urban imaging
3. **Environmental Psychology**: Bridging spatial theory with psychological frameworks
4. **Contemporary Applications**: Connecting theory to GeoAI and machine learning methods

### Research Evolution

**Phase 1: Theoretical Grounding**
- Establishing understanding of space vs. place distinctions
- Exploring phenomenological approaches to spatial experience
- Understanding critical perspectives on spatial production

**Phase 2: Psychological Integration**
- Connecting spatial theory to environmental psychology
- Investigating person-environment relationships
- Exploring design principles that support well-being

**Phase 3: Methodological Innovation** 
- Applying machine learning to spatial behavior patterns
- Using GeoAI for large-scale environmental psychology research
- Developing new approaches to built-environment-personality studies

### Assignment Reflection

This Mini-Geo Journey accomplishes several academic goals:

- **Theoretical Engagement**: Demonstrates deep reading in space/place literature
- **Intellectual Connections**: Shows how different theoretical traditions inform my research
- **Methodological Bridge**: Connects classical theory to contemporary digital methods
- **Research Roadmap**: Illustrates progression toward my built-environment-personality study

### Interactive Features

- **Drag and Rotate**: Explore the 3D knowledge space
- **Hover for Details**: Learn about each work and its relevance
- **Connection Mapping**: See how ideas flow between different authors and approaches
- **Theoretical Clustering**: Notice how different schools of thought group together

## Papers I Have Read

Below are the comprehensive bibliographies of papers I have read across three key areas of my research. These readings form the foundation of my theoretical understanding and inform my approach to built-environment-personality research.

### 📊 GeoAI & Spatial Intelligence

<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #007cba;">

**Brown, C. F., Kazmierski, M. R., Pasquarella, V. J., et al.** (2025). *AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data* (arXiv:2507.22291). arXiv. [https://doi.org/10.48550/arXiv.2507.22291](https://doi.org/10.48550/arXiv.2507.22291)

**Goodchild, M. F., & Janelle, D. G.** (2004). Thinking Spatially in the Social Sciences. In M. F. Goodchild & D. G. Janelle (Eds.), *Spatially Integrated Social Science* (p. 0). Oxford University Press. [https://doi.org/10.1093/oso/9780195152708.003.0001](https://doi.org/10.1093/oso/9780195152708.003.0001)

**Goodchild, M. F., & Li, W.** (2021). Replication across space and time must be weak in the social and environmental sciences. *Proceedings of the National Academy of Sciences*, *118*(35), e2015759118. [https://doi.org/10.1073/pnas.2015759118](https://doi.org/10.1073/pnas.2015759118)

**Hu, Y., Gao, S., Lunga, D., Li, W., Newsam, S., & Bhaduri, B.** (2019). GeoAI at ACM SIGSPATIAL: Progress, challenges, and future directions. *SIGSPATIAL Special*, *11*(2), 5–15. [https://doi.org/10.1145/3377000.3377002](https://doi.org/10.1145/3377000.3377002)

**Janowicz, K., Gao, S., McKenzie, G., Hu, Y., & Bhaduri, B.** (2020). GeoAI: Spatially explicit artificial intelligence techniques for geographic knowledge discovery and beyond. *International Journal of Geographical Information Science*, *34*(4), 625–636. [https://doi.org/10.1080/13658816.2019.1684500](https://doi.org/10.1080/13658816.2019.1684500)

**Jean, N., Wang, S., Samar, A., Azzari, G., Lobell, D., & Ermon, S.** (2019). Tile2Vec: Unsupervised Representation Learning for Spatially Distributed Data. *Proceedings of the AAAI Conference on Artificial Intelligence*, *33*(01), 3967–3974. [https://doi.org/10.1609/aaai.v33i01.33013967](https://doi.org/10.1609/aaai.v33i01.33013967)

</div>

### 🧠 Geography & Personality Research

<div style="background: #f1f8e9; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #4CAF50;">

**Biljecki, F., & Ito, K.** (2021). Street view imagery in urban analytics and GIS: A review. *Landscape and Urban Planning*, *215*, 104217. [https://doi.org/10.1016/j.landurbplan.2021.104217](https://doi.org/10.1016/j.landurbplan.2021.104217)

**Ebert, T., Gebauer, J. E., Brenner, T., Bleidorn, W., Gosling, S. D., Potter, J., & Rentfrow, P. J.** (2022). Are Regional Differences in Psychological Characteristics and Their Correlates Robust? Applying Spatial-Analysis Techniques to Examine Regional Variation in Personality. *Perspectives on Psychological Science*, *17*(2), 407–441. [https://doi.org/10.1177/1745691621998326](https://doi.org/10.1177/1745691621998326)

**Götz, F. M., Ebert, T., Gosling, S. D., Obschonka, M., Potter, J., & Rentfrow, P. J.** (2021). Local housing market dynamics predict rapid shifts in cultural openness: A 9-year study across 199 cities. *American Psychologist*, *76*(6), 947–961. [https://doi.org/10.1037/amp0000812](https://doi.org/10.1037/amp0000812)

**Götz, F. M., Gosling, S. D., & Rentfrow, P. J.** (2022). Small Effects: The Indispensable Foundation for a Cumulative Psychological Science. *Perspectives on Psychological Science*, *17*(1), 205–215. [https://doi.org/10.1177/1745691620984483](https://doi.org/10.1177/1745691620984483)

**Götz, F. M., Montello, D. R., Varnum, M. E. W., Luca, D., & Kenrick, D. T.** (2025). A unified framework integrating psychology and geography. *Nature Human Behaviour*, 1–13. [https://doi.org/10.1038/s41562-025-02237-y](https://doi.org/10.1038/s41562-025-02237-y)

**Ito, K., Kang, Y., Gosling, S. D., Potter, J., Yao, X., & Biljecki, F.** Uncovering the Associations between Human Big Five Personality Traits and Built Environment Characteristics from Street View Imagery. *[In Preparation]*

**Ito, K., Zhu, Y., Abdelrahman, M., et al.** (2025). ZenSVI: An open-source software for the integrated acquisition, processing and analysis of street view imagery towards scalable urban science. *Computers, Environment and Urban Systems*, *119*, 102283. [https://doi.org/10.1016/j.compenvurbsys.2025.102283](https://doi.org/10.1016/j.compenvurbsys.2025.102283)

**Jokela, M., Bleidorn, W., Lamb, M. E., Gosling, S. D., & Rentfrow, P. J.** (2015). Geographically varying associations between personality and life satisfaction in the London metropolitan area. *Proceedings of the National Academy of Sciences*, *112*(3), 725–730. [https://doi.org/10.1073/pnas.1415800112](https://doi.org/10.1073/pnas.1415800112)

**Militaru, I. E., Serapio-García, G., Ebert, T., et al.** (2024). The lay of the land: Associations between environmental features and personality. *Journal of Personality*, *92*(1), 88–110. [https://doi.org/10.1111/jopy.12822](https://doi.org/10.1111/jopy.12822)

**Rentfrow, P. J., Gosling, S. D., Jokela, M., Stillwell, D. J., Kosinski, M., & Potter, J.** (2013). Divided we stand: Three psychological regions of the United States and their political, economic, social, and health correlates. *Journal of Personality and Social Psychology*, *105*(6), 996–1012. [https://doi.org/10.1037/a0034434](https://doi.org/10.1037/a0034434)

**Rentfrow, P. J., Gosling, S. D., & Potter, J.** (2008). A Theory of the Emergence, Persistence, and Expression of Geographic Variation in Psychological Characteristics. *Perspectives on Psychological Science*, *3*(5), 339–369. [https://doi.org/10.1111/j.1745-6924.2008.00084.x](https://doi.org/10.1111/j.1745-6924.2008.00084.x)

**Wei, W., Lu, J. G., Galinsky, A. D., et al.** (2017). Regional ambient temperature is associated with human personality. *Nature Human Behaviour*, *1*(12), 890–895. [https://doi.org/10.1038/s41562-017-0240-0](https://doi.org/10.1038/s41562-017-0240-0)

</div>

### 🏛️ Critical Issues in Geography

<div style="background: #fff3e0; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #FF9800;">

**Cox, K.** (2021). Human and physical geography and the question of space. *Belgeo. Revue Belge de Géographie*, *4*. [https://doi.org/10.4000/belgeo.52790](https://doi.org/10.4000/belgeo.52790)

**Fluri, J. L.** (2021). Political geography 1: Extractions. *Progress in Human Geography*, *45*(4), 855–865. [https://doi.org/10.1177/0309132520970258](https://doi.org/10.1177/0309132520970258)

**Goodchild, M. F.** (2011). Scale in GIS: An overview. *Geomorphology*, *130*(1), 5–9. [https://doi.org/10.1016/j.geomorph.2010.10.004](https://doi.org/10.1016/j.geomorph.2010.10.004)

**Kobayashi, A.** (2014). The Dialectic of Race and the Discipline of Geography. *Annals of the Association of American Geographers*, *104*(6), 1101–1115. [https://doi.org/10.1080/00045608.2014.958388](https://doi.org/10.1080/00045608.2014.958388)

**Lin, Y., & Kim, J.** (2025). Pillars of GeoAI in Human Geography. In X. Huang, S. Wang, J. Wilson, & P. Kedron (Eds.), *GeoAI and Human Geography: The Dawn of a New Spatial Intelligence Era* (pp. 29–40). Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-87421-5_3](https://doi.org/10.1007/978-3-031-87421-5_3)

**Mansfield, B., Lave, R., McSweeney, K., et al.** (2019). It's time to recognize how men's careers benefit from sexually harassing women in academia. *Human Geography*, *12*(1), 82–87. [https://doi.org/10.1177/194277861901200110](https://doi.org/10.1177/194277861901200110)

</div>

### 📚 Reading Strategy & Research Impact

These comprehensive reading lists demonstrate my systematic approach to literature review across multiple domains:

- **🔬 Technical Foundation**: GeoAI papers provide methodological grounding for computational spatial analysis
- **🧩 Theoretical Integration**: Geography-personality research bridges spatial theory with psychological frameworks  
- **⚖️ Critical Perspective**: Issues in geography ensure awareness of disciplinary challenges and social justice concerns
- **🔗 Interdisciplinary Synthesis**: Combined readings inform my built-environment-personality research approach

*The papers listed above represent active engagement with current literature in my field, informing both my Mini-Geo Journey theoretical development and my ongoing research methodology.*

---

*This visualization serves as my first Mini-Geo Journey, demonstrating how theories of space and place inform my research trajectory in environmental psychology and GeoAI. The interactive format allows viewers to explore the connections between foundational readings and contemporary methodological approaches.*

**Assignment Context**: First of three Mini-Geo Journeys for graduate coursework, focusing on space/place theory engagement and research foundation building.