class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        dp = {}
        dp_cut = {}

        def check_apple(arr, points):
            if points in dp_cut:
                return dp_cut[points]
            for r in range(len(arr)):
                for c in range(len(arr[0])):
                    if arr[r][c]=='A':
                        dp_cut[points]=True
                        return True
            dp_cut[points]=False
            return False
        
        def recurse(arr, points, cuts):
            if cuts==0:
                if check_apple(arr, points):
                    return 1
                else:
                    return 0
            # ADD MEMO
            if (points,cuts) in dp:
                return dp[(points,cuts)]
            # CUTS
            count = 0
            # print ("standing", points)
            cut_arr = []
            for ver_cut in range(1, len(arr[0])):
                left_arr = [x[:ver_cut] for x in arr]
                left_points = (points[0], points[1], points[2], points[2]+ver_cut-1)
                right_arr = [x[ver_cut:] for x in arr]
                right_points = (points[0], points[1], points[2]+ver_cut, points[3])
                if (check_apple(left_arr, left_points)):
                    prev = recurse(right_arr, right_points, cuts-1)
                    count+=prev
                cut_arr.append(left_arr)
                cut_arr.append(right_arr)

                
            for hori_cut in range(1, len(arr)):
                left_arr = arr[:hori_cut]
                left_points = (points[0], points[0]+hori_cut-1, points[2], points[3])
                right_arr = arr[hori_cut:]
                right_points = (points[0]+hori_cut, points[1], points[2], points[3])
                if (check_apple(left_arr, left_points)):
                    prev = recurse(right_arr, right_points, cuts-1)
                    count+=prev
            dp[(points,cuts)]=count
            
            # print ("Starting", points)
            # print_cut(cut_arr)
            # print ("end", points)

            # print ("FINAL POINTS", count)
            return count

        sr=0
        er=len(pizza)-1
        sc=0
        ec=len(pizza[0])-1
        points=(sr, er, sc, ec)

        out = recurse(pizza, points, k-1)
        # print (dp)
        return out%( 10**9 + 7)
