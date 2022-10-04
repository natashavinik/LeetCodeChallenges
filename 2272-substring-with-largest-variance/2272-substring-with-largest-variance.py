from collections import Counter
import itertools
class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        scount = Counter(s)
        n_lett = len(scount)
        if n_lett <= 1:
            return 0
        # print(scount)
        s_set = set(scount.values())
        # print(s_set)
        if s_set == set([1]):
            return 0
        s_let = scount.keys()
        # print(s_let)
        permutations = itertools.permutations(s_let, 2)
        count = 0
        for a, b in permutations:
            # print(a, b, count)
            if a == b:
                continue
            if scount[a] == 1 and scount[b] == 1:
                continue
            count = max(self.kadene(a, b, s, scount), count)
        return count
    
    def kadene(self, a, b, s, scount):
        max_local = 0
        current_sum = 0
        count_a = scount[a]
        count_b = scount[b]
        have_a = False
        have_b = False
        for x in s:
            # print(x, current_sum)
            if x!= a and x!= b:
                continue
            if current_sum < 0 and count_a != 0 and count_b != 0:
                current_sum = 0
                have_a = False
                have_b = False
            if x==a:
                current_sum += 1
                have_a = True
                count_a -= 1
            elif x==b:
                current_sum -= 1
                have_b = True
                count_b -= 1
            # print(current_sum)
            if have_a and have_b:
                max_local = max(max_local, current_sum)
        # if max_local == scount[a]:
        #     max_local -= 1
        return max_local

# 				# Keep track if c has become a or b
#         is_a = False
#         is_b = False

# 				# Keep track of characters for a and b
#         val_a = chars[a]
#         val_b = chars[b]
#         for c in s:
# 						# No need to continue if c is not a or b
#             if c != a and c != b:
#                 continue

# 						# Reset the max_local if there are no chars left or max_total
# 						# is negative
#             if max_local < 0 and val_a != 0 and val_b != 0:
#                 max_local = 0
#                 is_a = False
#                 is_b = False

# 						# Add 1 to the local max if c is the expected char
#             if c == a:
#                 max_local += 1
#                 val_a -= 1
#                 is_a = True
						
# 						# Remove 1 from the local max if c is the expected char
#             if c == b:
#                 max_local -= 1
#                 val_b -=1
#                 is_b = True
            
# 						# Only calculate the count if a and b apperared
#             if is_a and is_b:
#                 count = max(count, max_local)
#         return count
    
    
    
    
    
#         scount = Counter(s)
#         n_lett = len(scount)
#         if n_lett <= 1:
#             return 0
#         print(scount)
#         s_set = set(scount.values())
#         print(s_set)
#         if s_set == set([1]):
#             return 0
        
#         let_arr = scount.keys()
#         print(let_arr)
        
#         n_string = [1 if c == "a" else -1 for c in s]
#         m_string = [1 if c == "b" else -1 for c in s]
        
#         best_sum = 0
#         current_sum = 0
#         n_best = 0
        
#         for x in n_string:
#             print(x, current_sum, best_sum)
#             current_sum = max(0, current_sum + x)
#             best_sum = max(best_sum, current_sum)
        
#         n_best = max(best_sum, current_sum)  
        
#         best_sum = 0
#         current_sum = 0
        
#         for x in m_string:
#             print(x, current_sum, best_sum)
#             current_sum = max(0, current_sum + x)
#             best_sum = max(best_sum, current_sum)
        
#         m_best = max(best_sum, current_sum)
        
#         return max(n_best, m_best)