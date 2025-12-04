"""
Interactive Journey Map - Connecting the Dots (Folium Version)
A 2D interactive map with clickable markers that display stories in a sidebar panel

This script creates an interactive map where clicking markers updates a sidebar
with detailed information about each location.

Requirements:
    pip install folium pandas

Usage:
    1. Edit the LOCATIONS list below with your places and stories
    2. Run: python journey_map_folium.py
    3. Open journey_map.html in a browser
    4. Upload journey_map.html to your website's /files/ folder
"""

import folium
from folium import IFrame
import pandas as pd
import json

# Import locations from separate data file
try:
    from journey_locations import JOURNEY_LOCATIONS as LOCATIONS
except ImportError:
    # Fallback if journey_locations.py doesn't exist
    print("Warning: journey_locations.py not found, using embedded data")
    LOCATIONS = [
    {
        'name': 'Yueqing',
        'lat': 28.1167,
        'lon': 120.9667,
        'institution': 'Birthplace',
        'degree': 'Early Childhood',
        'years': '1998 - 2004',
        'story': '''
            I was born in 1998 in Yueqing, a coastal town tucked under the jurisdiction of Wenzhou in eastern China. 
            Ringed by mountains on one side and the sea on the other, it's a place shaped by fishing traditions, 
            early industrial growth, and the rhythms of the ocean. I spent my earliest years there—only until about 
            the age of five—but it wasn't until much later that I understood how distinctive my hometown really was.
            Yueqing was transforming rapidly back then, with countless privately owned lighting factories sprouting 
            up across the town. At the same time, it was constantly tested by nature. Typhoons were a regular part 
            of life, and I still remember waking up to find a foot of water covering the ground outside. My dad would 
            simply roll up his pants, start his motorcycle, and ride through the flooded streets to pick up groceries, 
            unfazed by the stormy chaos around him. Even though I left early, these memories have stayed with me. 
            Yueqing remains a place of deep personal significance—my first home, and the backdrop of the experiences 
            that quietly shaped my sense of resilience, curiosity, and connection to the environments I later chose to study.
        '''
    },
    {
        'name': 'Hangzhou',
        'lat': 30.2741,
        'lon': 120.1551,
        'institution': 'Childhood Home',
        'years': '2004 - 2017',
        'story': '''
            The second meaningful place in my life is Hangzhou, the capital of Zhejiang Province and one of China’s largest and most storied cities. I spent nearly all my childhood and teenage years there—from primary school through high school—before heading off to university. Hangzhou is a city with a long memory, having once served as the capital of a major part of China, and its landscapes carry layers of history, culture, and human ingenuity.

Growing up, the West Lake was a constant presence. As a UNESCO World Cultural Heritage site, it represents thousands of years of deliberate efforts to harmonize the built environment with nature. Bridges, pavilions, and pagodas crafted by generations have shaped the lake into a celebrated landscape—no longer purely natural, but unquestionably iconic. Walking or biking along its shores gave me an early sense of how deeply nature can shape urban life and identity.

To the west of the city, the expansive wetland that was preserved and transformed into a national wetland park served as another reminder: Hangzhou was once a vast swamp before the city rose around it. And the Grand Canal—stretching all the way from Beijing to Hangzhou—was a living testament to the role of water not just as a resource, but as a cultural artery that carried people, goods, and ideas across hundreds of years.

All of these elements shaped my understanding of the close relationship between humans and water, and of how natural systems quietly but powerfully influence the rhythm of urban life. Hangzhou wasn’t just the city where I grew up—it was a formative landscape that nurtured my early appreciation for the interplay between nature, history, and everyday living.
        '''
    },
    {
        'name': 'Hong Kong',
        'lat': 22.3193,
        'lon': 114.1694,
        'institution': 'Hong Kong University of Science and Technology',
        'degree': 'BSc in Environmental Science',
        'years': '2015 - 2019',
        'story': '''
            Where my journey began. This is where I first discovered my passion for 
            understanding human-environment interactions and the power of geospatial 
            analysis to address environmental challenges. The vibrant city and coastal 
            ecosystems provided a rich context for learning about urban environmental issues.
        '''
    },
    {
        'name': 'Berkeley, California',
        'lat': 37.8715,
        'lon': -122.2730,
        'institution': 'University of California, Berkeley',
        'degree': 'Master of Landscape Architecture (MLA)',
        'years': '2021 - 2023',
        'story': '''
            At UC Berkeley, I deepened my understanding of urban forests, microclimate 
            modeling, and how environmental planning can create more equitable and 
            sustainable cities. Working with Prof. Iryna Dronova opened new doors 
            to remote sensing and GeoAI research. The Bay Area's diverse landscapes 
            and progressive environmental policies provided endless research opportunities.
        '''
    },
    {
        'name': 'Austin, Texas',
        'lat': 30.2849,
        'lon': -97.7341,
        'institution': 'The University of Texas at Austin',
        'degree': 'PhD in Geography',
        'years': '2023 - Present',
        'story': '''
            Currently pursuing my PhD in the GISense Lab with Prof. Yuhao Kang. 
            Here, I'm developing data-driven GeoAI approaches to understand environmental 
            processes, urban sustainability, and climate resilience. Austin has become 
            my home for exploring the frontiers of geospatial science. The city's rapid 
            growth and environmental challenges provide a living laboratory for my research.
        '''
    },
    {
        'name': 'Minneapolis, Minnesota',
        'lat': 44.9778,
        'lon': -93.2650,
        'institution': 'ACSP 2025 Conference',
        'degree': 'Conference Presentation',
        'years': 'October 2025',
        'story': '''
            My first ACSP conference! Presented my research on urban forests and 
            microclimate modeling in the "Advanced Methods for Environmental Science" session. 
            Visited Prof. Yao-Yi Chiang's lab at University of Minnesota and connected 
            with the planning community. The Mill City Museum and Minneapolis Institute 
            of Art were highlights of the visit. The city's commitment to green infrastructure 
            was inspiring.
        '''
    },
    ]

# ============================================================================
# VISUALIZATION CODE
# ============================================================================

def create_journey_map_folium(locations):
    """
    Creates an interactive Folium map with markers and sidebar panel.
    
    Args:
        locations: List of dictionaries with location data
    
    Returns:
        folium Map object
    """
    # Create base map centered on US
    m = folium.Map(
        location=[37.0, -95.0],
        zoom_start=4,
        tiles='CartoDB positron',
        width='100%',
        height='100%'
    )
    
    # Add markers for each location
    for i, loc in enumerate(locations):
        # Create popup content (brief version)
        popup_html = f"""
        <div style="width: 180px; font-family: Arial, sans-serif;">
            <h4 style="margin: 0 0 8px 0; color: #333;">{loc['name']}</h4>
            <p style="margin: 8px 0 0 0; font-size: 11px; color: #999;">
                Click marker for the full story →
            </p>
        </div>
        """
        
        # Create the marker with click event
        marker = folium.Marker(
            location=[loc['lat'], loc['lon']],
            popup=folium.Popup(popup_html, max_width=200),
            tooltip=loc['name'],
            icon=folium.Icon(color='red', icon='info-sign')
        )
        
        marker.add_to(m)
    
    return m


def save_map_with_sidebar(map_obj, locations, filename='journey_map.html'):
    """
    Saves the map with an integrated sidebar panel.
    
    Args:
        map_obj: Folium map object
        locations: List of location dictionaries
        filename: Output HTML filename
    """
    # Save the base map to a temporary file
    temp_file = 'temp_map.html'
    map_obj.save(temp_file)
    
    # Read the generated HTML
    with open(temp_file, 'r', encoding='utf-8') as f:
        map_html = f.read()
    
    # Extract just the head content and body content from Folium
    head_start = map_html.find('<head>')
    head_end = map_html.find('</head>') + 7
    head_content = map_html[head_start:head_end]
    
    body_start = map_html.find('<body>')
    body_end = map_html.find('</body>')
    body_content = map_html[body_start+6:body_end]
    
    # Create location data as JSON for JavaScript
    locations_json = json.dumps(locations)
    
    # Enhanced HTML with sidebar
    enhanced_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Geospatial Journey: Connecting the Dots</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            display: flex;
            height: 100vh;
            overflow: hidden;
        }}
        #map-container {{
            flex: 1;
            position: relative;
        }}
        #map {{
            width: 100%;
            height: 100%;
        }}
        #sidebar {{
            width: 400px;
            background: white;
            border-left: 1px solid #ddd;
            overflow-y: auto;
            padding: 24px;
            box-shadow: -2px 0 8px rgba(0,0,0,0.1);
        }}
        #sidebar h2 {{
            margin: 0 0 8px 0;
            color: #333;
            font-size: 24px;
        }}
        #sidebar h3 {{
            margin: 16px 0 8px 0;
            color: #666;
            font-size: 16px;
            font-weight: normal;
        }}
        #sidebar .years {{
            color: #999;
            font-size: 14px;
            margin-bottom: 16px;
        }}
        #sidebar .story {{
            color: #555;
            line-height: 1.7;
            font-size: 14px;
            margin-top: 16px;
            padding-top: 16px;
            border-top: 1px solid #eee;
        }}
        #sidebar .placeholder {{
            color: #999;
            font-style: italic;
            text-align: center;
            margin-top: 100px;
        }}
        .marker-icon {{
            color: #dc3545;
            font-size: 18px;
            margin-bottom: 8px;
        }}
        @media (max-width: 768px) {{
            body {{
                flex-direction: column;
            }}
            #sidebar {{
                width: 100%;
                height: 40vh;
                border-left: none;
                border-top: 1px solid #ddd;
            }}
            #map-container {{
                height: 60vh;
            }}
        }}
    </style>
</head>
<body>
    <div id="map-container">
        <div id="map"></div>
    </div>
    <div id="sidebar">
        <div class="placeholder">
            <p>👈 Click on a marker to explore stories from each location</p>
        </div>
    </div>
    
    <script>
        // Location data
        const locations = {locations_json};
        
        // Create the map centered on the globe
        var map = L.map('map').setView([20.0, 0.0], 2);
        
        // Add satellite tile layer
        L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
            attribution: '© Esri, Maxar, Earthstar Geographics',
            maxZoom: 19
        }}).addTo(map);
        
        // Add markers
        locations.forEach((loc, index) => {{
            var marker = L.marker([loc.lat, loc.lon], {{
                icon: L.icon({{
                    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
                    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png',
                    iconSize: [25, 41],
                    iconAnchor: [12, 41],
                    popupAnchor: [1, -34],
                    shadowSize: [41, 41]
                }})
            }}).addTo(map);
            
            // Add popup
            marker.bindPopup(`
                <div style="width: 180px; font-family: Arial, sans-serif;">
                    <h4 style="margin: 0 0 8px 0; color: #333;">${{loc.name}}</h4>
                    <p style="margin: 8px 0 0 0; font-size: 11px; color: #999;">
                        Click marker for the full story →
                    </p>
                </div>
            `);
            
            // Add click event to update sidebar
            marker.on('click', function() {{
                updateSidebar(loc);
            }});
        }});
        
        // Function to update sidebar
        function updateSidebar(locationData) {{
            const sidebar = document.getElementById('sidebar');
            sidebar.innerHTML = `
                <div class="marker-icon">📍</div>
                <h2>${{locationData.name}}</h2>
                <div class="story">${{locationData.story}}</div>
            `;
        }}
    </script>
</body>
</html>"""
    
    # Write enhanced HTML
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(enhanced_html)
    
    # Clean up temp file
    import os
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    print(f"✓ Map with sidebar saved as {filename}")
    print(f"✓ Open {filename} in your browser to view")
    print(f"✓ Upload to your website's /files/ folder")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("Creating your interactive journey map with Folium...")
    
    # Create the map
    journey_map = create_journey_map_folium(LOCATIONS)
    
    # Save with integrated sidebar
    save_map_with_sidebar(journey_map, LOCATIONS)
    
    print("\nFeatures:")
    print("- Click markers to see full details in sidebar")
    print("- Hover over markers for quick preview")
    print("- Responsive design works on mobile too")
    print("\nNext steps:")
    print("1. Open journey_map.html in your browser")
    print("2. Click on markers to test the sidebar")
    print("3. Add more locations to LOCATIONS list as needed")
    print("4. Upload to xyaoaf.github.io/files/")
