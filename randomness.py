# True Random Process vs Pseudorandom process
# The surprising complexity of randomness

r = []

def pseudorandom(seed):
    remainder = (387*seed + 217)%953
    print('Remainder is:', remainder)
    return remainder
    
def generate_random_sequence(seed):
    try:
        if seed == 0:
            print('Please enter non-null seed!!')
        else:
            while True:
                remainder = pseudorandom(seed) 
                r.append(remainder)
                seed = remainder
                if remainder == 0:
                    print('remainder is 0!!')

    except:
        print('something went wrong!!')


        
#call generate_random_sequence function
generate_random_sequence(43)
        
#Results: Pseudo 'random sequence' is repeating after every 952 numbers
for i in range(len(r)):
    if r[i] == 657:
        print(i)
