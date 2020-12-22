import csv

'''
This function extracts a list of categories for a business record:

Input: 1) list containing all sub categories for the specific business category

Output: a list of the categories that the business belongs to
'''
def attribute(input_Str):
    
    items = []
    
    for elem in input_Str:
        
        
        if (elem == 'Active Life' or elem == 'ATV Rentals/Tours' or elem == 'Airsoft' or elem == 'Amateur Sports Teams' or elem == 'Amusement Parks'
            or elem == 'Aquariums' or elem == 'Archery' or elem == 'Axe Throwing' or elem == 'Badminton' or elem == 'Baseball Fields'
            or elem == 'Basketball Courts' or elem == 'Batting Cages' or elem == 'Beach Equipment Rentals' or  elem == 'Beaches'
            or elem == 'Bike Parking' or elem == 'Bike Rentals' or elem == 'Boating' or elem == 'Bobsledding' or elem == 'Bocce Ball'
            or elem == 'Bowling' or elem == 'Bubble Soccer' or elem == 'Bungee Jumping' or elem == 'Canyoneering'
            or elem == 'Carousels' or elem == 'Challenge Courses' or elem == 'Climbing' or elem == 'Cycling Classes'
            or elem == 'Dart Arenas' or elem == 'Day Camps' or elem == 'Disc Golf' or elem == 'Diving' or elem == 'Free Diving'
            or elem == 'Scuba Diving' or elem == 'Escape Games' or elem == 'Fencing Clubs' or elem == 'Fishing'
            or elem == 'Fitness & Instruction' or elem == 'Aerial Fitness' or elem == 'Barre Classes' or elem == 'Boot Camps'
            or elem == 'Boxing' or elem == 'Cardio Classes' or elem == 'Dance Studios' or elem == 'Golf Lessons'
            or elem == 'Gyms' or elem == 'Circuit Training Gyms' or elem == 'Interval Training Gyms' or elem == 'Martial Arts'
            or elem == 'Brazilian Jiu-jitsu' or elem == 'Chinese Martial Arts' or elem == 'Karate' or elem == 'Kickboxing'
            or elem == 'Muay Thai' or elem == 'Taekwondo' or elem == 'Meditation Centers' or elem == 'Pilates' or elem == 'Qi Gong'
            or elem == 'Self-defense Classes' or elem == 'Swimming Lessons/Schools' or elem ==  'Tai Chi' or elem == 'Trainers'
            or elem == 'Yoga' or elem == 'Flyboarding' or elem == 'Go Karts'or elem == 'Golf' or elem ==  'Gun/Rifle Ranges'
            or elem == 'Gymnastics' or elem == 'Hang Gliding' or elem == 'Hiking' or elem == 'Horse Racing'
            or elem == 'Horseback Riding' or elem == 'Hot Air Balloons' or elem == 'Indoor Playcentre' or elem == 'Jet Skis'
            or elem == 'Kids Activities' or elem == 'Kiteboarding' or elem == 'Lakes' or elem == 'Laser Tag'
            or elem == 'Mini Golf' or elem == 'Mountain Biking' or elem == 'Nudist' or elem == 'Paddleboarding'
            or elem == 'Paintball' or elem == 'Paragliding' or elem == 'Parasailing' or elem == 'Parks' or elem == 'Dog Parks'
            or elem == 'Skate Parks' or elem == 'Pickleball' or elem == 'Playgrounds' or elem == 'Races & Competitions'
            or elem == 'Racing Experience' or elem == 'Rafting/Kayaking' or elem == 'Recreation Centers' or elem == 'Rock Climbing'
            or elem == 'Sailing' or elem == 'Scavenger Hunts' or elem == 'Scooter Rentals' or elem == 'Senior Centers'
            or elem == 'Skating Rinks' or elem == 'Skydiving' or elem == 'Sledding' or elem == 'Snorkeling' or elem == 'Soccer'
            or elem == 'Sports Clubs' or elem == 'Squash' or elem == 'Summer Camps' or elem == 'Surfing' or elem == 'Swimming Pools'
            or elem == 'Tennis' or elem == 'Trampoline Parks' or elem == 'Tubing' or elem == 'Water Parks' or elem == 'Wildlife Hunting Ranges'
            or elem == 'Ziplining' or elem == 'Zoos' or elem == 'Petting Zoos' or elem == 'Zorbing'):
            if 'Active Life' not in items:
                items.append('Active Life')
        
        elif (elem == 'Arts & Entertainment' or elem == 'Arcades' or elem == 'Art Galleries' or elem == 'Bingo Halls' or elem == 'Botanical Gardens'
              or elem == 'Cabaret' or elem == 'Casinos' or elem == 'Cinema' or elem == 'Drive-In Theater' or elem == 'Outdoor Movies'
              or elem == 'Country Clubs' or elem == 'Cultural Center' or elem == 'Entertainment' or elem == 'Farms'
              or elem == 'Attraction Farms' or elem == 'Pick Your Own Farms' or elem == 'Ranches' or elem == 'Festivals'
              or elem == 'Haunted Houses' or elem == 'Jazz & Blues' or elem == 'LAN Centers' or elem == 'Makerspaces'
              or elem == 'Museums' or elem == 'Art Museums' or elem == 'Children’s Museums' or elem == 'Music Venues'
              or elem == 'Observatories' or elem == 'Opera & Ballet' or elem == 'Paint & Sip' or elem == 'Performing Arts'
              or elem == 'Planetarium' or elem == 'Professional Sports Teams' or elem == 'Race Tracks' or elem == 'Rodeo'
              or elem == 'Social Clubs' or elem == 'Veterans Organizations' or elem == 'Sports Betting' or elem == 'Stadiums & Arenas'
              or elem == 'Studio Taping' or elem == 'Supernatural Readings' or elem == 'Astrologers' or elem == 'Mystics'
              or elem == 'Psychic Mediums' or elem == 'Psychics' or elem == 'Ticket Sales' or elem == 'Virtual Reality Centers'
              or elem == 'Wineries' or elem == 'Wine Tasting Room'):
              if 'Arts & Entertainment' not in items:
                    items.append('Arts & Entertainment')
        
        elif(elem == 'Automotive' or elem == 'Aircraft Dealers' or elem == 'Aircraft Repairs' or elem == 'Auto Customization' or elem == 'Auto Detailing'
             or elem == 'Auto Glass Services' or elem == 'Car Window Tinting' or elem == 'Auto Loan Providers'
             or elem == 'Auto Parts & Supplies' or elem == 'Motorcycle Parts & Supplies' or elem == 'Auto Repair'
             or elem == 'DIY Auto Shop' or elem == 'Auto Security' or elem == 'Auto Upholstery' or elem == 'Aviation Services'
             or elem == 'Boat Dealers' or elem == 'Boat Parts & Supplies' or elem == 'Body Shops' or elem == 'Car Auctions'
             or elem == 'Car Brokers' or elem == 'Car Buyers' or elem == 'Car Dealers' or elem == 'Car Inspectors'
             or elem == 'Car Share Services' or elem == 'Car Stereo Installation' or elem == 'Car Wash'
             or elem == 'Commercial Truck Dealers' or elem == 'Commercial Truck Repair' or elem == 'EV Charging Stations'
             or elem == 'Fuel Docks' or elem == 'Gas Stations' or elem == 'Golf Cart Dealers' or elem == 'Hybrid Car Repair'
             or elem == 'Interlock Systems' or elem == 'Marinas (marinas)' or elem == 'Mobile Dent Repair'
             or elem == 'Mobility Equipment Sales & Services' or elem == 'Motorcycle Dealers' or elem == 'Motorcycle Repair'
             or elem == 'Motorsport Vehicle Dealers' or elem == 'Motorsport Vehicle Repairs' or elem == 'Oil Change Stations'
             or elem == 'Parking' or elem == 'RV Dealers' or elem == 'RV Repair' or elem == 'Registration Services'
             or elem == 'Roadside Assistance' or elem == 'Service Stations' or elem == 'Smog Check Stations'
             or elem == 'Tires' or elem == 'Towing' or elem == 'Trailer Dealers' or elem == 'Trailer Rental'
             or elem == 'Trailer Repair' or elem == 'Transmission Repair' or elem == 'Truck Rental' or elem == 'Used Car Dealers'
             or elem == 'Vehicle Shipping' or elem == 'Vehicle Wraps' or elem == 'Wheel & Rim Repair'
             or elem == 'Windshield Installation & Repair'):
             if 'Automotive' not in items:
                    items.append('Automotive')
        
        elif(elem == 'Beauty & Spas' or elem == 'Acne Treatment' or elem == 'Barbers' or elem == 'Cosmetics & Beauty Supply' or elem == 'Day Spas'
             or elem == 'Eyebrow Services' or elem == 'Eyelash Service' or elem == 'Hair Extensions' 
             or elem == 'Hair Loss Centers' or elem == 'Hair Removal' or elem == 'Laser Hair Removal' or elem == 'Sugaring'
             or elem == 'Threading Services' or elem == 'Waxing' or elem == 'Hair Salons' or elem == 'Blow Dry/Out Services'
             or elem == 'Hair Extensions' or elem == 'Hair Stylists' or elem == 'Kids Hair Salons' or elem == 'Men’s Hair Salons'
             or elem == 'Hot Springs' or elem == 'Makeup Artists' or elem == 'Massage' or elem == 'Medical Spas'
             or elem == 'Aestheticians' or elem == 'Nail Salons' or elem == 'Nail Technicians' or elem == 'Perfume'
             or elem == 'Permanent Makeup' or elem == 'Piercing' or elem == 'Skin Care' or elem == 'Estheticians'
             or elem == 'Tanning' or elem == 'Spray Tanning' or elem == 'Tanning Beds' or elem == 'Tattoo'
             or elem == 'Teeth Whitening'):
             if 'Beauty & Spas' not in items:
                    items.append('Beauty & Spas')
        
        elif(elem == 'Education' or elem == 'Adult Education' or elem == 'Art Classes' or elem == 'Glass Blowing' or elem == 'College Counseling'
             or elem == 'Colleges & Universities' or elem == 'Educational Services' or elem == 'Elementary Schools'
             or elem == 'Middle Schools & High Schools' or elem == 'Montessori Schools' or elem == 'Preschools'
             or elem == 'Private Schools' or elem == 'Private Tutors' or elem == 'Religious Schools'
             or elem == 'Special Education' or elem == 'Specialty Schools' or elem == 'Art Schools' or elem == 'Bartending Schools'
             or elem == 'CPR Classes' or elem == 'Cheerleading' or elem == 'Childbirth Education' or elem == 'Cooking Schools'
             or elem == 'Cosmetology Schools' or elem == 'DUI Schools' or elem == 'Dance Schools' or elem == 'Drama Schools'
             or elem == 'Driving Schools' or elem == 'Firearm Training' or elem == 'First Aid Classes'
             or elem == 'Flight Instruction' or elem == 'Food Safety Training' or elem == 'Language Schools'
             or elem == 'Massage Schools' or elem == 'Nursing Schools' or elem == 'Parenting Classes'
             or elem == 'Photography Classes' or elem == 'Pole Dancing Classes' or elem == 'Ski Schools'
             or elem == 'Speech Training' or elem == 'Surf Schools' or elem == 'Swimming Lessons/Schools'
             or elem == 'Traffic Schools' or elem == 'Vocational & Technical School' or elem == 'Tasting Classes'
             or elem == 'Cheese Tasting Classes' or elem == 'Wine Tasting Classes' or elem == 'Test Preparation'
             or elem == 'Tutoring Centers' or elem == 'Waldorf Schools'):
             if 'Education' not in items:
                    items.append('Education')
        
        elif(elem == 'Event Planning & Services' or elem == 'Balloon Services' or elem == 'Bartenders' or elem == 'Boat Charters' or elem == 'Cards & Stationery'
             or elem == 'Caricatures' or elem == 'Caterers' or elem == 'Clowns' or elem == 'DJs' or elem == 'Face Painting'
             or elem == 'Floral Designers' or elem == 'Game Truck Rental' or elem == 'Golf Cart Rentals'
             or elem == 'Henna Artists' or elem == 'Hotels' or elem == 'Mountain Huts' or elem == 'Residences'
             or elem == 'Rest Stops' or elem == 'Magicians' or elem == 'Mohels' or elem == 'Musicians'
             or elem == 'Officiants' or elem == 'Party & Event Planning' or elem == 'Party Bike Rentals'
             or elem == 'Party Bus Rentals' or elem == 'Party Characters' or elem == 'Party Equipment Rentals'
             or elem == 'Audio/Visual Equipment Rental' or elem == 'Bounce House Rentals' or elem == 'Karaoke Rentals'
             or elem == 'Party Supplies' or elem == 'Personal Chefs' or elem == 'Photo Booth Rentals'
             or elem == 'Photographers (photographers)' or elem == 'Boudoir Photography' or elem == 'Event Photography'
             or elem == 'Session Photography' or elem == 'Silent Disco' or elem == 'Sommelier Services'
             or elem == 'Team Building Activities' or elem == 'Trivia Hosts' or elem == 'Valet Services'
             or elem == 'Venues & Event Spaces' or elem == 'Videographers' or elem == 'Wedding Chapels' 
             or elem == 'Wedding Planning'):
             if 'Event Planning & Services' not in items:
                    items.append('Event Planning & Services')
        
        elif(elem == 'Financial Services' or elem == 'Banks & Credit Unions' or elem == 'Business Financing' or elem == 'Check Cashing/Pay-day Loans'
             or elem == 'Currency Exchange' or elem == 'Debt Relief Services' or elem == 'Financial Advising'
             or elem == 'Installment Loans' or elem == 'Insurance' or elem == 'Auto Insurance'
             or elem == 'Home & Rental Insurance' or elem == 'Life Insurance' or elem == 'Investing' or elem == 'Mortgage Lenders'
             or elem == 'Tax Services' or elem == 'Title Loans'):
             if 'Financial Services' not in items:
                    items.append('Financial Services')
        
        elif(elem == 'Food' or elem == 'Acai Bowls' or elem == 'Bagels' or elem == 'Bakeries' or elem == 'Beer, Wine & Spirits'
             or elem == 'Beverage Store' or elem == 'Breweries' or elem == 'Brewpubs' or elem == 'Bubble Tea' or elem == 'Butcher'
             or elem == 'CSA' or elem == 'Chimney Cakes' or elem == 'Cideries' or elem == 'Coffee & Tea' or elem == 'Coffee Roasteries'
             or elem == 'Convenience Stores' or elem == 'Cupcakes' or elem == 'Custom Cakes' or elem == 'Desserts'
             or elem == 'Distilleries' or elem == 'Do-It-Yourself Food' or elem == 'Donuts' or elem == 'Empanadas'
             or elem == 'Farmers Market' or elem == 'Food Delivery Services' or elem == 'Food Trucks' or elem == 'Gelato'
             or elem == 'Grocery' or elem == 'Honey' or elem == 'Ice Cream & Frozen Yogurt' or elem == 'Imported Food'
             or elem == 'International Grocery' or elem == 'Internet Cafes' or elem == 'Juice Bars & Smoothies'
             or elem == 'Kombucha' or elem == 'Meaderies' or elem == 'Organic Stores' or elem == 'Patisserie/Cake Shop'
             or elem == 'Piadina' or elem == 'Poke' or elem == 'Pretzels' or elem == 'Shaved Ice' or elem == 'Shaved Snow'
             or elem == 'Smokehouse' or elem == 'Specialty Food' or elem == 'Candy Stores' or elem == 'Cheese Shops'
             or elem == 'Chocolatiers & Shops' or elem == 'Fruits & Veggies' or elem == 'Health Markets'
             or elem == 'Herbs & Spices' or elem == 'Macarons' or elem == 'Meat Shops' or elem == 'Olive Oil'
             or elem == 'Pasta Shops' or elem == 'Popcorn Shops' or elem == 'Seafood Markets' or elem == 'Street Vendors'
             or elem == 'Tea Rooms' or elem == 'Water Stores' or elem == 'Wineries' or elem == 'Wine Tasting Room'):
             if 'Food' not in items:
                    items.append('Food')
        
        elif(elem == 'Health & Medical' or elem == 'Acupuncture' or elem == 'Alternative Medicine' or elem == 'Animal Assisted Therapy'
             or elem == 'Assisted Living Facilities' or elem == 'Ayurveda' or elem == 'Behavior Analysts'
             or elem == 'Blood & Plasma Donation Centers' or elem == 'Body Contouring' or elem == 'Cannabis Clinics'
             or elem == 'Cannabis Tours' or elem == 'Cannabis Collective' or elem == 'Chiropractors' or elem == 'Colonics'
             or elem == 'Concierge Medicine' or elem == 'Counseling & Mental Health' or elem == 'Psychologists'
             or elem == 'Sex Therapists' or elem == 'Sports Psychologists' or elem == 'Crisis Pregnancy Centers'
             or elem == 'Faith-based Crisis Pregnancy Centers' or elem == 'Cryotherapy' or elem == 'Dental Hygienists'
             or elem == 'Dentists' or elem == 'Cosmetic Dentists' or elem == 'Endodontists' or elem == 'General Dentistry'
             or elem == 'Oral Surgeons' or elem == 'Orthodontists' or elem == 'Pediatric Dentists' or elem == 'Periodontists'
             or elem == 'Diagnostic Services' or elem == 'Diagnostic Imaging' or elem == 'Laboratory Testing' 
             or elem == 'Dialysis Clinics' or elem == 'Dietitians' or elem == 'Doctors' or elem == 'Addiction Medicine' 
             or elem == 'Allergists' or elem == 'Anesthesiologists' or elem == 'Audiologist' or elem == 'Cardiologists' 
             or elem == 'Cosmetic Surgeons' or elem == 'Dermatologists' or elem == 'Ear Nose & Throat' 
             or elem == 'Emergency Medicine' or elem == 'Endocrinologists' or elem == 'Family Practice' or elem == 'Fertility' 
             or elem == 'Gastroenterologist' or elem == 'Geneticists' or elem == 'Gerontologists' or elem == 'Hepatologists' 
             or elem == 'Hospitalists' or elem == 'Immunodermatologists' or elem == 'Infectious Disease Specialists' 
             or elem == 'Internal Medicine' or elem == 'Naturopathic/Holistic' or elem == 'Nephrologists' 
             or elem == 'Neurologist' or elem == 'Neuropathologists' or elem == 'Neurotologists' or elem == 'Obstetricians & Gynecologists' 
             or elem == 'Oncologist' or elem == 'Ophthalmologists' or elem == 'Retina Specialists' or elem == 'Orthopedists'
             or elem == 'Osteopathic Physicians' or elem == 'Otologists' or elem == 'Pain Management' 
             or elem == 'Pathologists' or elem == 'Pediatricians' or elem == 'Phlebologists' or elem == 'Plastic Surgeons'
             or elem == 'Podiatrists' or elem == 'Preventive Medicine' or elem == 'Proctologists' 
             or elem == 'Psychiatrists' or elem == 'Pulmonologist' or elem == 'Radiologists' or elem == 'Rheumatologists'
             or elem == 'Spine Surgeons' or elem == 'Sports Medicine' or elem == 'Surgeons' or elem == 'Tattoo Removal'
             or elem == 'Toxicologists' or elem == 'Undersea/Hyperbaric Medicine' or elem == 'Urologists' 
             or elem == 'Vascular Medicine' or elem == 'Doulas' or elem == 'Emergency Rooms' or elem == 'Float Spa' 
             or elem == 'Habilitative Services' or elem == 'Halfway Houses' or elem == 'Halotherapy' or elem == 'Health Coach'
             or elem == 'Health Insurance Offices' or elem == 'Hearing Aid Providers' or elem == 'Herbal Shops'
             or elem == 'Home Health Care' or elem == 'Hospice' or elem == 'Hospitals' or elem == 'Hydrotherapy' 
             or elem == 'Hypnosis/Hypnotherapy' or elem == 'IV Hydration' or elem == 'Lactation Services' 
             or elem == 'Laser Eye Surgery/Lasik' or elem == 'Lice Services' or elem == 'Massage Therapy' 
             or elem == 'Medical Cannabis Referrals' or elem == 'Medical Centers' or elem == 'Walk-in Clinics' 
             or elem == 'Medical Spas' or elem == 'Aestheticians' or elem == 'Medical Transportation' 
             or elem == 'Memory Care' or elem == 'Midwives' or elem == 'Nurse Practitioner' or elem == 'Nutritionists' 
             or elem == 'Occupational Therapy' or elem == 'Optometrists' or elem == 'Organ & Tissue Donor Services' 
             or elem == 'Orthotics' or elem == 'Oxygen Bars' or elem == 'Personal Care Services' 
             or elem == 'Pharmacy' or elem == 'Physical Therapy' or elem == 'Placenta Encapsulations'
             or elem == 'Prenatal/Perinatal Care' or elem == 'Prosthetics' or elem == 'Prosthodontists' 
             or elem == 'Reflexology' or elem == 'Rehabilitation Center' or elem == 'Reiki' 
             or elem == 'Reproductive Health Services' or elem == 'Retirement Homes' or elem == 'Saunas' 
             or elem == 'Skilled Nursing' or elem == 'Sleep Specialists' or elem == 'Speech Therapists' 
             or elem == 'Sperm Clinic' or elem == 'Traditional Chinese Medicine' or elem == 'Tui Na' 
             or elem == 'Ultrasound Imaging Centers' or elem == 'Urgent Care' or elem == 'Weight Loss Centers'):
             if 'Health & Medical' not in items:
                    items.append('Health & Medical')
        
        elif(elem == 'Home Services' or elem == 'Artificial Turf' or elem == 'Building Supplies' or elem == 'Cabinetry' or elem == 'Carpenters' 
             or elem == 'Carpet Installation' or elem == 'Carpeting' or elem == 'Childproofing' 
             or elem == 'Chimney Sweeps' or elem == 'Contractors' or elem == 'Countertop Installation' 
             or elem == 'Damage Restoration' or elem == 'Decks & Railing' or elem == 'Demolition Services' 
             or elem == 'Door Sales/Installation' or elem == 'Drywall Installation & Repair' or elem == 'Electricians' 
             or elem == 'Excavation Services' or elem == 'Fences & Gates' or elem == 'Fire Protection Services' 
             or elem == 'Fireplace Services' or elem == 'Firewood' or elem == 'Flooring' or elem == 'Foundation Repair' 
             or elem == 'Furniture Assembly' or elem == 'Garage Door Services' or elem == 'Gardeners' 
             or elem == 'Glass & Mirrors' or elem == 'Grout Services' or elem == 'Gutter Services' or elem == 'Handyman'
             or elem == 'Heating & Air Conditioning/HVAC' or elem == 'Holiday Decorating Services' 
             or elem == 'Home Automation' or elem == 'Home Cleaning' or elem == 'Home Energy Auditors' 
             or elem == 'Home Inspectors' or elem == 'Home Network Installation' or elem == 'Home Organization' 
             or elem == 'Home Theatre Installation' or elem == 'Home Window Tinting' or elem == 'House Sitters' 
             or elem == 'Insulation Installation' or elem == 'Interior Design' or elem == 'Internet Service Providers' 
             or elem == 'Irrigation' or elem == 'Keys & Locksmiths' or elem == 'Landscape Architects' 
             or elem == 'Landscaping' or elem == 'Lawn Services' or elem == 'Lighting Fixtures & Equipment' 
             or elem == 'Masonry/Concrete' or elem == 'Mobile Home Repair' or elem == 'Movers' or elem == 'Packing Services'
             or elem == 'Painters' or elem == 'Patio Coverings' or elem == 'Plumbing' or elem == 'Backflow Services' 
             or elem == 'Pool & Hot Tub Service' or elem == 'Pool Cleaners' or elem == 'Pressure Washers' 
             or elem == 'Real Estate' or elem == 'Apartments' or elem == 'Art Space Rentals' or elem == 'Commercial Real Estate'
             or elem == 'Condominiums' or elem == 'Estate Liquidation' or elem == 'Home Developers' 
             or elem == 'Home Staging' or elem == 'Homeowner Association' or elem == 'Housing Cooperatives' 
             or elem == 'Kitchen Incubators' or elem == 'Mobile Home Dealers' or elem == 'Mobile Home Parks' 
             or elem == 'Mortgage Brokers' or elem == 'Property Management' or elem == 'Real Estate Agents' 
             or elem == 'Apartment Agents' or elem == 'Real Estate Services' or elem == 'Land Surveying' 
             or elem == 'Real Estate Photography' or elem == 'Shared Office Spaces' or elem == 'University Housing' 
             or elem == 'Refinishing Services' or elem == 'Roof Inspectors' or elem == 'Roofing' 
             or elem == 'Sauna Installation & Repair' or elem == 'Security Systems' or elem == 'Shades & Blinds'
             or elem == 'Shutters' or elem == 'Siding' or elem == 'Solar Installation' or elem == 'Solar Panel Cleaning'
             or elem == 'Structural Engineers' or elem == 'Stucco Services' or elem == 'Television Service Providers' 
             or elem == 'Tiling' or elem == 'Tree Services' or elem == 'Utilities' or elem == 'Electricity Suppliers'
             or elem == 'Natural Gas Suppliers' or elem == 'Water Suppliers' or elem == 'Wallpapering' 
             or elem == 'Water Heater Installation/Repair' or elem == 'Water Purification Services' 
             or elem == 'Waterproofing' or elem == 'Window Washing' or elem == 'Windows Installation'):
             if 'Home Services' not in items:
                    items.append('Home Services')
                    
        elif(elem == 'Hotels & Travel' or elem =='Airports' or elem == 'Airport Terminals' or elem == 'Bed & Breakfast' or elem == 'Campgrounds'
             or elem == 'Car Rental' or elem == 'Guest Houses' or elem == 'Health Retreats' or elem == 'Hostels'
             or elem == 'Hotels' or elem == 'Mountain Huts' or elem == 'Residences' or elem == 'Rest Stops' 
             or elem == 'Motorcycle Rental' or elem == 'RV Parks' or elem == 'RV Rental' or elem == 'Resorts' 
             or elem == 'Ski Resorts' or elem == 'Tours' or elem == 'Aerial Tours' or elem == 'Architectural Tours' 
             or elem == 'Art Tours' or elem == 'Beer Tours' or elem == 'Bike tours' or elem == 'Boat Tours' 
             or elem == 'Bus Tours' or elem == 'Food Tours' or elem == 'Historical Tours' or elem == 'Scooter Tours' 
             or elem == 'Walking Tours' or elem == 'Whale Watching Tours' or elem == 'Wine Tours' 
             or elem == 'Train Stations' or elem == 'Transportation' or elem == 'Airlines' or elem == 'Airport Shuttles'
             or elem == 'Bike Sharing' or elem == 'Bus Stations' or elem == 'Buses' or elem == 'Cable Cars' 
             or elem == 'Ferries' or elem == 'Limos' or elem == 'Metro Stations' or elem == 'Pedicabs' 
             or elem == 'Private Jet Charter' or elem == 'Public Transportation' or elem == 'Taxis' 
             or elem == 'Town Car Service' or elem == 'Trains' or elem == 'Travel Services' or elem == 'Luggage Storage'
             or elem == 'Passport & Visa Services' or elem == 'Travel Agents' or elem == 'Visitor Centers' 
             or elem == 'Vacation Rental Agents' or elem == 'Vacation Rentals'):
             if 'Hotels & Travel' not in items:
                    items.append('Hotels & Travel')
        
        elif(elem == 'Local Flavor' or elem == 'Parklets' or elem == 'Public Art' or elem == 'Unofficial Yelp Events' or elem == 'Yelp Events'):
             if 'Local Flavor' not in items:
                    items.append('Local Flavor')
        
        elif(elem == 'Local Services' or elem == '3D Printing' or elem == 'Adoption Services' or elem == 'Air Duct Cleaning' or elem == 'Appliances & Repair'
             or elem == 'Appraisal Services' or elem == 'Art Installation' or elem == 'Art Restoration' 
             or elem == 'Awnings' or elem == 'Bail Bondsmen' or elem == 'Bike Repair/Maintenance' 
             or elem == 'Biohazard Cleanup' or elem == 'Bookbinding' or elem == 'Bus Rental' or elem == 'Calligraphy'
             or elem == 'Carpet Cleaning' or elem == 'Carpet Dyeing' or elem == 'Child Care & Day Care' 
             or elem == 'Clock Repair' or elem == 'Community Book Box' or elem == 'Community Gardens' 
             or elem == 'Community Service/Non-Profit' or elem == 'Food Banks' or elem == 'Homeless Shelters' 
             or elem == 'Couriers & Delivery Services' or elem == 'Crane Services' or elem == 'Donation Center' 
             or elem == 'Elder Care Planning' or elem == 'Electronics Repair' or elem == 'Elevator Services' 
             or elem == 'Engraving' or elem == 'Environmental Abatement' or elem == 'Environmental Testing' 
             or elem == 'Farm Equipment Repair' or elem == 'Fingerprinting' or elem == 'Funeral Services & Cemeteries'
             or elem == 'Cremation Services' or elem == 'Mortuary Services' or elem == 'Furniture Rental' 
             or elem == 'Furniture Repair' or elem == 'Furniture Reupholstery' or elem == 'Generator Installation/Repair'
             or elem == 'Grill Services' or elem == 'Gunsmith' or elem == 'Hazardous Waste Disposal' 
             or elem == 'Hydro-jetting' or elem == 'IT Services & Computer Repair' or elem == 'Data Recovery' 
             or elem == 'Mobile Phone Repair' or elem == 'Telecommunications' or elem == 'Ice Delivery' 
             or elem == 'Jewelry Repair' or elem == 'Junk Removal & Hauling' or elem == 'Dumpster Rental' 
             or elem == 'Junkyards' or elem == 'Knife Sharpening' or elem == 'Laundry Services' or elem == 'Dry Cleaning'
             or elem == 'Laundromat' or elem == 'Machine & Tool Rental' or elem == 'Machine Shops' 
             or elem == 'Mailbox Centers' or elem == 'Metal Detector Services' or elem == 'Metal Fabricators' 
             or elem == 'Misting System Services' or elem == 'Musical Instrument Services' or elem == 'Guitar Stores' 
             or elem == 'Piano Services' or elem == 'Piano Stores' or elem == 'Vocal Coach' or elem == 'Nanny Services'
             or elem == 'Notaries' or elem == 'Outdoor Power Equipment Services' or elem == 'Pest Control' 
             or elem == 'Portable Toilet Services' or elem == 'Powder Coating' or elem == 'Printing Services' 
             or elem == 'Propane' or elem == 'Recording & Rehearsal Studios' or elem == 'Recycling Center' 
             or elem == 'Sandblasting' or elem == 'Screen Printing' or elem == 'Screen Printing/T-Shirt Printing' 
             or elem == 'Self Storage' or elem == 'Septic Services' or elem == 'Sewing & Alterations' 
             or elem == 'Shipping Centers' or elem == 'Shoe Repair' or elem == 'Shoe Shine' or elem == 'Snow Removal' 
             or elem == 'Snuggle Services' or elem == 'Stonemasons' or elem == 'TV Mounting' 
             or elem == 'Watch Repair' or elem == 'Water Delivery' or elem == 'Well Drilling' or elem == 'Wildlife Control'):
             if 'Local Services' not in items:
                    items.append('Local Services')
        
        elif(elem == 'Mass Media' or elem == 'Print Media' or elem == 'Radio Stations' or elem == 'Television Stations'):
             if 'Mass Media' not in items:
                    items.append('Mass Media')
        
        elif(elem == 'Nightlife' or elem == 'Adult Entertainment' or elem == 'Strip Clubs' or elem == 'Striptease Dancers' 
             or elem == 'Bar Crawl' or elem == 'Bars' or elem == 'Airport Lounges' or elem == 'Beer Bar' 
             or elem == 'Champagne Bars' or elem == 'Cigar Bars' or elem == 'Cocktail Bars' or elem == 'Dive Bars' 
             or elem == 'Drive-Thru Bars' or elem == 'Gay Bars' or elem == 'Hookah Bars' or elem == 'Irish Pub' 
             or elem == 'Lounges' or elem == 'Pubs' or elem == 'Speakeasies' or elem == 'Sports Bars' 
             or elem == 'Tiki Bars' or elem == 'Vermouth Bars' or elem == 'Whiskey Bars' or elem == 'Wine Bars' 
             or elem == 'Beer Gardens' or elem == 'Club Crawl' or elem == 'Comedy Clubs' or elem == 'Country Dance Halls' 
             or elem == 'Dance Clubs' or elem == 'Jazz & Blues' or elem == 'Karaoke' or elem == 'Music Venues' 
             or elem == 'Piano Bars' or elem == 'Pool Halls'):
             if 'Nightlife' not in items:
                    items.append('Nightlife')
        
        elif(elem =='Pets' or elem == 'Animal Shelters' or elem == 'Horse Boarding' or elem == 'Pet Adoption' 
             or elem == 'Pet Services' or elem == 'Animal Physical Therapy' or elem == 'Aquarium Services' 
             or elem == 'Dog Walkers' or elem == 'Emergency Pet Hospital' or elem == 'Farriers' 
             or elem == 'Holistic Animal Care' or elem == 'Pet Breeders' or elem == 'Pet Cremation Services' 
             or elem == 'Pet Groomers' or elem == 'Pet Hospice' or elem == 'Pet Insurance' 
             or elem == 'Pet Photography' or elem == 'Pet Sitting' or elem == 'Pet Boarding' 
             or elem == 'Pet Training' or elem == 'Pet Transportation' or elem == 'Pet Waste Removal' 
             or elem == 'Pet Stores' or elem == 'Bird Shops' or elem == 'Local Fish Stores' 
             or elem == 'Reptile Shops' or elem == 'Veterinarians'):
             if 'Pets' not in items:
                    items.append('Pets')
        
        elif(elem == 'Professional Services' or elem == 'Accountants' or elem == 'Advertising' or elem == 'Architects' or elem == 'Art Consultants' 
             or elem == 'Billing Services' or elem == 'Boat Repair' or elem == 'Bookkeepers' 
             or elem == 'Business Consulting' or elem == 'Career Counseling' or elem == 'Commissioned Artists' 
             or elem == 'Customs Brokers' or elem == 'Digitizing Services' or elem == 'Duplication Services' 
             or elem == 'Editorial Services' or elem == 'Employment Agencies' or elem == 'Feng Shui' 
             or elem == 'Graphic Design' or elem == 'Indoor Landscaping' or elem == 'Internet Service Providers' 
             or elem == 'Lawyers' or elem == 'Bankruptcy Law' or elem == 'Business Law' or elem == 'Consumer Law' 
             or elem == 'Contract Law' or elem == 'Criminal Defense Law' or elem == 'DUI Law' 
             or elem == 'Disability Law' or elem == 'Divorce & Family Law' or elem == 'Elder Law' 
             or elem == 'Employment Law' or elem == 'Entertainment Law' or elem == 'Estate Planning Law' 
             or elem == 'Wills, Trusts, & Probates' or elem == 'General Litigation' or elem == 'IP & Internet Law' 
             or elem == 'Immigration Law' or elem == 'Medical Law' or elem == 'Personal Injury Law' 
             or elem == 'Real Estate Law' or elem == 'Social Security Law' or elem == 'Tax Law' 
             or elem == 'Traffic Ticketing Law' or elem == 'Workers Compensation Law' or elem == 'Legal Services' 
             or elem == 'Court Reporters' or elem == 'Process Servers' or elem == 'Life Coach' 
             or elem == 'Marketing' or elem == 'Matchmakers' or elem == 'Mediators' or elem == 'Music Production Services'
             or elem == 'Office Cleaning' or elem == 'Patent Law' or elem == 'Payroll Services' 
             or elem == 'Personal Assistants' or elem == 'Private Investigation' or elem == 'Product Design'
             or elem == 'Public Adjusters' or elem == 'Public Relations' or elem == 'Security Services' 
             or elem == 'Shredding Services' or elem == 'Signmaking' or elem == 'Software Development' 
             or elem == 'Talent Agencies' or elem == 'Taxidermy' or elem == 'Tenant and Eviction Law' 
             or elem == 'Translation Services' or elem == 'Video/Film Production' or elem == 'Web Design' 
             or elem == 'Wholesalers' or elem == 'Restaurant Supplies'):
             if 'Professional Services' not in items:
                    items.append('Professional Services')
        
        elif(elem == 'Public Services & Government' or elem == 'Civic Center' or elem == 'Community Centers' or elem == 'Courthouses' 
             or elem == 'Departments of Motor Vehicles' or elem == 'Embassy' or elem == 'Fire Departments' 
             or elem == 'Jails & Prisons' or elem == 'Landmarks & Historical Buildings' 
             or elem == 'Libraries' or elem == 'Municipality' or elem == 'Police Departments' 
             or elem == 'Post Offices' or elem == 'Town Hall'):
             if 'Public Services & Government' not in items:
                    items.append('Public Services & Government')
        
        
        elif(elem == 'Religious Organizations' or elem == 'Buddhist Temples' or elem == 'Churches' or elem == 'Hindu Temples' or elem == 'Mosques' 
             or elem == 'Sikh Temples' or elem == 'Synagogues'):
            if 'Religious Organizations' not in items:
                items.append('Religious Organizations')
        
        elif(elem == 'Restaurants' or elem == 'Afghan' or elem == 'African' or elem == 'Senegalese' or elem == 'South African' 
             or elem == 'American (New)' or elem == 'American (Traditional)' or elem == 'Arabian' 
             or elem == 'Argentine' or elem == 'Armenian' or elem == 'Asian Fusion' or elem == 'Australian' 
             or elem == 'Austrian' or elem == 'Bangladeshi' or elem == 'Barbeque' or elem == 'Basque' 
             or elem == 'Belgian' or elem == 'Brasseries' or elem == 'Brazilian' or elem == 'Breakfast & Brunch' 
             or elem == 'Pancakes' or elem == 'British' or elem == 'Buffets' or elem == 'Bulgarian' 
             or elem == 'Burgers' or elem == 'Burmese' or elem == 'Cafes' or elem == 'Themed Cafes' or elem == 'Cafeteria' 
             or elem == 'Cajun/Creole' or elem == 'Cambodian' or elem == 'Caribbean' or elem == 'Dominican' 
             or elem == 'Haitian' or elem == 'Puerto Rican' or elem == 'Trinidadian' or elem == 'Catalan' 
             or elem == 'Cheesesteaks' or elem == 'Chicken Shop' or elem == 'Chicken Wings' 
             or elem == 'Chinese' or elem == 'Cantonese' or elem == 'Dim Sum' or elem == 'Hainan' 
             or elem == 'Shanghainese' or elem == 'Szechuan' or elem == 'Comfort Food' or elem == 'Creperies' 
             or elem == 'Cuban' or elem == 'Czech' or elem == 'Delis' or elem == 'Diners' or elem == 'Dinner Theater'
             or elem == 'Eritrean' or elem == 'Ethiopian' or elem == 'Fast Food' or elem == 'Filipino' 
             or elem == 'Fish & Chips' or elem == 'Fondue' or elem == 'Food Court' or elem == 'Food Stands' 
             or elem == 'French' or elem == 'Mauritius' or elem == 'Reunion' or elem == 'Game Meat' 
             or elem == 'Gastropubs' or elem == 'Georgian' or elem == 'German' or elem == 'Gluten-Free' 
             or elem == 'Greek' or elem == 'Guamanian' or elem == 'Halal' or elem == 'Hawaiian' 
             or elem == 'Himalayan/Nepalese' or elem == 'Honduran' or elem == 'Hong Kong Style Cafe' 
             or elem == 'Hot Dogs' or elem == 'Hot Pot' or elem == 'Hungarian' or elem == 'Iberian' 
             or elem == 'Indian' or elem == 'Indonesian' or elem == 'Irish' or elem == 'Italian' 
             or elem == 'Calabrian' or elem == 'Sardinian' or elem == 'Sicilian' or elem == 'Tuscan' 
             or elem == 'Japanese' or elem == 'Conveyor Belt Sushi' or elem == 'Izakaya' or elem == 'Japanese Curry' 
             or elem == 'Ramen' or elem == 'Teppanyaki' or elem == 'Kebab' or elem == 'Korean' or elem == 'Kosher' 
             or elem == 'Laotian' or elem == 'Latin American' or elem == 'Colombian' or elem == 'Salvadoran' 
             or elem == 'Venezuelan' or elem == 'Live/Raw Food' or elem == 'Malaysian' or elem == 'Mediterranean' 
             or elem == 'Falafel' or elem == 'Mexican' or elem == 'Tacos' or elem == 'Middle Eastern' 
             or elem == 'Egyptian' or elem == 'Lebanese' or elem == 'Modern European' or elem == 'Mongolian' 
             or elem == 'Moroccan' or elem == 'New Mexican Cuisine' or elem == 'Nicaraguan' or elem == 'Noodles' 
             or elem == 'Pakistani' or elem == 'Pan Asia' or elem == 'Persian/Iranian' or elem == 'Peruvian' 
             or elem == 'Pizza' or elem == 'Polish' or elem == 'Polynesian' or elem == 'Pop-Up Restaurants' 
             or elem == 'Portuguese' or elem == 'Poutineries' or elem == 'Russian' or elem == 'Salad' 
             or elem == 'Sandwiches' or elem == 'Scandinavian' or elem == 'Scottish' or elem == 'Seafood' 
             or elem == 'Singaporean' or elem == 'Slovakian' or elem == 'Somali' or elem == 'Soul Food' 
             or elem == 'Soup' or elem == 'Southern' or elem == 'Spanish' or elem == 'Sri Lankan' 
             or elem == 'Steakhouses' or elem == 'Supper Clubs' or elem == 'Sushi Bars' or elem == 'Syrian' 
             or elem == 'Taiwanese' or elem == 'Tapas Bars' or elem == 'Tapas/Small Plates' 
             or elem == 'Tex-Mex' or elem == 'Thai' or elem == 'Turkish' or elem == 'Ukrainian' or elem == 'Uzbek' 
             or elem == 'Vegan' or elem == 'Vegetarian' or elem == 'Vietnamese' or elem == 'Waffles' 
             or elem == 'Wraps'):
             if 'Restaurants' not in items:
                    items.append('Restaurants')
        
        elif(elem == 'Shopping' or elem == 'Adult' or elem == 'Antiques' or elem == 'Art Galleries' or elem == 'Arts & Crafts' 
             or elem == 'Art Supplies' or elem == 'Cards & Stationery' or elem == 'Cooking Classes' 
             or elem == 'Costumes' or elem == 'Embroidery & Crochet' or elem == 'Fabric Stores' 
             or elem == 'Framing' or elem == 'Paint-Your-Own Pottery' or elem == 'Auction Houses' 
             or elem == 'Baby Gear & Furniture' or elem == 'Battery Stores' or elem == 'Bespoke Clothing' 
             or elem == 'Books, Mags, Music & Video' or elem == 'Bookstores' or elem == 'Comic Books' 
             or elem == 'Music & DVDs' or elem == 'Newspapers & Magazines' or elem == 'Video Game Stores' 
             or elem == 'Videos & Video Game Rental' or elem == 'Vinyl Records' or elem == 'Brewing Supplies' 
             or elem == 'Bridal' or elem == 'Cannabis Dispensaries' or elem == 'Computers' 
             or elem == 'Cosmetics & Beauty Supply' or elem == 'Customized Merchandise' or elem == 'Department Stores' 
             or elem == 'Diamond Buyers' or elem == 'Discount Store' or elem == 'Drones' or elem == 'Drugstores' 
             or elem == 'Duty-Free Shops' or elem == 'Electronics' or elem == 'Eyewear & Opticians' 
             or elem == 'Sunglasses' or elem == 'Farming Equipment' or elem == 'Fashion' or elem == 'Accessories' 
             or elem == 'Ceremonial Clothing' or elem == 'Children’s Clothing' or elem == 'Clothing Rental' 
             or elem == 'Department Stores' or elem == 'Formal Wear' or elem == 'Fur Clothing' or elem == 'Hats' 
             or elem == 'Leather Goods' or elem == 'Lingerie' or elem == 'Maternity Wear' or elem == 'Men’s Clothing' 
             or elem == 'Plus Size Fashion' or elem == 'Shoe Stores' or elem == 'Sports Wear' or elem == 'Dance Wear' 
             or elem == 'Surf Shop' or elem == 'Swimwear' or elem == 'Traditional Clothing' 
             or elem == 'Used, Vintage & Consignment' or elem == 'Women’s Clothing' or elem == 'Fireworks' 
             or elem == 'Fitness/Exercise Equipment' or elem == 'Flea Markets' or elem == 'Flowers & Gifts' 
             or elem == 'Cards & Stationery' or elem == 'Florists' or elem == 'Gift Shops' or elem == 'Gemstones & Minerals'
             or elem == 'Gold Buyers' or elem == 'Guns & Ammo' or elem == 'Head Shops' 
             or elem == 'High Fidelity Audio Equipment' or elem == 'Hobby Shops' or elem == 'Home & Garden' 
             or elem == 'Appliances' or elem == 'Candle Stores' or elem == 'Christmas Trees' 
             or elem == 'Furniture Stores' or elem == 'Grilling Equipment' or elem == 'Hardware Stores' 
             or elem == 'Holiday Decorations' or elem == 'Home Decor' or elem == 'Hot Tub & Pool' 
             or elem == 'Kitchen & Bath' or elem == 'Kitchen Supplies' or elem == 'Lighting Stores' 
             or elem == 'Mattresses' or elem == 'Nurseries & Gardening' or elem == 'Hydroponics' 
             or elem == 'Outdoor Furniture Stores' or elem == 'Paint Stores' or elem == 'Playsets' 
             or elem == 'Pumpkin Patches' or elem == 'Rugs' or elem == 'Sheds & Outdoor Storage' 
             or elem == 'Tableware' or elem == 'Horse Equipment Shops' or elem == 'Jewelry' or elem == 'Knitting Supplies' 
             or elem == 'Livestock Feed & Supply' or elem == 'Luggage' or elem == 'Medical Supplies' 
             or elem == 'Military Surplus' or elem == 'Mobile Phone Accessories' or elem == 'Mobile Phones' 
             or elem == 'Motorcycle Gear' or elem == 'Musical Instruments & Teachers' or elem == 'Office Equipment' 
             or elem == 'Outlet Stores' or elem == 'Packing Supplies' or elem == 'Pawn Shops' 
             or elem == 'Perfume' or elem == 'Personal Shopping' or elem == 'Photography Stores & Services' 
             or elem == 'Pool & Billiards' or elem == 'Pop-up Shops' or elem == 'Props' or elem == 'Public Markets' 
             or elem == 'Religious Items' or elem == 'Safe Stores' or elem == 'Safety Equipment' 
             or elem == 'Shopping Centers' or elem == 'Souvenir Shops' or elem == 'Spiritual Shop' 
             or elem == 'Sporting Goods' or elem == 'Bikes' or elem == 'Dive Shops' or elem == 'Golf Equipment' 
             or elem == 'Hockey Equipment' or elem == 'Hunting & Fishing Supplies' or elem == 'Outdoor Gear' 
             or elem == 'Skate Shops' or elem == 'Ski & Snowboard Shops' or elem == 'Sports Wear' 
             or elem == 'Dance Wear' or elem == 'Tabletop Games' or elem == 'Teacher Supplies' 
             or elem == 'Thrift Stores' or elem == 'Tobacco Shops' or elem == 'Toy Stores' or elem == 'Trophy Shops' 
             or elem == 'Uniforms' or elem == 'Used Bookstore' or elem == 'Vape Shops' 
             or elem == 'Vitamins & Supplements' or elem == 'Watches' or elem == 'Wholesale Stores' 
             or elem == 'Wigs'):
             if 'Shopping' not in items:
                    items.append('Shopping')
                    
        
    return items