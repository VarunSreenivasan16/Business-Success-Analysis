import csv

'''
This function returns the population for a specific postcode in a state

Input: 1) post_code
       2) state
       3) state_population_list: a list of dictionaries. Each dictionary contains population for all postcodes in a state

Output: population for a specific postcode in a state

#Note: There are some missing values. That is population isn't available for some postcodes. We use the mean of population over remaining
       postcodes in the state to fill in. 
'''
def get_population_for_postcode(post_code, state, state_population_list):
    
    population = 0
    
    if(state == 'AL'):
        
        if(post_code in state_population_list[0]):
            population = state_population_list[0][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[0])
        
    elif(state == 'AK'):
        
        if(post_code in state_population_list[1]):
            population = state_population_list[1][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[1])
    
    elif(state == 'AZ'):
         
        if(post_code in state_population_list[2]):
            population = state_population_list[2][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[2]) 
        
    elif(state == 'AR'):
        
        if(post_code in state_population_list[3]):
            population = state_population_list[3][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[3])
        
    elif(state == 'CA'):
        
        if(post_code in state_population_list[4]):
            population = state_population_list[4][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[4])
            
    elif(state == 'CO'):
        
        if(post_code in state_population_list[5]):
            population = state_population_list[5][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[5])    
            
        
    elif(state == 'CT'):
        
        if(post_code in state_population_list[6]):
            population = state_population_list[6][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[6])    
    
    elif(state == 'DE'):
        
        if(post_code in state_population_list[7]):
            population = state_population_list[7][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[7]) 
        
    elif(state == 'FL'):
        
        if(post_code in state_population_list[8]):
            population = state_population_list[8][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[8])
       
    elif(state == 'GA'):
        
        if(post_code in state_population_list[9]):
            population = state_population_list[9][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[9])
            
    elif(state == 'HI'):
        
        if(post_code in state_population_list[10]):
            population = state_population_list[10][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[10])
            
    elif(state == 'ID'):
        
        if(post_code in state_population_list[11]):
            population = state_population_list[11][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[11])    
            
    elif(state == 'IL'):
        
        if(post_code in state_population_list[12]):
            population = state_population_list[12][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[12])
        
    elif(state == 'IN'):
        
        if(post_code in state_population_list[13]):
            population = state_population_list[13][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[13])
        
    elif(state == 'IA'):
        
        if(post_code in state_population_list[14]):
            population = state_population_list[14][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[14])
        
    elif(state == 'KS'):
        
        if(post_code in state_population_list[15]):
            population = state_population_list[15][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[15])
        
    elif(state == 'KY'):
        
        if(post_code in state_population_list[16]):
            population = state_population_list[16][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[16])
        
    elif(state == 'LA'):
        
        if(post_code in state_population_list[17]):
            population = state_population_list[17][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[17])
        
    elif(state == 'ME'):
        
        if(post_code in state_population_list[18]):
            population = state_population_list[18][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[18])
        
    elif(state == 'MD'):
        
        if(post_code in state_population_list[19]):
            population = state_population_list[19][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[19])
        
    elif(state == 'MA'):
        
        if(post_code in state_population_list[20]):
            population = state_population_list[20][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[20])
        
    elif(state == 'MI'):
        
        if(post_code in state_population_list[21]):
            population = state_population_list[21][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[21])
            
    elif(state == 'MN'):
        
        if(post_code in state_population_list[22]):
            population = state_population_list[22][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[22])
        
    elif(state == 'MS'):
        
        if(post_code in state_population_list[23]):
            population = state_population_list[23][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[23])
        
    elif(state == 'MO'):
        
        if(post_code in state_population_list[24]):
            population = state_population_list[24][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[24])
        
    elif(state == 'MT'):
        
        if(post_code in state_population_list[25]):
            population = state_population_list[25][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[25])
        
    elif(state == 'NE'):
        
        if(post_code in state_population_list[26]):
            population = state_population_list[26][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[26])
        
    elif(state == 'NV'):
        
        if(post_code in state_population_list[27]):
            population = state_population_list[27][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[27])
        
    elif(state == 'NH'):
        
        if(post_code in state_population_list[28]):
            population = state_population_list[28][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[28])
        
    elif(state == 'NJ'):
        
        if(post_code in state_population_list[29]):
            population = state_population_list[29][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[29]) 
            
    elif(state == 'NM'):
        
        if(post_code in state_population_list[30]):
            population = state_population_list[30][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[30])
            
    elif(state == 'NY'):
        
        if(post_code in state_population_list[31]):
            population = state_population_list[31][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[31])
            
    elif(state == 'NC'):
        
        if(post_code in state_population_list[32]):
            population = state_population_list[32][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[32])
            
    elif(state == 'ND'):
        
        if(post_code in state_population_list[33]):
            population = state_population_list[33][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[33])
            
    elif(state == 'OH'):
         
        if(post_code in state_population_list[34]):
            population = state_population_list[34][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[34])
    
    elif(state == 'OK'):
        
        if(post_code in state_population_list[35]):
            population = state_population_list[35][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[35])    
        
    elif(state == 'OR'):
        
        if(post_code in state_population_list[36]):
            population = state_population_list[36][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[36])
            
    elif(state == 'PA'):
        
        if(post_code in state_population_list[37]):
            population = state_population_list[37][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[37])
            
    elif(state == 'RI'):
        
        if(post_code in state_population_list[38]):
            population = state_population_list[38][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[38])
            
    elif(state == 'SC'):
        
        if(post_code in state_population_list[39]):
            population = state_population_list[39][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[39])
            
    elif(state == 'SD'):
        
        if(post_code in state_population_list[40]):
            population = state_population_list[40][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[40])
            
    elif(state == 'TN'):
        
        if(post_code in state_population_list[41]):
            population = state_population_list[41][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[41])
            
    elif(state == 'TX'):
        
        if(post_code in state_population_list[42]):
            population = state_population_list[42][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[42])
            
    elif(state == 'UT'):
        
        if(post_code in state_population_list[43]):
            population = state_population_list[43][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[43])
            
    elif(state == 'VT'):
        
        if(post_code in state_population_list[44]):
            population = state_population_list[44][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[44])
            
    elif(state == 'VA'):
        
        if(post_code in state_population_list[45]):
            population = state_population_list[45][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[45]) 
        
    elif(state == 'WA'):
        
        if(post_code in state_population_list[46]):
            population = state_population_list[46][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[46])
            
    elif(state == 'WV'):
        
        if(post_code in state_population_list[47]):
            population = state_population_list[47][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[47])
            
    elif(state == 'WI'):
        
        if(post_code in state_population_list[48]):
            population = state_population_list[48][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[48])
            
    elif(state == 'WY'):
        
        if(post_code in state_income_list[49]):
            population = state_population_list[49][post_code]
        else:
            population = get_mean_population_for_state(state_population_list[49])
   
    
    return population


'''
Function used to fill missing population values for a postcode using the average population for the state over other postcodes

Input: population_state: a dictionary of postcodes with corresponding population values

Output: mean population
'''
def get_mean_population_for_state(population_state):
    
    total_state_population = 0
    num_postcodes = 0
    
    for key in population_state:
        
        total_state_population += population_state[key]
        num_postcodes += 1
    
    mean_population = int(total_state_population / num_postcodes)
    
    return mean_population


'''
Function that creates a list of dictionaries. Each dictionary contains population for the postcodes in a state.

Input: None

Output: a list of dictionaries containing population for the postcodes in a state.
'''
def extract_Population():
    
    state_population_list = []
    Alabama = {}
    Alaska = {}
    Arizona = {}
    Arkansas = {}
    California = {}
    Colorado = {}
    Connecticut = {}
    Delaware = {}
    Florida = {}
    Georgia = {}
    Hawaii = {}
    Idaho = {}
    Illinois = {}
    Indiana = {}
    Iowa = {}
    Kansas = {}
    Kentucky = {}
    Louisiana = {}
    Maine = {}
    Maryland = {}
    Massachusetts = {}
    Michigan = {}
    Minnesota = {}
    Mississippi = {}
    Missouri = {}
    Montana = {}
    Nebraska = {}
    Nevada = {}
    NewHampshire = {}
    NewJersey = {}
    NewMexico = {}
    NewYork = {}
    NorthCarolina = {}
    NorthDakota = {}
    Ohio = {}
    Oklahoma = {}
    Oregon = {}
    Pennsylvania = {}
    RhodeIsland = {}
    SouthCarolina = {}
    SouthDakota = {}
    Tennessee = {}
    Texas = {}
    Utah = {}
    Vermont = {}
    Virginia = {}
    Washington = {}
    WestVirginia = {}
    Wisconsin = {}
    Wyoming = {}
    
    directory = 'Population/zip_code_database.csv'
    
    with open(directory) as csvfile:
    
        readCSV = csv.reader(csvfile)
    
        for row in readCSV:
        
            zip_code = row[0]
        
            if(len(zip_code) == 3):
                continue
        
            if(len(zip_code) == 4):
            
                zip_code = '0' + zip_code
        
            state = row[6]
            population = int(row[14])
        
            if(state == 'AL'):
                Alabama[zip_code] = population 
        
       
            elif(state == 'AK'):
                Alaska[zip_code] = population
        
       
            
            elif(state == 'AZ'):
                Arizona[zip_code] = population
        
        
            elif(state == 'AR'):
                Arkansas[zip_code] = population
        
        
            elif(state == 'CA'):
                California[zip_code] = population
       
            
            elif(state == 'CO'):
                Colorado[zip_code] = population
        
        
            elif(state == 'CT'):
                Connecticut[zip_code] = population
            
    
            elif(state == 'DE'):
                Delaware[zip_code] = population
        
            
            elif(state == 'FL'):
                Florida[zip_code] = population
       
       
            elif(state == 'GA'):
                Georgia[zip_code] = population
       
            
            elif(state == 'HI'):
                Hawaii[zip_code] = population
       
            
            elif(state == 'ID'):
                Idaho[zip_code] = population
        
            
            elif(state == 'IL'):
                Illinois[zip_code] = population
       
        
            elif(state == 'IN'):
                Indiana[zip_code] = population
        
        
            elif(state == 'IA'):
                Iowa[zip_code] = population
       
        
            elif(state == 'KS'):
                Kansas[zip_code] = population
        
        
            elif(state == 'KY'):
                Kentucky[zip_code] = population
     
        
            elif(state == 'LA'):
                Louisiana[zip_code] = population
     
            elif(state == 'ME'):
                Maine[zip_code] = population
      
        
            elif(state == 'MD'):
                Maryland[zip_code] = population
      
            elif(state == 'MA'):
                Massachusetts[zip_code] = population
        
            elif(state == 'MI'):
                Michigan[zip_code] = population

            elif(state == 'MN'):
                Minnesota[zip_code] = population
     
        
            elif(state == 'MS'):
                Mississippi[zip_code] = population
      
        
            elif(state == 'MO'):
                Missouri[zip_code] = population

        
            elif(state == 'MT'):
                Montana[zip_code] = population
    
        
            elif(state == 'NE'):
                Nebraska[zip_code] = population
     
        
            elif(state == 'NV'):
                Nevada[zip_code] = population
     
        
            elif(state == 'NH'):
                NewHampshire[zip_code] = population
     
        
            elif(state == 'NJ'):
                NewJersey[zip_code] = population
  
            elif(state == 'NM'):
                NewMexico[zip_code] = population
     
            elif(state == 'NY'):
                NewYork[zip_code] = population
      
            
            elif(state == 'NC'):
                NorthCarolina[zip_code] = population
     
            
            elif(state == 'ND'):
                NorthDakota[zip_code] = population
    
    
            elif(state == 'OH'):
                Ohio[zip_code] = population
    
    
            elif(state == 'OK'):
                Oklahoma[zip_code] = population
       
    
            elif(state == 'OR'):
                Oregon[zip_code] = population
       
            
            elif(state == 'PA'):
                Pennsylvania[zip_code] = population
       
            elif(state == 'RI'):
                RhodeIsland[zip_code] = population
       
            
            elif(state == 'SC'):
                SouthCarolina[zip_code] = population
        
            
            elif(state == 'SD'):
                SouthDakota[zip_code] = population
        
        
            elif(state == 'TN'):
                Tennessee[zip_code] = population
       
            
            elif(state == 'TX'):
                Texas[zip_code] = population
        
            
            elif(state == 'UT'):
                Utah[zip_code] = population
       
            
            elif(state == 'VT'):
                Vermont[zip_code] = population
            
            elif(state == 'VA'):
                Virginia[zip_code] = population
       
        
            elif(state == 'WA'):
                Washington[zip_code] = population
      
            elif(state == 'WV'):
                WestVirginia[zip_code] = population
        
            
            elif(state == 'WI'):
                Wisconsin[zip_code] = population
       
            
            elif(state == 'WY'):
                Wyoming[zip_code] = population
        
 
        
     
    state_population_list.append(Alabama)
    state_population_list.append(Alaska)
    state_population_list.append(Arizona)
    state_population_list.append(Arkansas)
    state_population_list.append(California)
    state_population_list.append(Colorado)
    state_population_list.append(Connecticut)
    state_population_list.append(Delaware)
    state_population_list.append(Florida)
    state_population_list.append(Georgia)
    state_population_list.append(Hawaii)
    state_population_list.append(Idaho)
    state_population_list.append(Illinois)
    state_population_list.append(Indiana)
    state_population_list.append(Iowa)
    state_population_list.append(Kansas)
    state_population_list.append(Kentucky)
    state_population_list.append(Louisiana)
    state_population_list.append(Maine)
    state_population_list.append(Maryland)
    state_population_list.append(Massachusetts)
    state_population_list.append(Michigan)
    state_population_list.append(Minnesota)
    state_population_list.append(Mississippi)
    state_population_list.append(Missouri)
    state_population_list.append(Montana)
    state_population_list.append(Nebraska)
    state_population_list.append(Nevada)
    state_population_list.append(NewHampshire)
    state_population_list.append(NewJersey)
    state_population_list.append(NewMexico)
    state_population_list.append(NewYork)
    state_population_list.append(NorthCarolina)
    state_population_list.append(NorthDakota)
    state_population_list.append(Ohio)
    state_population_list.append(Oklahoma)
    state_population_list.append(Oregon)
    state_population_list.append(Pennsylvania)
    state_population_list.append(RhodeIsland)
    state_population_list.append(SouthCarolina)
    state_population_list.append(SouthDakota)
    state_population_list.append(Tennessee)
    state_population_list.append(Texas)
    state_population_list.append(Utah)
    state_population_list.append(Vermont)
    state_population_list.append(Virginia)
    state_population_list.append(Washington)
    state_population_list.append(WestVirginia)
    state_population_list.append(Wisconsin)
    state_population_list.append(Wyoming)
    
    
    return state_population_list