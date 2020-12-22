import csv

'''
This function finds the income category for a specific postcode in a state

Input: 1) post_code: the specific postcode
       2) state: the American state
       3) state_income_list: a list of dictionaries for all states

Output: income category
'''
def get_income_for_postcode(post_code, state, state_income_list):
    
    income = 3
    
    if(state == 'AL'):
        
        if(post_code in state_income_list[0]):
            income = state_income_list[0][post_code]
    
        
    elif(state == 'AK'):
        
        if(post_code in state_income_list[1]):
            income = state_income_list[1][post_code]
    
    
    elif(state == 'AZ'):
         
        if(post_code in state_income_list[2]):
            income = state_income_list[2][post_code]
            
    elif(state == 'AR'):
        
         if(post_code in state_income_list[3]):
            income = state_income_list[3][post_code]
        
    elif(state == 'CA'):
        
         if(post_code in state_income_list[4]):
            income = state_income_list[4][post_code]
        
    elif(state == 'CO'):
        
         if(post_code in state_income_list[5]):
            income = state_income_list[5][post_code]
        
    elif(state == 'CT'):
        
         if(post_code in state_income_list[6]):
            income = state_income_list[6][post_code]
       
    elif(state == 'DE'):
        
         if(post_code in state_income_list[7]):
            income = state_income_list[7][post_code]
            
    elif(state == 'FL'):
        
         if(post_code in state_income_list[8]):
            income = state_income_list[8][post_code]
       
    elif(state == 'GA'):
        
         if(post_code in state_income_list[9]):
            income = state_income_list[9][post_code]
            
    elif(state == 'HI'):
        
         if(post_code in state_income_list[10]):
            income = state_income_list[10][post_code]
            
    elif(state == 'ID'):
        
         if(post_code in state_income_list[11]):
            income = state_income_list[11][post_code]
            
    elif(state == 'IL'):
        
         if(post_code in state_income_list[12]):
            income = state_income_list[12][post_code]
        
    elif(state == 'IN'):
        
         if(post_code in state_income_list[13]):
            income = state_income_list[13][post_code]
            
    elif(state == 'IA'):
        
         if(post_code in state_income_list[14]):
            income = state_income_list[14][post_code]
            
    elif(state == 'KS'):
        
         if(post_code in state_income_list[15]):
            income = state_income_list[15][post_code]
        
    elif(state == 'KY'):
        
         if(post_code in state_income_list[16]):
            income = state_income_list[16][post_code]
        
    elif(state == 'LA'):
        
         if(post_code in state_income_list[17]):
            income = state_income_list[17][post_code]
        
    elif(state == 'ME'):
        
         if(post_code in state_income_list[18]):
            income = state_income_list[18][post_code]
            
    elif(state == 'MD'):
        
         if(post_code in state_income_list[19]):
            income = state_income_list[19][post_code]
        
    elif(state == 'MA'):
        
         if(post_code in state_income_list[20]):
            income = state_income_list[20][post_code]
            
    elif(state == 'MI'):
        
         if(post_code in state_income_list[21]):
            income = state_income_list[21][post_code]
            
    elif(state == 'MN'):
        
         if(post_code in state_income_list[22]):
            income = state_income_list[22][post_code]
        
    elif(state == 'MS'):
        
         if(post_code in state_income_list[23]):
            income = state_income_list[23][post_code]
            
    elif(state == 'MO'):
        
         if(post_code in state_income_list[24]):
            income = state_income_list[24][post_code]
            
    elif(state == 'MT'):
        
         if(post_code in state_income_list[25]):
            income = state_income_list[25][post_code]
            
    elif(state == 'NE'):
        
         if(post_code in state_income_list[26]):
            income = state_income_list[26][post_code]
            
    elif(state == 'NV'):
        
         if(post_code in state_income_list[27]):
            income = state_income_list[27][post_code]
            
    elif(state == 'NH'):
        
         if(post_code in state_income_list[28]):
            income = state_income_list[28][post_code]
            
    elif(state == 'NJ'):
        
         if(post_code in state_income_list[29]):
            income = state_income_list[29][post_code]
        
    elif(state == 'NM'):
        
         if(post_code in state_income_list[30]):
            income = state_income_list[30][post_code]
            
    elif(state == 'NY'):
        
         if(post_code in state_income_list[31]):
            income = state_income_list[31][post_code]
            
    elif(state == 'NC'):
        
         if(post_code in state_income_list[32]):
            income = state_income_list[32][post_code]
            
    elif(state == 'ND'):
        
         if(post_code in state_income_list[33]):
            income = state_income_list[33][post_code]
            
    elif(state == 'OH'):
         
        if(post_code in state_income_list[34]):
            income = state_income_list[34][post_code]
    
    elif(state == 'OK'):
        
         if(post_code in state_income_list[35]):
            income = state_income_list[35][post_code]
            
    elif(state == 'OR'):
        
         if(post_code in state_income_list[36]):
            income = state_income_list[36][post_code]
            
    elif(state == 'PA'):
        
         if(post_code in state_income_list[37]):
            income = state_income_list[37][post_code]
            
    elif(state == 'RI'):
        
         if(post_code in state_income_list[38]):
            income = state_income_list[38][post_code]
            
    elif(state == 'SC'):
        
         if(post_code in state_income_list[39]):
            income = state_income_list[39][post_code]
            
    elif(state == 'SD'):
        
         if(post_code in state_income_list[40]):
            income = state_income_list[40][post_code]
            
    elif(state == 'TN'):
        
         if(post_code in state_income_list[41]):
            income = state_income_list[41][post_code]
            
    elif(state == 'TX'):
        
         if(post_code in state_income_list[42]):
            income = state_income_list[42][post_code]
            
    elif(state == 'UT'):
        
         if(post_code in state_income_list[43]):
            income = state_income_list[43][post_code]
            
    elif(state == 'VT'):
        
         if(post_code in state_income_list[44]):
            income = state_income_list[44][post_code]
            
    elif(state == 'VA'):
        
         if(post_code in state_income_list[45]):
            income = state_income_list[45][post_code]
            
    elif(state == 'WA'):
        
         if(post_code in state_income_list[46]):
            income = state_income_list[46][post_code]
            
    elif(state == 'WV'):
        
         if(post_code in state_income_list[47]):
            income = state_income_list[47][post_code]
            
    elif(state == 'WI'):
        
         if(post_code in state_income_list[48]):
            income = state_income_list[48][post_code]
            
    elif(state == 'WY'):
        
         if(post_code in state_income_list[49]):
            income = state_income_list[49][post_code]
 
    
    return income


'''
This function creates a list containing a dictionary for each state. Each dictionary contains income category for
     each postcode in the state

Input: None

Output: a list of dictionaries.
'''
def income_dictionary():
    
    Alabama = extract_income('Alabama')
    Alaska = extract_income('Alaska')
    Arizona = extract_income('Arizona')
    Arkansas = extract_income('Arkansas')
    California = extract_income('California')
    Colorado = extract_income('Colorado')
    Connecticut = extract_income('Connecticut')
    Delaware = extract_income('Delaware')
    Florida = extract_income('Florida')
    Georgia = extract_income('Georgia')
    Hawaii = extract_income('Hawaii')
    Idaho = extract_income('Idaho')
    Illinois = extract_income('Illinois')
    Indiana = extract_income('Indiana')
    Iowa = extract_income('Iowa')
    Kansas = extract_income('Kansas')
    Kentucky = extract_income('Kentucky')
    Louisiana = extract_income('Louisiana')
    Maine = extract_income('Maine')
    Maryland = extract_income('Maryland')
    Massachusetts = extract_income('Massachusetts')
    Michigan = extract_income('Michigan')
    Minnesota = extract_income('Minnesota')
    Mississippi = extract_income('Mississippi')
    Missouri = extract_income('Missouri')
    Montana = extract_income('Montana')
    Nebraska = extract_income('Nebraska')
    Nevada = extract_income('Nevada')
    NewHampshire = extract_income('NewHampshire')
    NewJersey = extract_income('NewJersey')
    NewMexico = extract_income('NewMexico')
    NewYork = extract_income('NewYork')
    NorthCarolina = extract_income('NorthCarolina')
    NorthDakota = extract_income('NorthDakota')
    Ohio = extract_income('Ohio')
    Oklahoma = extract_income('Oklahoma')
    Oregon = extract_income('Oregon')
    Pennsylvania = extract_income('Pennsylvania')
    RhodeIsland = extract_income('RhodeIsland')
    SouthCarolina = extract_income('SouthCarolina')
    SouthDakota = extract_income('SouthDakota')
    Tennessee = extract_income('Tennessee')
    Texas = extract_income('Texas')
    Utah = extract_income('Utah')
    Vermont = extract_income('Vermont')
    Virginia = extract_income('Virginia')
    Washington = extract_income('Washington')
    WestVirginia = extract_income('WestVirginia')
    Wisconsin = extract_income('Wisconsin')
    Wyoming = extract_income('Wyoming')

    state_income_list = []
    state_income_list.append(Alabama)
    state_income_list.append(Alaska)
    state_income_list.append(Arizona)
    state_income_list.append(Arkansas)
    state_income_list.append(California)
    state_income_list.append(Colorado)
    state_income_list.append(Connecticut)
    state_income_list.append(Delaware)
    state_income_list.append(Florida)
    state_income_list.append(Georgia)
    state_income_list.append(Hawaii)
    state_income_list.append(Idaho)
    state_income_list.append(Illinois)
    state_income_list.append(Indiana)
    state_income_list.append(Iowa)
    state_income_list.append(Kansas)
    state_income_list.append(Kentucky)
    state_income_list.append(Louisiana)
    state_income_list.append(Maine)
    state_income_list.append(Maryland)
    state_income_list.append(Massachusetts)
    state_income_list.append(Michigan)
    state_income_list.append(Minnesota)
    state_income_list.append(Mississippi)
    state_income_list.append(Missouri)
    state_income_list.append(Montana)
    state_income_list.append(Nebraska)
    state_income_list.append(Nevada)
    state_income_list.append(NewHampshire)
    state_income_list.append(NewJersey)
    state_income_list.append(NewMexico)
    state_income_list.append(NewYork)
    state_income_list.append(NorthCarolina)
    state_income_list.append(NorthDakota)
    state_income_list.append(Ohio)
    state_income_list.append(Oklahoma)
    state_income_list.append(Oregon)
    state_income_list.append(Pennsylvania)
    state_income_list.append(RhodeIsland)
    state_income_list.append(SouthCarolina)
    state_income_list.append(SouthDakota)
    state_income_list.append(Tennessee)
    state_income_list.append(Texas)
    state_income_list.append(Utah)
    state_income_list.append(Vermont)
    state_income_list.append(Virginia)
    state_income_list.append(Washington)
    state_income_list.append(WestVirginia)
    state_income_list.append(Wisconsin)
    state_income_list.append(Wyoming)
    
    
    return state_income_list


'''
This function creates a dictionary for each state containing income categories for all the postcodes in the state

Input: 1) state

Output: dictionary containing income categories for all the postcodes in the state
'''
def extract_income(state):
    
    dictionary = {}
    
    directory = 'State_Incomes/Parsed/' + state + '.csv'
    
    with open(directory) as csvfile:
    
        readCSV = csv.reader(csvfile)
    
        i = 0
    
        temp_dictionary = {}
        temp_dictionary['1'] = 0
        temp_dictionary['2'] = 0
        temp_dictionary['3'] = 0
        temp_dictionary['4'] = 0
        temp_dictionary['5'] = 0
        temp_dictionary['6'] = 0
        postcode = 0
    
        for row in readCSV:
        
       
            
            if(i == 0): 
                i += 1
    
            elif(i == 1):
                postcode = row[0]
                if(row[2] != '**' and row[2] != '.' and row[2] != '' ):
                    temp_dictionary['1'] += int(row[2])
                
                i += 1 
        
            elif(i == 2):
                if(row[2] != '**' and row[2] != '.' and row[2] != ''):
                    temp_dictionary['2'] += int(row[2])
                i += 1 
        
            elif(i == 3):
                if(row[2] != '**' and row[2] != '.' and row[2] != ''):
                    temp_dictionary['3'] += int(row[2])
                i += 1 
        
            elif(i == 4):
                if(row[2] != '**' and row[2] != '.' and row[2] != ''):
                    temp_dictionary['4'] += int(row[2])
                i += 1 
        
            elif(i == 5):
                if(row[2] != '**' and row[2] != '.' and row[2] != ''):
                    temp_dictionary['5'] += int(row[2])
                i += 1 
        
            elif(i == 6):
                if(row[2] != '**' and row[2] != '.' and row[2] != ''):
                    temp_dictionary['6'] += int(row[2])
                i += 1 
        
            elif(i == 7):
            
                i = 0
                total = 0
                check_median = 0
            
                for key in temp_dictionary:
                    total += temp_dictionary[key]
            
                index = 1
            
                for key in temp_dictionary:
                 
                    if((check_median < total/2) and (check_median + temp_dictionary[key] > total/2)):
                        
                        if(state == 'Connecticut' or state == 'Maine' or state == 'Massachusetts' or state == 'NewHampshire' 
                            or state == 'NewJersey' or state == 'RhodeIsland' or state == 'Vermont'):
                                postcode = '0' + postcode
                        
                        dictionary[postcode] = index
                        temp_dictionary['1'] = 0
                        temp_dictionary['2'] = 0
                        temp_dictionary['3'] = 0
                        temp_dictionary['4'] = 0
                        temp_dictionary['5'] = 0
                        temp_dictionary['6'] = 0
                        break
                
                    else:
                        index += 1
                        check_median += temp_dictionary[key]
                    
    
    return dictionary