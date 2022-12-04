
def ruleOut(filename):
    list= ['anti-D','anti-C','anti-E','anti-c','anti-e','anti-f',
           'anti-Cw','anti-V','anti-K','anti-k','anti-Kpa','anti-Kpb',
           'anti-Jsa','anti-Jsb','anti-Fya','anti-Fyb','anti-Jka','anti-Jkb',
           'anti-Xga','anti-Lea','anti-Leb','anti-S','anti-s','anti-M',
           'anti-N']
    data = open(filename, 'r')
    read_data= data.readlines()
    data_without_newline_char = [i[:-1] for i in read_data]
    
    each_line_split =[]
    for j in data_without_newline_char:
        split = j.split(',')
        each_line_split.append(split)
        
    antigen_list = each_line_split[1:]
    
    for line in antigen_list:
        if (line[0]=='"""+"""' and line[-1] =='"""0"""'):
            del list[0]
             
        elif line[1]=='"""+"""' and line[3]=='"""0"""' and line[-1] =='"""0"""':
            del list[1]
             
        elif line[2]=='"""+"""' and line[4]=='"""0"""' and line[-1] =='"""0"""':
            del list[2]
             
        elif line[3]=='"""+"""' and line[1]=='"""0"""' and line[-1] =='"""0"""':
            del list[3]
             
        elif line[4]=='"""+"""' and line[2]=='"""0"""' and line[-1] =='"""0"""':
            del list[4]
             
        elif line[5]=='"""+"""' and line[-1] =='"""0"""':
            del list[5]
             
        
        elif line[6]=='"""+"""' and line[-1] =='"""0"""':
            del list[6]
             
        
        elif line[7]=='"""+"""' and line[-1] =='"""0"""':
            del list[7]
             
        
        elif line[8]=='"""+"""' and  line[9]=='"""0"""' and line[-1] =='"""0"""':
            del list[8]
             
        
        elif line[9]=='"""+"""' and  line[8]=='"""0"""' and line[-1] =='"""0"""':
            del list[9]
             
        
        elif line[10]=='"""+"""' and  line[11]=='"""0"""' and line[-1] =='"""0"""':
            del list[10]
             

        elif line[11]=='"""+"""' and  line[10]=='"""0"""' and line[-1] =='"""0"""':
            del list[11]
             
        
        elif line[13]=='"""+"""' and  line[12]=='"""0"""' and line[-1] =='"""0"""':
            del list[13]
        
        elif line[14]=='"""+"""' and  line[15]=='"""0"""' and line[-1] =='"""0"""':
            del list[14]
        elif line[15]=='"""+"""' and  line[14]=='"""0"""' and line[-1] =='"""0"""':
            del list[15]
             
        elif line[16]=='"""+"""' and  line[17]=='"""0"""' and line[-1] =='"""0"""':
            del list[16]
             
        elif line[17]=='"""+"""' and  line[16]=='"""0"""' and line[-1] =='"""0"""':
            del list[17]
             
        elif line[18]=='"""+"""' and line[-1] =='"""0"""':
            del list[18]
             
        elif line[19]=='"""+"""' and  line[20]=='"""0"""' and line[-1] =='"""0"""':
            del list[19]
             
        elif line[20]=='"""+"""' and  line[19]=='"""0"""' and line[-1] =='"""0"""':
            del list[20]
             
        elif line[21]=='"""+"""' and  line[22]=='"""0"""' and line[-1] =='"""0"""':
            del list[21]
             
        elif line[22]=='"""+"""' and  line[21]=='"""0"""' and line[-1] =='"""0"""':
            del list[22]
             
        elif line[23]=='"""+"""' and  line[24]=='"""0"""' and line[-1] =='"""0"""':
            del list[23]
             
        elif line[24]=='"""+"""' and  line[23]=='"""0"""' and line[-1] =='"""0"""':
            del list[24]
             
        elif line[25]=='"""+"""' and line[-1] =='"""0"""':
            del list[25]
             
        elif line[26]=='"""+"""' and  line[27]=='"""0"""' and line[-1] =='"""0"""':
            del list[26]
             
        elif line[27]=='"""+"""' and  line[26]=='"""0"""' and line[-1] =='"""0"""':
            del list[27]
             
        
    return list



print(ruleOut('Transfusion_medicine_panel_for_Joe__Doe_ID-123456_-_Sheet1.csv'))

