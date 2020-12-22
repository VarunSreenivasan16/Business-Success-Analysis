import csv
import json

'''
This function creates a dictionary of the distinct business names in the records

Input: None

Output: A dictionary containg the distinct business names and the number of times they appear
'''
def get_business_names():
    
    business = open('yelp_academic_dataset_business.json', encoding = 'utf-8')
    business_count = {}
    
    for line in business:
        
        l = json.loads(line)
        name = l['name'].strip()
        
        if(name in business_count):
            business_count[name] += 1
        else:
            business_count[name] = 1
    
    return business_count
    
    
'''
This function identifies the region to which a state belongs to

Input: state

Output: a tuple of the regions (1- if state belongs to region, 0 otherwise)
'''
def identify_region(state):
    
    sw = 0
    w = 0
    mw = 0
    se = 0
    ne = 0
    
    if(state == 'AZ' or state == 'TX' or state == 'NM' or state == 'OK'):
        sw = 1
    
    elif(state == 'HI' or state == 'AK' or state == 'CA' or  state == 'NV' or state == 'UT' or state == 'CO' or state == 'WY'
      or state == 'ID' or state == 'OR' or state == 'MT' or state == 'WA' ):
        w = 1
    
    elif(state == 'ND' or state == 'SD' or state == 'NE' or state == 'KS' or state == 'MN' or state == 'IA' or state == 'MO'
      or state == 'WI' or state == 'IL' or state == 'IN' or state == 'MI' or state == 'OH'):
        mw = 1
        
    elif(state == 'AR' or state == 'LA' or state == 'MS' or state == 'AL' or state == 'GA' or state == 'FL' or state == 'TN' 
      or state == 'KY' or state == 'WV' or state == 'VA' or state == 'NC' or state == 'SC'):
        se = 1
    
    elif(state == 'ME' or state == 'NH' or state == 'MA' or state == 'RI' or state == 'CT' or state == 'VT' or state == 'NY'
      or state == 'PA' or state == 'NJ' or state == 'DE' or state == 'MD'):
        ne = 1
    
    return (sw, w, mw, se, ne)


'''
This fuction checks if the business accepts credit cards

Input: 1) Business record
       2) the attribute

Output: 1 if attribute is BusinessAcceptsCreditCards and corresponding value is true
        0 otherwise
'''
def check_Business_Cards(key, line):
    
    if(key == 'BusinessAcceptsCreditCards'):
        
        if(line['attributes']['BusinessAcceptsCreditCards'] == 'True'):
            return 1
        
    return 0


'''
This function checks if the business offers bike parking

Input: 1) Business record
       2) the attribute
       
Output: 1 if attribute is BikeParking and corresponding value is true
        0 otherwise
'''
def check_Bike_Parking(key, line):
    
    if(key == 'BikeParking'):
                    
        if(line['attributes']['BikeParking'] == 'True'):
             return 1
    
    return 0        

'''
This function checks if business offers WiFi

Input: 1) Business record
       2) the attribute
       
Output: 1 if attribute is WiFi and business offers WiFi
        0 otherwise
'''
def check_wifi(key, line):
    
    if(key == 'WiFi'):
                    
        str_split = line['attributes']['WiFi'].split("'")
                    
        if(len(str_split) > 1):
                        
            val = str_split[1]
                        
            if(val == 'free' or val == 'paid'):
                return 1
    
    return 0

'''
This function checks if business offers alcohol

Input: 1) Business record
       2) the attribute
       
Output: 1 if attribute is Alcohol and business offers alcohol
        0 otherwise
'''
def check_alcohol(key, line):
    
    if(key == 'Alcohol'):
                    
        if('none' not in line['attributes']['Alcohol']):
            return 1
    
    return 0


'''
This function checks if business has a TV

Input: 1) Business record
       2) the attribute

Output: 1 if attribute is HasTV and corresponding value is true
        0 otherwise
'''
def check_TV(key, line):
    
    if(key == 'HasTV'):
                    
        if(line['attributes']['HasTV'] == 'True'):
            return 1
    
    return 0

'''
This function checks if a business offers outdoor seating

Input: 1) Business record
       2) the attribute
       
Output: 1 if attribute if OutdoorSeating and corresponding value is True
        0 otherwise
'''
def check_outdoor_seating(key, line):
    
    if(key == 'OutdoorSeating'):
                    
        if(line['attributes']['OutdoorSeating'] == 'True'):
            return 1
    
    return 0


'''
This function determines the noise level at a business

Input: 1) Business record
       2) the attribute
       
Output: 1 if attribute is NoiseLevel and corresponding value is quiet
        3 if attribute is NoiseLevel and corresponding value is loud
        4 if attribute is NoiseLevel and corresponding value is very loud
        2 otherwise
'''
def check_noise_level(key, line):
    
    if(key == 'NoiseLevel'):
                    
        if('quiet' in line['attributes']['NoiseLevel']):
            return 1
                    
        elif('average' in line['attributes']['NoiseLevel']):
            return 2
                    
        elif('very_loud' in line['attributes']['NoiseLevel']):
            return 4
                    
        elif('loud' in line['attributes']['NoiseLevel']):
            return 3
    
    return 2


'''
This function determines price range for a business

Input: 1) Business record
       2) the attribute

Output: 1 if attribute is RestaurantsPriceRange2 and corresponding value is 1
        3 if attribute is RestaurantsPriceRange2 and corresponding value is 3
        4 if attribute is RestaurantsPriceRange2 and corresponding value is 4
        2 otherwise
'''
def check_Price_Range(key, line):
    
    if(key == 'RestaurantsPriceRange2'):
                
        if(line['attributes']['RestaurantsPriceRange2'] == '1'):
            return 1
                                              
        elif(line['attributes']['RestaurantsPriceRange2'] == '2'):
            return 2
                
        elif(line['attributes']['RestaurantsPriceRange2'] == '3'):
            return 3
                    
        elif(line['attributes']['RestaurantsPriceRange2'] == '4'):
            return 4
    
    return 2


'''
This function checks if a business offers Business Parking

Input: 1) Business record
       2) the attribute
       
Output : 1 if attribute is BusinessParking and business offers parking
         0 otherwise
'''
def check_Business_Parking(key, line):
    
    if(key != 'BusinessParking'):
            return 0
        
    elif(key == 'BusinessParking'):
                   
        parking_split = line['attributes']['BusinessParking'].split(',')
                    
                    
        garage = 0
        street = 0
        validated = 0
        lot = 0
        valet = 0
                    
        if(len(parking_split) == 5):
                       
            garage_split = parking_split[0]
            garage_split1 = garage_split.split(':')
                        
            if(len(garage_split1) > 1):
                garage_split2 = garage_split1[1].strip()
                            
                if(garage_split2 == 'True'):
                    garage = 1
            
            
            street_split = parking_split[1]
            street_split1 = street_split.split(':')
                        
            if(len(street_split1) > 1):
                street_split2 = street_split1[1].strip()
                            
                if(street_split2 == 'True'):
                    street = 1
                        
                        
            validated_split = parking_split[2]
            validated_split1 = validated_split.split(':')
                        
            if(len(validated_split1) > 1):
                validated_split2 = validated_split1[1].strip()
                            
                if(validated_split2 == 'True'):
                    validated = 1
                        
    
            lot_split = parking_split[3]
            lot_split1 = lot_split.split(':')
            
            if(len(lot_split1) > 1):
                lot_split2 = lot_split1[1].strip()
                                
                if(lot_split2 == 'True'):
                    lot = 1
                        
            valet_split = parking_split[4]
            valet_split1 = valet_split.split(':')
                        
            if(len(valet_split1) > 1):
                valet_split2 = valet_split1[1].strip()
                                
                if(valet_split2 == 'True'):
                    valet = 1 
                    
                    
            if(garage == 1 or street == 1 or validated == 1 or lot == 1 or valet == 1):
                return 1
            else:
                return 0
        
        
    return 0  
 
                    