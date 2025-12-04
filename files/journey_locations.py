"""
Journey Locations Data
Separate file to store all your journey locations for easy editing

Edit this file to add/update locations, then run journey_map_folium.py to regenerate the map
"""

JOURNEY_LOCATIONS = [
    {
        'name': 'Yueqing, China',
        'lat': 28.1167,
        'lon': 120.9667,
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
        'name': 'Hong Kong',
        'lat': 22.3193,
        'lon': 114.1694,
        'story': '''
            Where my academic journey began. This is where I first discovered my passion for 
            understanding human-environment interactions and the power of geospatial 
            analysis to address environmental challenges. The vibrant city and coastal 
            ecosystems provided a rich context for learning about urban environmental issues.
        '''
    },
    {
        'name': 'Berkeley, California',
        'lat': 37.8715,
        'lon': -122.2730,
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
        'story': '''
            My first ACSP conference! Presented my research on urban forests and 
            microclimate modeling in the "Advanced Methods for Environmental Science" session. 
            Visited Prof. Yao-Yi Chiang's lab at University of Minnesota and connected 
            with the planning community. The Mill City Museum and Minneapolis Institute 
            of Art were highlights of the visit. The city's commitment to green infrastructure 
            was inspiring.
        '''
    },
    
    # ADD MORE LOCATIONS BELOW THIS LINE:
    # Just add the place name, coordinates, and your story:
    # {
    #     'name': 'City, Country/State',
    #     'lat': 0.0,  # Get from Google Maps: right-click location → coordinates
    #     'lon': 0.0,
    #     'story': '''
    #         Your story about this place...
    #     '''
    # },
]
