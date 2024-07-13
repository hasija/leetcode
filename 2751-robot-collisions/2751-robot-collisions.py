class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robot_posi_health = list(zip(list(range(n)),positions,healths,directions))
        sorted_run = sorted(robot_posi_health, key = lambda x: x[1])
        stack = []
        for idx, posi, health, dire in sorted_run:
            if not stack:
                stack.append((idx, posi, health, dire))
                continue
            if dire == stack[-1][3] or (stack[-1][3]=='L' and dire=='R'):
                stack.append((idx, posi, health, dire))
            else:
                
                while stack and stack[-1][3]=='R' and dire=='L':
                    arr = stack.pop()
                    if arr[2] == health:
                        health=0
                        break
                    elif arr[2]<health:
                        health-=1
                    else:
                        stack.append((arr[0],arr[1],arr[2]-1,arr[3]))
                        health = 0
                        break
                # print ("Collision happened", 'and stack', stack, health)

                if health>0:
                    stack.append((idx, posi, health, dire))
        final = sorted(stack, key = lambda x: x[0])
        return [i[2] for i in final]