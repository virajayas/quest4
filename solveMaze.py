import queue

"""
this program assumes that the data given is proper and works
it also assumes each lines has the same number of items as the others
start--"S"
finish--"F"
walls--"#"
open_space--"."
already visited--"0"
"""
def get_nexts(map, i, j):
    vertical_length=len(map)
    horizontal_length=len(map[0])
    out=[]
    #if there exists a next where it is a finish, only return that
    #left item
    if(i-1<=0):
        if(map[i-1][j])==".":#checks if that point is movable into
            out.append([i-1, j])
    #right item
    if(i+1<horizontal_length):
        if(map[i+1][j])==".":  # checks if that point is movable into
            out.append([i+1, j])
    #top item
    if(j>=0):
        if(map[i][j-1])==".":  # checks if that point is movable into
            out.append([i, j-1])
    #bottom item
    if(j<vertical_length):
        if (map[i][j+1])==".":  # checks if that point is movable into
            out.append([i, j+1])
    return out

def get_shortest_path(file_name):
    #put all the values in the file into an array
    string=file_name.read().strip()
    array_map=[[]]
    line_counter=0
    start_i=None
    start_j=None

    for i in range(len(string)):
        #ignore everything that isnt a hash or a dot but take into account the new line
        if(string[i]!="#" and string[i]!="."):
            if(string[i]=="\n"):
                line_counter+=1
                array_map.append([])
        else:
            array_map[line_counter].append(string[i])
        # check if the value is the start node
        if (string[i] == "S"):
            start_i = line_counter
            start_j = (i-line_counter)#takes the "\n" count off
    start_j=start_j%len(array_map[0])#divide the number by the amount of items in one row

    #use Breadth-First Search technique to find the finish point, using python's implementation of queue
    i=start_i
    j=start_j
    while(1):
        pass


class Node:
    def __init__(self, val, next):
        self.val=val
        self.next=next

if __name__=="__main__":
    filename="supps/t1/"+str(input("Enter the maze file: "))
    try:
        fid=open(filename, "r")
    except:
        try:
            filename+=".txt"
            fid=open(filename, "r")
        except:
            raise FileNotFoundError("The name of the file you entered does not exist!!!")
    get_shortest_path(fid)