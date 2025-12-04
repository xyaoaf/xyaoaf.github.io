"""
Interactive Journey Map - Connecting the Dots
A 3D globe visualization showing places that shaped your academic and personal journey

This script creates an interactive map where you can click on markers to see stories
about your connection to each place.

Requirements:
    pip install plotly pandas

Usage:
    1. Edit the LOCATIONS list below with your places and stories
    2. Run: python journey_map.py
    3. Open journey_map.html in a browser
    4. Upload journey_map.html to your website's /files/ folder
"""

import plotly.graph_objects as go
import pandas as pd

# ============================================================================
# EDIT THIS SECTION: Add your locations and stories
# ============================================================================

LOCATIONS = [
    {
        'name': 'Hong Kong',
        'lat': 22.3193,
        'lon': 114.1694,
        'story': '''
            <b>Hong Kong University of Science and Technology</b><br>
            BSc in Environmental Science<br><br>
            Where my journey began. This is where I first discovered my passion for 
            understanding human-environment interactions and the power of geospatial 
            analysis to address environmental challenges.
        '''
    },
    {
        'name': 'Berkeley, California',
        'lat': 37.8715,
        'lon': -122.2730,
        'story': '''
            <b>University of California, Berkeley</b><br>
            Master of Landscape Architecture (MLA)<br><br>
            At UC Berkeley, I deepened my understanding of urban forests, microclimate 
            modeling, and how environmental planning can create more equitable and 
            sustainable cities. Working with Prof. Iryna Dronova opened new doors 
            to remote sensing and GeoAI research.
        '''
    },
    {
        'name': 'Austin, Texas',
        'lat': 30.2849,
        'lon': -97.7341,
        'story': '''
            <b>The University of Texas at Austin</b><br>
            PhD in Geography<br><br>
            Currently pursuing my PhD in the GISense Lab with Prof. Yuhao Kang. 
            Here, I'm developing data-driven GeoAI approaches to understand environmental 
            processes, urban sustainability, and climate resilience. Austin has become 
            my home for exploring the frontiers of geospatial science.
        '''
    },
    {
        'name': 'Minneapolis, Minnesota',
        'lat': 44.9778,
        'lon': -93.2650,
        'story': '''
            <b>ACSP 2025 Conference</b><br>
            October 2025<br><br>
            My first ACSP conference! Presented my research on urban forests and 
            microclimate modeling, visited Prof. Yao-Yi Chiang's lab at University 
            of Minnesota, and connected with the planning community. The Mill City 
            Museum and Minneapolis Institute of Art were highlights of the visit.
        '''
    },
    # ADD MORE LOCATIONS HERE:
    # {
    #     'name': 'Your City',
    #     'lat': 0.0,  # latitude
    #     'lon': 0.0,  # longitude
    #     'story': '''
    #         <b>Title or Institution</b><br>
    #         Dates<br><br>
    #         Your story about this place and what it means to you...
    #     '''
    # },
]

# ============================================================================
# VISUALIZATION CODE (No need to edit below unless customizing appearance)
# ============================================================================

def create_journey_map(locations):
    """
    Creates an interactive 3D globe with markers for each location.
    
    Args:
        locations: List of dictionaries with 'name', 'lat', 'lon', 'story'
    
    Returns:
        plotly Figure object
    """
    # Create DataFrame
    df = pd.DataFrame(locations)
    
    # Create the 3D globe trace
    fig = go.Figure()
    
    # Add markers for each location
    fig.add_trace(go.Scattergeo(
        lon=df['lon'],
        lat=df['lat'],
        text=df['story'],
        mode='markers+text',
        name='',
        marker=dict(
            size=12,
            color='rgb(255, 127, 80)',  # Coral color
            line=dict(width=2, color='white'),
            symbol='circle'
        ),
        textposition='top center',
        textfont=dict(size=10, color='white'),
        hovertemplate='<b>%{hovertext}</b><br><br>%{text}<extra></extra>',
        hovertext=df['name']
    ))
    
    # Add connecting lines between consecutive locations (optional)
    for i in range(len(df) - 1):
        fig.add_trace(go.Scattergeo(
            lon=[df.iloc[i]['lon'], df.iloc[i+1]['lon']],
            lat=[df.iloc[i]['lat'], df.iloc[i+1]['lat']],
            mode='lines',
            line=dict(width=1, color='rgba(255, 127, 80, 0.3)'),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Update layout for 3D globe appearance
    fig.update_geos(
        projection_type='orthographic',
        showcountries=True,
        countrycolor='rgb(204, 204, 204)',
        showcoastlines=True,
        coastlinecolor='rgb(204, 204, 204)',
        showland=True,
        landcolor='rgb(243, 243, 243)',
        showocean=True,
        oceancolor='rgb(230, 245, 255)',
        showlakes=True,
        lakecolor='rgb(230, 245, 255)',
        showrivers=True,
        rivercolor='rgb(230, 245, 255)',
        bgcolor='rgb(255, 255, 255)'
    )
    
    fig.update_layout(
        title={
            'text': 'My Geospatial Journey: Connecting the Dots',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20}
        },
        height=600,
        margin={'l': 0, 'r': 0, 't': 50, 'b': 0},
        showlegend=False,
        geo=dict(
            projection_rotation=dict(
                lon=-97,  # Center on Austin
                lat=30,
                roll=0
            )
        )
    )
    
    return fig


def save_map(fig, filename='journey_map.html'):
    """
    Saves the map as an HTML file.
    
    Args:
        fig: plotly Figure object
        filename: Output HTML filename
    """
    fig.write_html(filename, include_plotlyjs='cdn')
    print(f"✓ Map saved as {filename}")
    print(f"✓ Open {filename} in your browser to view")
    print(f"✓ Upload to your website's /files/ folder")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("Creating your journey map...")
    
    # Create the map
    fig = create_journey_map(LOCATIONS)
    
    # Save as HTML
    save_map(fig)
    
    print("\nNext steps:")
    print("1. Open journey_map.html in your browser to preview")
    print("2. Edit LOCATIONS in this script to add more places")
    print("3. Upload journey_map.html to xyaoaf.github.io/files/")
    print("4. Your blog post will automatically display the map!")
