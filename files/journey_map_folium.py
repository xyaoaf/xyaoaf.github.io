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

# ============================================================================
# EDIT THIS SECTION: Add your locations and stories
# ============================================================================

LOCATIONS = [
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
    # ADD MORE LOCATIONS HERE:
    # {
    #     'name': 'Your City',
    #     'lat': 0.0,
    #     'lon': 0.0,
    #     'institution': 'Institution Name',
    #     'degree': 'Degree or Event',
    #     'years': 'Years',
    #     'story': 'Your detailed story about this place...'
    # },
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
        <div style="width: 200px; font-family: Arial, sans-serif;">
            <h4 style="margin: 0 0 8px 0; color: #333;">{loc['name']}</h4>
            <p style="margin: 4px 0; font-size: 12px; color: #666;">
                <b>{loc['institution']}</b><br>
                {loc['years']}
            </p>
            <p style="margin: 8px 0 0 0; font-size: 11px; color: #999;">
                Click marker for full details →
            </p>
        </div>
        """
        
        # Create the marker with click event
        marker = folium.Marker(
            location=[loc['lat'], loc['lon']],
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=loc['name'],
            icon=folium.Icon(color='red', icon='info-sign')
        )
        
        # Add JavaScript to update sidebar on click
        marker_js = f"""
        <script>
        var locationData_{i} = {{
            name: "{loc['name']}",
            institution: "{loc['institution']}",
            degree: "{loc['degree']}",
            years: "{loc['years']}",
            story: `{loc['story']}`
        }};
        </script>
        """
        
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
    # Save the base map
    map_obj.save(filename)
    
    # Read the generated HTML
    with open(filename, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Create location data as JSON for JavaScript
    locations_json = json.dumps(locations)
    
    # Enhanced HTML with sidebar
    enhanced_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Geospatial Journey: Connecting the Dots</title>
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
            {html_content.split('<body>')[1].split('</body>')[0]}
        </div>
        <div id="sidebar">
            <div class="placeholder">
                <p>👈 Click on a marker to explore stories from each location</p>
            </div>
        </div>
        
        <script>
            // Location data
            const locations = {locations_json};
            
            // Function to update sidebar
            function updateSidebar(locationData) {{
                const sidebar = document.getElementById('sidebar');
                sidebar.innerHTML = `
                    <div class="marker-icon">📍</div>
                    <h2>${{locationData.name}}</h2>
                    <h3>${{locationData.institution}}</h3>
                    <div class="years">${{locationData.years}}</div>
                    <p><strong>${{locationData.degree}}</strong></p>
                    <div class="story">${{locationData.story}}</div>
                `;
            }}
            
            // Add click listeners to all markers
            setTimeout(function() {{
                const markers = document.querySelectorAll('.leaflet-marker-icon');
                markers.forEach((marker, index) => {{
                    marker.addEventListener('click', function() {{
                        if (locations[index]) {{
                            updateSidebar(locations[index]);
                        }}
                    }});
                }});
            }}, 1000);
        </script>
    </body>
    </html>
    """
    
    # Write enhanced HTML
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(enhanced_html)
    
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
