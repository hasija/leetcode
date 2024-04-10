class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        arr = deque([i for i in range(len(deck))])
        ans = [0 for i in range(len(deck))]
        start = 0
        deck_ind = 0
        ans_ind = 0
        while len(arr)>0:
            ind = arr.popleft()
            if start%2==0:
                ans[ind] = deck[deck_ind]
                deck_ind+=1
            else:
                arr.append(ind)
            start+=1
        return ans
            
            
        
        