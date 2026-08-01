# from collections import defaultdict

# class Solution(object):
#     def longestCommonPrefix(self, strs) :
#         prefix = ""
#         # (index, count)
#         prefix_dict = defaultdict(lambda: tuple()) # (index, count)

#         for string in strs:
#             seen = set()
#             for idx, s in enumerate(string):
#                 cur_value = prefix_dict.get(s)
#                 if cur_value and s not in seen:
#                     prefix_dict[s] = (idx, cur_value[1] + 1)
#                 else:
#                     prefix_dict[s] = (idx, 1)
#                 seen.add(s)

#         prefix_dict = dict(sorted(prefix_dict.items(), key=lambda x: x[1][0]))
#         print(prefix_dict)
#         prev_idx = None
#         for key, value in prefix_dict.items():
#             print(prev_idx)
#             if value[1] == len(strs):
#                 if prev_idx is None:
#                     prefix += key
#                 elif prev_idx + 1 == value[0]:
#                     prefix += key
#                 prev_idx = value[0]

#         return prefix 
  
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix
       

