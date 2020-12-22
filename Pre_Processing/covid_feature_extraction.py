import csv

'''
This function extracts value for a specific covid feature. Returns as binary (1/0)

Input: 1) elem: record
       2) feature: the specific covid feature

Output: binary value (1- True, 0 - False)
'''
def extract_covid_feature_value(elem, feature):
    
    if(feature == 'highlights'):
        
        if(elem['highlights'] != 'FALSE'):
            return 1
        else:
            return 0
    
    if(feature == 'Grubhub enabled'):
        
        if(elem['Grubhub enabled'] == 'TRUE'):
            return 1
        else:
            return 0
    
    
    if(feature == 'delivery or takeout'):
        
        if(elem['delivery or takeout'] == 'TRUE'):
            return 1
        else:
            return 0
    
    if(feature == 'Call To Action enabled'):
        
        if(elem['Call To Action enabled'] == 'TRUE'):
            return 1
        else:
            return 0
    
    
    if(feature == 'Request a Quote Enabled'):
        
        if(elem['Request a Quote Enabled'] == 'TRUE'):
             return 1
        else:
             return 0
                    
    if(feature == 'Covid Banner'):
        
        if(elem['Covid Banner'] != 'FALSE'):
            return 1
        else:
            return 0
    
    if(feature == 'Temporary Closed Until'):
        
        if(elem['Temporary Closed Until'] != 'FALSE'):
            return 1
        else:
            return 0
    
    if(feature == 'Virtual Services Offered'):
        
        if(elem['Virtual Services Offered'] != 'FALSE'):
            return 1
        else:
            return 0
    