"""
Journey Locations Data
Separate file to store all your journey locations for easy editing

Edit this file to add/update locations, then run journey_map_folium.py to regenerate the map
"""

JOURNEY_LOCATIONS = [
    {
        'name': 'Yueqing, Zhejiang',
        'lat': 28.115304,
        'lon': 120.953046,
        'story': '''
            Yueqing is a coastal city in Zhejiang Province and one of the earliest places that shaped my understanding of human–environment relationships. Mountains, the sea, rapid industrial development, and recurring typhoons all formed part of its landscape.

            Memories of flooding and infrastructure disruption gave me an early awareness of both the benefits and risks associated with water. These experiences later contributed to my interest in environmental change, climate resilience, and the ways communities adapt to natural processes.
        '''
    },
    {
        'name': 'Hangzhou, Zhejiang',
        'lat': 30.222346,
        'lon': 120.030019,
        'story': '''
            I grew up in Hangzhou, where water is central to both the city's landscape and its cultural identity. West Lake, the Grand Canal, and the region's wetlands provided early examples of how environmental processes, infrastructure, and landscape design shape urban life.

            West Lake is recognized by UNESCO as a cultural landscape rather than a purely natural site. Its long history of management and design illustrates how landscapes emerge through sustained interaction between people and their environment.

            Growing up in this setting contributed to my interest in water, urban environmental change, and the relationship between natural systems and cultural landscapes.
        '''
    },
    {
        'name': 'Hong Kong',
        'lat': 22.336668,
        'lon': 114.263418,
        'story': '''
            From 2017 to 2021, I completed a BSc in Environmental Management and Technology at the Hong Kong University of Science and Technology. The interdisciplinary program brought together environmental science, engineering, technology, and the social sciences, providing an early foundation for my work across disciplinary boundaries.

            My undergraduate research examined neighborhood-scale light pollution through field measurements and spatial modeling. This work introduced me to the use of geospatial methods for studying urban environmental conditions and contributed to my first academic publication.

            Hong Kong's dense urban environment and coastal setting also provided an important context for thinking about how infrastructure, environmental processes, and human activity interact within a rapidly changing city.
        '''
    },
    {
        'name': 'Shanghai',
        'lat': 31.104848,
        'lon': 121.610225,
        'story': '''
            In 2020, I completed an Environment, Health, and Safety internship with an international manufacturing company in Shanghai. My work included compliance documentation, operational coordination, and support for workplace safety practices.

            The experience introduced me to the practical responsibilities of environmental and safety management in an industrial setting. It also strengthened my ability to work independently, communicate across organizational roles, and respond to changing project needs.
        '''
    },
    {
        'name': 'Beijing',
        'lat': 39.909395,
        'lon':  116.465402,
        'story': '''
            In summer 2020, I worked with the Beijing Smart and Green Transport Research Institute on transportation and sustainability research. I supported projects examining the electrification potential of commercial vehicle fleets through data collection, carbon modeling, scenario analysis, and policy research.

            This experience introduced me to the relationship between technical analysis and environmental policy. It also showed me the importance of communicating assumptions, evidence, and uncertainty when research is intended to inform decision-making.
        '''
    },
    {
        'name': 'Seattle, Washington',
        'lat': 47.655442, 
        'lon': -122.307149,
        'story': '''
            The Seattle region is connected to two stages of my academic and professional development. In 2019, I studied at the University of Washington as an exchange student. Courses in urban planning and geographic programming broadened my interest in cities, environmental systems, and computational geography.

            I later returned to the region to work as a GIS Analyst at EarthDefine in Redmond. I applied aerial imagery, deep-learning methods, and geospatial workflows to the production of high-resolution land-cover and tree-canopy datasets.

            Together, these experiences connected my academic training with the practical development of spatial data used in urban planning and environmental management.
        '''
    },
    {
        'name': 'Berkeley, California',
        'lat': 37.8703622,
        'lon': -122.2551394,
        'story': '''
            Berkeley was an important stage in my academic development. From 2021 to 2023, I completed a master's degree in Environmental Planning at the University of California, Berkeley. During the program, I developed my research interests in urban forests, remote sensing, and microclimate modeling.

            My thesis brought together LiDAR, spatial analysis, and environmental modeling to examine differences in urban vegetation and cooling benefits. The project helped establish the research direction that I continue to develop through my doctoral studies.

            After graduation, I served as the instructor of record for GEOG/LDARCH C188, an interdisciplinary GIS course enrolling more than 200 students. Designing the course, coordinating its instructional team, and supporting student projects strengthened my interests in teaching and geospatial education.

            Berkeley therefore shaped both my research trajectory and my approach to teaching.
        '''
    },
    {
        'name': 'Austin, Texas',
        'lat': 30.2844774,
        'lon': -97.737072,
        'story': '''
            Austin marks the beginning of my doctoral studies in Geography at The University of Texas at Austin. I joined the GISense Lab in 2025, where I study GeoAI, environmental processes, and human–environment interactions.

            Moving from Berkeley to Austin has introduced me to a different academic and geographic setting. The city's rapid growth and environmental change provide an important context for thinking about urban development, climate resilience, and the applications of geospatial research.
        '''
            ,
            'photo': '../images/E4CBD7EF-8361-4088-997D-1094B15CB593_1_102_o.jpeg'
    },
    {
        'name': 'Minneapolis, Minnesota',
        'lat': 44.9737073,
        'lon': -93.272617,
        'story': '''
            I visited Minneapolis in October 2025 for the Association of Collegiate Schools of Planning Annual Conference. I presented our published research on community-scale microclimate simulation and object-based urban tree classification in the session "Advanced Methods for Environmental Science."

            During the trip, I also visited a geospatial research group at the University of Minnesota. The conference and lab visit provided opportunities to discuss how remote sensing, GeoAI, and environmental modeling can contribute to planning research.

            <a href="/posts/2025/10/acsp-conference-minneapolis/">Read the conference note</a>.
        '''
    },
    {
        'name': 'Portland, Oregon',
        'lat': 45.545435,
        'lon': -122.651532,
        'story': '''
            Portland was the case-study location for my master's research on urban forests and neighborhood microclimates. In collaboration with the City of Portland Bureau of Environmental Services, I used high-density airborne LiDAR and other spatial data to examine urban tree structure and associated cooling benefits.

            The study compared two neighborhoods with different development and vegetation conditions. The analysis identified differences not only in tree-canopy quantity, but also in the composition and structure of their urban forests—factors that influence the distribution of ecosystem services.

            Visiting the study areas after completing much of the remote analysis helped connect the spatial data with their physical and community contexts. This experience strengthened my interest in combining remote sensing with questions of environmental equity and urban planning.
        '''
    },
    {
        'name': 'Pasadena, California',
        'lat': 34.1436727,
        'lon': -118.1451019,
        'story': '''
            In July 2023, I attended the IEEE International Geoscience and Remote Sensing Symposium (IGARSS) in Pasadena. I presented our conference paper, "From Local to Micro: Exploratory Data Analysis on Urban Forests and Microclimates in Portland, Oregon, USA," which examined relationships between urban vegetation and neighborhood microclimates.

            I also participated in the IEEE Geoscience and Remote Sensing Society GeoPitch competition with "Object-Based Urban Trees Characterization with Airborne LiDAR for Microclimate Simulation." The project received the Third Place Award.

            IGARSS was my first major international academic conference and an early opportunity to present my master's research to the remote-sensing community.
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
