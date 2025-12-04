# Interactive Journey Map - Setup Guide

This guide will help you create and customize your interactive journey map.

## Quick Start

### 1. Install Requirements

```bash
pip install plotly pandas
```

### 2. Edit Your Locations

Open `journey_map.py` and edit the `LOCATIONS` list:

```python
LOCATIONS = [
    {
        'name': 'Your City Name',
        'lat': 0.0,      # latitude (get from Google Maps)
        'lon': 0.0,      # longitude (get from Google Maps)
        'story': '''
            <b>Title</b><br>
            Subtitle or dates<br><br>
            Your story about this place...
        '''
    },
    # Add more locations...
]
```

### 3. Generate the Map

```bash
cd /path/to/your/website/files
python journey_map.py
```

This creates `journey_map.html`

### 4. Preview Locally

Open `journey_map.html` in your browser to preview

### 5. Deploy to Website

The file is already in the `/files/` folder, so just commit and push:

```bash
git add files/journey_map.html
git commit -m "Add interactive journey map"
git push origin master
```

## How to Get Coordinates

### Method 1: Google Maps
1. Go to https://www.google.com/maps
2. Right-click on your location
3. Click the coordinates (e.g., "30.2849, -97.7341")
4. Copy latitude (first number) and longitude (second number)

### Method 2: Python Geocoding
```python
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="journey_map")
location = geolocator.geocode("Austin, Texas")
print(f"lat: {location.latitude}, lon: {location.longitude}")
```

## Customization Options

### Change Colors
Edit the `marker` dictionary in `create_journey_map()`:

```python
marker=dict(
    size=12,
    color='rgb(255, 127, 80)',  # Change this RGB value
    line=dict(width=2, color='white'),
)
```

### Change Starting View
Edit the `projection_rotation` in `update_layout()`:

```python
projection_rotation=dict(
    lon=-97,  # longitude to center on
    lat=30,   # latitude to center on
    roll=0
)
```

### Add More Information
You can use HTML in the `story` field:

```python
'story': '''
    <b>Bold Title</b><br>
    <i>Italic subtitle</i><br><br>
    Regular text...<br>
    <a href="https://example.com">Link</a>
'''
```

## Troubleshooting

**Map doesn't show up on website:**
- Check that `journey_map.html` is in the `/files/` folder
- Verify the iframe path in your blog post is `/files/journey_map.html`
- Clear your browser cache

**Markers not appearing:**
- Verify latitude and longitude are correct
- Latitude should be between -90 and 90
- Longitude should be between -180 and 180

**Stories not displaying on hover:**
- Check for unclosed HTML tags in your story text
- Make sure quotes are properly escaped

## Advanced: Alternative Visualization Libraries

If you want different styles, you can also use:

### Folium (2D interactive maps)
```python
import folium

m = folium.Map(location=[30.2849, -97.7341], zoom_start=2)
folium.Marker([30.2849, -97.7341], 
              popup='Austin, TX',
              tooltip='Click for story').add_to(m)
m.save('journey_map.html')
```

### Kepler.gl (Advanced geospatial visualization)
More complex but very powerful for larger datasets

## Questions?

Feel free to customize the code! The main function to edit is `create_journey_map()` where you can adjust:
- Marker sizes and colors
- Globe projection and rotation
- Connecting lines between locations
- Hover information display
- Overall layout and styling

Happy mapping! 🗺️
