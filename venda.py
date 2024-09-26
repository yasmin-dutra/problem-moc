class BagObject:
    def __init__(self, price, weight, ratio):
        self.price = price
        self.weight = weight
        self.ratio = ratio

def get_max(list_bag_objects_ord, m, i):
    
    obj = list_bag_objects_ord[i-1]
    
    if i == 0 or m == 0:
        return 0
    if obj.weight > m:
        return get_max(list_bag_objects_ord,m,i-1)
    else:
        return max(obj.price+get_max(list_bag_objects_ord,m-obj.weight,i-1),get_max(list_bag_objects_ord,m,i-1))

ipt = []
n = 1

while(n != 0):

    n = int(input())

    if n != 0:
        
        sum_obj = 0
        sum_obj_aux = 0
        list_bag_objects = []
        list_bag_objects_ord =[]
        aux_list = []

        for i in range(n):
            ipt = input()
            ipt = ipt.split(' ')
            object_price = float(ipt[0])
            object_weight = float(ipt[1])
            object_ratio = (object_price / object_weight)
            bag_object = BagObject(object_price,object_weight,object_ratio)
            list_bag_objects.append(bag_object)

        m = int(input())
        list_bag_objects_ord = sorted(list_bag_objects, key = lambda x: x.ratio, reverse=True)
        
        sum_obj = get_max(list_bag_objects, m, n)

        print(int(sum_obj))