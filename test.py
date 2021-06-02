import numpy as np

def get_num(num):
    epic_list = []
    for i in range(1, int(np.ceil(np.sqrt(num)))):
        for j in range(1, int(np.ceil(np.sqrt(num)))):
            if i**2 + j**2 == num:
                 epic_list.append([i,j])
                 
    return epic_list
                 
def generate_pairs(min_num,max_num, list_len):
    epic_list = []
    for i in range(min_num,max_num,2):
        num_list = get_num(i)
        if len(num_list) > list_len:
            epic_list.append([i,num_list])
            
    return epic_list
            
            