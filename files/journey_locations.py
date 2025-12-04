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
        'name': 'Hangzhou, China',
        'lat': 30.2741,
        'lon': 120.1551,
        'story': '''
            The second meaningful place in my life is Hangzhou, the capital of Zhejiang Province and one of China's largest 
            and most storied cities. I spent nearly all my childhood and teenage years there—from primary school through 
            high school—before heading off to university. Hangzhou is a city with a long memory, having once served as the 
            capital of a major part of China, and its landscapes carry layers of history, culture, and human ingenuity.
            
            Growing up, the West Lake was a constant presence. As a UNESCO World Cultural Heritage site, it represents thousands 
            of years of deliberate efforts to harmonize the built environment with nature. Bridges, pavilions, and pagodas 
            crafted by generations have shaped the lake into a celebrated landscape—no longer purely natural, but unquestionably 
            iconic. Walking or biking along its shores gave me an early sense of how deeply nature can shape urban life and identity.
            
            To the west of the city, the expansive wetland that was preserved and transformed into a national wetland park served 
            as another reminder: Hangzhou was once a vast swamp before the city rose around it. And the Grand Canal—stretching all 
            the way from Beijing to Hangzhou—was a living testament to the role of water not just as a resource, but as a cultural 
            artery that carried people, goods, and ideas across hundreds of years.
            
            All of these elements shaped my understanding of the close relationship between humans and water, and of how natural 
            systems quietly but powerfully influence the rhythm of urban life. Hangzhou wasn't just the city where I grew up—it 
            was a formative landscape that nurtured my early appreciation for the interplay between nature, history, and everyday living.
        '''
    },
    {
        'name': 'Hong Kong',
        'lat': 22.3193,
        'lon': 114.1694,
        'story': '''
            The third meaningful place in my journey is Hong Kong, where I completed my undergraduate studies from 2017 to 2021. 
            Ending up there was, in many ways, a twist of fate—after the competitive and unpredictable experience of the Chinese 
            college entrance exam, life led me to the Hong Kong University of Science and Technology, a young and ambitious 
            institution that was barely 25 years old at the time, almost as young as I was.
            
            At HKUST, I majored in Environmental Management and Technology, an interdisciplinary program that sat at the intersection 
            of science, engineering, technology, and the social sciences. It was the first time I truly experienced how environmental 
            issues span across disciplines and require integrated thinking, not just technical knowledge. That program became my 
            gateway into understanding environmental systems through a broader and more holistic lens.
            
            Hong Kong itself was equally influential. As a dynamic international metropolis with deep Chinese cultural roots, the 
            city expanded my worldview in ways I could not have anticipated. I participated in social events, engaged with people 
            from diverse backgrounds, and became much more aware of global environmental conversations—both the urgency of the 
            challenges and the possibilities for innovation. I also began to understand what it meant to grow as a young professional 
            in a rapidly evolving field.
            
            Those four years in Hong Kong shaped not only my academic foundation but also my outlook on the world. They pushed me 
            to think beyond boundaries, prepared me for the complexities of my future studies, and set the stage for the next 
            chapters of my life.
        '''
    },
    {
        'name': 'Shanghai, China',
        'lat': 31.2304,
        'lon': 121.4737,
        'story': '''
            Shanghai played a unique—though relatively brief—role in my life in 2020. I never lived there long-term, but the city, 
            just about 200 kilometers from my home in Hangzhou, has always stood out as China's largest and most dynamic metropolis. 
            At that time, I wasn't pursuing any degree nor formally associated with any institution; I was simply an intern looking 
            for experience and direction during an uncertain year.
            
            My time in Shanghai unfolded during the early months of the pandemic, when lockdowns suddenly disrupted my original plan 
            to take a gap semester and intern abroad. With those plans derailed, I had to adjust quickly and look for opportunities 
            closer to home.
            
            That's how I found an internship at an international company in Shanghai that was expanding its operations and building 
            a new factory. The company produced disease testing kits—though not for COVID—and I joined their Environment, Health, 
            and Safety (EHS) department. The team was small, and about a month and a half into my internship, my supervisor 
            unexpectedly left the company. Overnight, I became the only person responsible for EHS across the China branch.
            
            It was an eye-opening experience to suddenly shoulder that level of responsibility with no formal authority and no degree 
            backing me—just my willingness to take ownership and figure things out. Managing compliance tasks, preparing documentation, 
            and ensuring on-site safety protocols all fell to me. In the process, I discovered that I could keep everything running 
            smoothly even under pressure and uncertainty.
            
            Though my time in Shanghai was short, it was deeply impactful. That 2020 internship became a formative chapter that 
            challenged me, strengthened my confidence, and added an unexpected but powerful layer to my professional growth.
        '''
    },
    {
        'name': 'Beijing, China',
        'lat': 39.9042,
        'lon': 116.4074,
        'story': '''
            Beijing became another meaningful stop in my journey during the summer of 2020, right after my internship in Shanghai. 
            I spent about three months there, working at the Beijing Smart and Green Transport Research Institute—a small but 
            influential think tank focused on transportation and sustainability. Unlike a large, formal institution, it was a 
            close-knit group where everyone took on multiple roles, and that made the experience both intimate and intellectually engaging.
            
            My work there revolved around data searching, data compilation, and policy analysis. For the first time, I had the chance 
            to work on projects that could directly influence national-level policies in China. One of the major projects I contributed 
            to was assessing the electrification potential of commercial vehicle fleets. Although electric passenger vehicles were 
            already a major topic at the time, applying electrification to cargo transportation was still new and somewhat speculative. 
            I remember being skeptical at first—could heavy-duty fleets really adopt electric technology at scale?
            
            Through carbon modeling, scenario analysis, and writing sections of policy reports, I started to see the possibilities 
            more clearly. It was my first exposure to work that resembled consulting, even if it took place within a smaller, 
            mission-driven organization rather than a major firm. I learned how technical insights, policy thinking, and communication 
            had to come together to inform decision-making.
            
            Looking back, that summer in Beijing brought my gap semester to a meaningful close. It pushed me to think more critically 
            about environmental strategies at the national scale and helped me mature professionally. By the time I returned to school 
            for my final undergraduate year, I felt far more prepared, grounded, and motivated for whatever came next.
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
