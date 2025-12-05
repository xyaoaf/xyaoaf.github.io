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
        'name': 'Hangzhou, Zhejiang',
        'lat': 30.222346,
        'lon': 120.030019,
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
        'lat': 22.336668,
        'lon': 114.263418,
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
        'name': 'Shanghai',
        'lat': 31.104848,
        'lon': 121.610225,
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
        'name': 'Beijing',
        'lat': 39.909395,
        'lon':  116.465402,
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
        'name': 'Seattle, Washington',
        'lat': 47.655442, 
        'lon': -122.307149,
        'story': '''
            Seattle holds a special place in my life because of two very different—but equally meaningful—chapters I experienced there.

            My first connection to Seattle was in 2019, when I spent a semester as an exchange student at the University of Washington. It was my first time studying at an American university, and I was immediately struck by the beauty of the UW campus, the diversity of the student community, and the vibrant atmosphere of the city itself. During that semester, I enrolled in courses I could not take back in Hong Kong—urban planning, geographic programming, and other classes that opened my eyes to new ways of thinking about geography, cities, and the environment. Outside of class, I made friends from around the world and traveled across Washington State, visiting national parks and soaking in the natural beauty of the Pacific Northwest. That exchange semester was a pivotal moment that broadened my academic horizons and reshaped my cultural perspective.

            My second Seattle chapter came several years later, when I took my first industrial job at EarthDefine, a small geospatial company based in Redmond, right next to Seattle. I worked there for over a year, applying my academic training to real-world geospatial challenges. EarthDefine specialized in producing high-resolution land cover datasets for city governments and national agencies. Using open-source deep learning models and NAIP imagery, we built detailed classifications of urban landscapes. My role involved generating tree canopy and land cover data that cities relied on to understand their communities, plan for the future, and monitor changes in vegetation and development over time.

            This experience was deeply meaningful because it was the first time I saw how my work directly informed real decisions in urban planning and environmental management. It taught me how technical spatial data could translate into tangible public benefits.

            Both of these Seattle experiences—one academic, one professional—played vital roles in shaping who I am today. Together, they expanded my worldview, deepened my skills, and marked key turning points in both my personal and career development.
        '''
    },
    {
        'name': 'Berkeley, California',
        'lat': 37.8703622,
        'lon': -122.2551394,
        'story': '''
            Berkeley, California, is unquestionably one of the most influential places in my life. From 2021 to 2023, I completed my Master's degree in Environmental Planning at UC Berkeley—an experience that reshaped not only my academic trajectory but also my understanding of myself. On the very first day of class, I realized I was the only Chinese or foreign student in my cohort. That moment carried far more weight than I expected; it made me acutely aware of how different cultural backgrounds and worldviews intersect in an academic environment like Berkeley.

            The diversity of perspectives on campus opened my eyes in ways I had never experienced before. But the beginning was not easy. Many of my peers came in with years of professional experience and already had a clear sense of their research goals. Meanwhile, I felt I had to explore widely—testing ideas, learning new methods, and searching for the direction that resonated with me. It was an uncertain period, but also an incredibly formative one.

            With the encouragement of my cohort and mentors, I gradually found my footing. I ended up developing an independent and innovative thesis that combined datasets and analytical approaches I had never used before. That project gave me confidence in my ability to carve out my own research path rather than simply following established ones.

            After graduating, I remained in Berkeley for another two years, and one of the most memorable chapters unfolded almost immediately. In the first semester after finishing my degree, I stepped into the role of lecturer for Berkeley's largest GIS class, C188, after my professor retired. I was only 24 at the time—just a few years older than many of the students I was teaching. I modernized the course, redesigned the slides and labs, and made an intentional effort to learn all 200 students' names.

            Standing in front of a lecture hall of so many students for the first time was both intimidating and exhilarating. It taught me how to teach, how to lead, and how to design a learning environment that could inspire curiosity. That experience fundamentally reshaped the way I viewed academia and revealed a side of myself I didn't know existed.

            Berkeley wasn't just where I earned my degree. It became a turning point—a place that challenged me, supported me, and ultimately helped me grow into who I am today.
        '''
    },
    {
        'name': 'Austin, Texas',
        'lat': 30.2844774,
        'lon': -97.737072,
        'story': '''
            Austin, Texas marks the newest chapter of my journey as I begin my PhD in Geography. It's a fresh start in a young, energetic city, and I feel fortunate to have joined a research group that fits me so well. I didn't choose my labmates, but working with them has been one of the best surprises—they're supportive, talented, and make the start of my PhD feel exciting rather than overwhelming.

            Academically, Austin offers perspectives and courses that are quite different from what I encountered at Berkeley, giving me new ways to think about my work. Even though I've only been here for about three months, I already feel the importance of protecting my time and focusing on what matters most as I settle into my PhD.

            Austin is still new to me, but it's full of possibility. I'm looking forward to the growth, challenges, and opportunities this chapter will bring.
        '''
            ,
            'photo': '../images/E4CBD7EF-8361-4088-997D-1094B15CB593_1_102_o.jpeg'
    },
    {
        'name': 'Minneapolis, Minnesota',
        'lat': 44.9737073,
        'lon': -93.272617,
        'story': '''
            I visited Minneapolis in October 2025 for the ACSP conference—my first time attending a planning conference. It brought together people from technology, science, and social science, all discussing planning from different angles. The experience gave me fresh insights and new connections, and I wrote a short post about my time there to look back on. It was brief, but it added another valuable perspective to my path.
        '''
    },
    {
        'name': 'Portland, Oregon',
        'lat': 45.545435,
        'lon': -122.651532,
        'story': '''
            Portland holds a special place in my heart as the city where I conducted my Master's thesis research on urban forest equity and microclimate disparities. I visited Portland several times during my research, and I was privileged to collaborate with the Bureau of Environmental Services at the City of Portland. They provided me with invaluable resources—especially the 2019 high-density LiDAR dataset—that made my thesis research possible.

            For my study, I selected two contrasting census blocks to compare: one historically affluent neighborhood and another located in the far suburbs on previously brownfield land, where residents tend to be more vulnerable. Using advanced remote sensing and spatial analysis, my research revealed not only significant differences in the quantity of urban trees between these communities but also major disparities in the composition and quality of their urban forests. These differences contributed to unequal access to ecosystem services—particularly cooling benefits that reduce heat exposure during summer months.

            The most meaningful part came after completing the research, when I finally visited both communities in person. Walking the streets and seeing the neighborhoods with my own eyes gave me a profound connection to the data I had analyzed. I even located and visited the two specific sample trees I had studied in detail for my thesis. Seeing those trees firsthand—understanding their physical characteristics, their role in their neighborhoods, and their impact on the people living around them—made the entire project feel real, grounded, and deeply meaningful. Portland transformed my understanding of what it means to do environmental justice research: it's not just about numbers and remote sensing, but about real communities and real people.
        '''
    },
    {
        'name': 'Pasadena, California',
        'lat': 34.1436727,
        'lon': -118.1451019,
        'story': '''
            Pasadena, California marks a pivotal milestone in my research career. In June 2023, I attended the IEEE IGARSS conference—the first major academic conference of my career and the first time I publicly presented my Master's thesis research on a large international stage.

            I delivered a full presentation on my project, "Object-Based Urban Trees Characterization with Airborne LiDAR for Microclimate Simulation," sharing my findings about urban forest equity and the disparities in tree canopy and ecosystem services between different neighborhoods in Portland. The experience of standing in front of hundreds of researchers from around the world, discussing my work, and receiving questions and feedback was both exhilarating and formative.

            Beyond the main presentation, I also distilled my thesis research into a sharp elevator pitch for the GeoPitch competition—a showcase of innovative work in geoscience. To my surprise and genuine excitement, I earned the Third Place Award in the IEEE Geoscience and Remote Sensing Society's GeoPitch competition for my innovative approach to sustainable geoscience.

            Pasadena marked many firsts for me: my first major international conference, my first thesis presentation, my first research award—an unforgettable milestone that pushed me forward in my research career and gave me confidence in my ability to contribute meaningfully to the geospatial science community.
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
