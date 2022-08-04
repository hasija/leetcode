class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        walls = p
        curr = 3
        right = True
        top = True
        prev_dist_side = 0
        prev_dist_td = 0
        while True:
            if prev_dist_side+q==p:
                if right and top:
                    return 1
                if not right and top:
                    return 2
                else:
                    return 0
                prev_dist_side = 0
                right = not right
                top = not top
            elif prev_dist_side+q<p:
                prev_dist_side +=q
                right = not right
                
            elif prev_dist_side+q>p:

                prev_dist_side = p-prev_dist_side
                prev_dist_side = -prev_dist_side
                # prev_dist_side = q-dist_to_travel
                top = not top
                right = not right
            # print (prev_dist_side, top, right)



# class Solution:
#     def mirrorReflection(self, p: int, q: int) -> int:
#         if p == q:
#             return 1
        
#         height = q
#         right, up = False, True
#         while 1:
#             if height + q == p:
#                 if right and up:
#                     return 1
#                 elif not right and up:
#                     return 2
#                 else:
#                     return 0
#             elif height + q < p:
#                 height += q
#                 right = not right
#             else:
#                 height += q
#                 height %= p
#                 right = not right
#                 up = not up