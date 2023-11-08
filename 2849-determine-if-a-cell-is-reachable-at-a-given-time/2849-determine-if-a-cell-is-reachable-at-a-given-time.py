class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist_x = abs(fx-sx)
        dist_y = abs(fy-sy)
        total_d = dist_x+dist_y
        if total_d == 0:
            return True if t!=1 else False
        rem_moves = abs(dist_x-dist_y)
        total_moves = min(dist_x, dist_y)+rem_moves
        # print (total_moves)
        return True if total_moves<=t else False