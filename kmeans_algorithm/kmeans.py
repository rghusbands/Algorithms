import math

#returns distance between two points
def distance(c, p):
    return ((c[0]-p[0])**2+(c[1]-p[1])**2)**.5

def kmeans(centers, data):
    groups = {}
    i=0
    for c in centers:
        name = i
        i+=1
        groups[name] = []
    #print(groups)
    for point in data:
        #print('point ' + point)
        min_dist = math.inf
        j=0
        final = 0
        for c in centers:
            #print('center ' + str(c))
            dist = distance(c, data[point])
            if (min_dist > dist):
                min_dist = dist
                final = j
                #print(final)
            j+=1
        groups[final].append(point)
        
    #print(groups)
    center_change = 0
    for center_num in groups:
        point_num = 0
        x_sum = 0
        y_sum = 0
        for points in groups[center_num]:
            x_sum += data[points][0]
            y_sum += data[points][1]
            point_num += 1
        new_center_x = x_sum/point_num
        new_center_y = y_sum/point_num
        new_center = [new_center_x, new_center_y]
        if (centers[center_num][0] == new_center[0] or
            centers[center_num][1] == new_center[1]):
            center_change += 1
        centers[center_num] = new_center
    print(centers)
    #print(center_change)
    if (center_change == 3):
        print("Terminate")
        return
    kmeans(centers, data)


def main():
    data_points = {'A1':[3,10],'A2':[4,6],'A3':[9,5],
                   'B1':[3,8],'B2':[8,5],'B3':[6,6],
                   'C1':[2,3],'C2':[5,7],'C3':[6,8]}
    centers = [[3,10],[3,8],[2,3]]

    kmeans(centers, data_points)

main()
