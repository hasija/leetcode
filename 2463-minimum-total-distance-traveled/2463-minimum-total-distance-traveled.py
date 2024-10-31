class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory_idx = []
        for k,v in factory:
            factory_idx+=[k]*v
        factory_idx.sort()
        # print (robot, factory_idx)
        ROBOTS = len(robot)
        TOTAL_FACTORIES = len(factory_idx)
        memo = [[None]*TOTAL_FACTORIES for i in range(ROBOTS)]

        def dp(robot_idx, factory_to_check):
            if robot_idx==ROBOTS:
                return 0
            # print ("i,j,dist", robot_idx, factory_to_check)
            if factory_to_check==TOTAL_FACTORIES:
                return float('inf')
            if memo[robot_idx][factory_to_check] is not None:
                return memo[robot_idx][factory_to_check]
            dist = abs(factory_idx[factory_to_check]-robot[robot_idx])
            nxt_dist = dp(robot_idx+1, factory_to_check+1)
            # print ("i,j,dist", robot_idx, factory_to_check, dist)
            no_skip_case = dist+nxt_dist # check if current one is the closest
            
            # check for the next factory _idx
            skip_case = dp(robot_idx, factory_to_check+1)
            ans = min(no_skip_case, skip_case)
            memo[robot_idx][factory_to_check] = ans
            return ans
            
            
        return dp(0, 0)