def reverse_engine(list):
        revers_list = []
        for index in range(len(list)):
            n_index = (index + 1) * -1
            revers_list.append(list[n_index])
        return revers_list
    
    
    
arr = [1,2,3,4,5,6,7]

if __name__ == '__main__':
    print(reverse_engine(arr))
    
    simulation = arr + reverse_engine(arr)
    
    print("Simulation:", simulation)
    print("Simulation 2:", [] + simulation)