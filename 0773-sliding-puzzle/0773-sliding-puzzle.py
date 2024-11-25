class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        direction_map = [
            [1,3],
            [0,2,4],
            [1,5],
            [0,4],
            [1,3,5],
            [2,4]
        ]
        final_state = "123450"        
        queue = deque()
        start = ''.join([''.join(map(str,row)) for row in board])
        visited = set()
        visited.add(start)
        queue.append(start)
        if start == final_state:
            return 0
        
        def swap_idx(state, idx1, idx2):
            new_state = state
            min_idx = min(idx1, idx2)
            max_idx = max(idx1, idx2)
            # print("swap", state, idx1, idx2)
            new_state = state[:min_idx]+state[max_idx]+state[min_idx+1:max_idx]+state[min_idx]+state[max_idx+1:]
            # print("final", new_state)
            return new_state
        
        ans = 0


        while True:
            new_queue = deque()
            while queue:
                curr_state = queue.popleft()
                curr_idx = curr_state.index('0')
                # print(curr_state)
                for move in direction_map[curr_idx]:
                    new_state = swap_idx(curr_state, curr_idx, move)
                    if new_state not in visited:
                        if new_state == final_state:
                            return ans+1
                        visited.add(new_state)
                        new_queue.append(new_state)

            if new_queue:
                ans+=1
                queue = new_queue
            else:
                break
        return -1 