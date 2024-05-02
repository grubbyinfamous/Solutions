'''
Final Exam Review
'''

def reversingArrays():
    song_array = ['Red', '99', 'Balloons']
    song_array.reverse()
    
    print(song_array)
    
    empty_list = []
    song_array.reverse()
    
    for elem in song_array:
        empty_list.append(elem)
        
    print(empty_list)
    

def determineCharInList():
    song_Array = ["Red", "99", "Balloons"]
    
    for elem in song_Array:
        if elem.isdigit():
            print(f"index location {song_Array.index(elem)} is an integer")
    

if __name__ == '__main__':
    reversingArrays()
    determineCharInList()