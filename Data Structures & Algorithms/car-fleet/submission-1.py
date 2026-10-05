class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make an array of tuples of (pos, speed) and sort by pos
        
        # example 1:
        # time = 0 -> pos[0] = 1, pos[1] = 4
        # time = 1 -> pos[0] = 4, pos[1] = 6
        # time = 2 -> pos[0] = 7, pos[1] = 8
        # time = 3 -> pos[0] = 10  pos[1] = 10


        # example 2 -> sort to [(0,1), (1,2), (4,2), (7,1)], target = 12
        # time = 0 -> pos[0]=0, pos[1]=1, pos[2]=4, pos[3]=7
        # time = 1 -> pos[0]=1, pos[1]=3, pos[2]=6, pos[3]=8
        # time = 2 -> pos[0]=2, pos[1]=5, pos[2]=8, pos[3]=9
        # time = 3 -> pos[0]=3, pos[1]=7, pos[2]=10, pos[3]=10
        # time = 4 -> pos[0]=4, pos[1]=9, pos[2]=11, pos[3]=11

        fleets = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True) #cars are sorted on position

        for pos, speed in cars:
            time = (target - pos) / speed
            if fleets and time <= fleets[-1]: # will join fleet at the top
                continue
            else:
                fleets.append(time)
        
        return len(fleets)

