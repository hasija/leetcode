class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)
        
        skill_dict = {req_skills[i]:i for i in range(m)}
        dp = collections.defaultdict(list)
        dp[0]=[]

        for i in range(n):
            # Iterating on all people and populating skill_found + prev_matched skills
            # print ("iterating", i)
            curr = 0
            for skill in people[i]:
                curr |= 1<<skill_dict[skill]
            
            if curr not in dp or len(dp[curr])>1:
                dp[curr] = [i]
            for prev_found, pep_found in dict(dp).items():
                new_skill = prev_found|curr
                # if prev_found==new_skill:
                #     continue
                if not dp[new_skill] or len(dp[new_skill])>len(pep_found)+1:
                    dp[new_skill] = pep_found+[i]
        
        req_skill_mask = 0
        for i in req_skills:
            req_skill_mask |= 1<<skill_dict[i]
        # print (dp)
        return dp[(1 << m) - 1]