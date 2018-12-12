def histogram(fdata, **kwargs):
    '''
        Plots the Histrogram for a given Frequency Distribution
        
        Parameters:
            * fdata: dict containing items as key and their frequency as value
            * kwargs: customizable parameters
                * design [default: ===] - design of the bar
                * label [default: True] - weather to show frequency after bar or not
                * align  [default:] - weather to align label or not
                    * not align will be False if label is False
                    
        >>> histogram({2: 6, 9: 4, 4: 1, 3: 1, 1: 2})
        2	|============ 6
        9	|======== 4
        4	|== 1
        3	|== 1
        1	|==== 2
        
        >>> histogram({2: 6, 9: 4, 4: 1, 3: 1, 1: 2}, label=False)
        2	|============ 
        9	|======== 
        4	|== 
        3	|== 
        1	|==== 
        
        >>> histogram({2: 6, 9: 4, 4: 1, 3: 1, 1: 2}, align=True)
        2	|============ 6
        9	|========     4
        4	|==           1
        3	|==           1
        1	|====         2

        >>> histogram({2: 6, 9: 4, 4: 1, 3: 1, 1: 2}, align=True, design='::::')
        2	|:::::::::::::::::::::::: 6
        9	|::::::::::::::::         4
        4	|::::                     1
        3	|::::                     1
        1	|::::::::                 2
    '''
    
    design=kwargs.get('design','==')    
    label=kwargs.get('label',True) 
    
    align=kwargs.get('align',False) if label else False

    hi=max(fdata.values())*len(design) if align else None
    
    
    for key,value in fdata.items():
        lbl = value if label else ''        
        bar= (design  * value)
        if hi!=None :
            bar=bar.ljust(hi)
        
        print('{}\t|{} {}'.format(key,bar,lbl))

def freq(* args):
    '''
    Calculate frequency distribution for provides set of values
    returning result as dictionary
    '''
    
    result=dict()
    
    for value in args: # each item
        result[value]= result.get(value,0)+1
    
    return result