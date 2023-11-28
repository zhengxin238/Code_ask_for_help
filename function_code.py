from itertools import combinations
import pandas as pd


import prefLibParse
import networkx as nx

# pd.set_option('display.max_columns', None)

# =====================================================
# the input information

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
voters = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']

preferences_v1 = [candidates[0], candidates[1], candidates[2], candidates[3], candidates[4], candidates[5]]
preferences_v2 = [candidates[1], candidates[3], candidates[4], candidates[2], candidates[5], candidates[0]]
preferences_v3 = [candidates[5], candidates[4], candidates[1], candidates[0], candidates[3], candidates[2]]
preferences_v4 = [candidates[3], candidates[2], candidates[0], candidates[5], candidates[1], candidates[4]]
preferences_v5 = [candidates[2], candidates[0], candidates[5], candidates[4], candidates[3], candidates[1]]
preferences_v6 = [candidates[4], candidates[5], candidates[3], candidates[1], candidates[0], candidates[2]]

preference_in_table = [preferences_v1, preferences_v2, preferences_v3, preferences_v4, preferences_v5, preferences_v6]

friends_v1 = [voters[1], voters[4], voters[5]]
friends_v2 = [voters[0], voters[4], voters[5]]
friends_v3 = [voters[3], voters[4]]
friends_v4 = [voters[2]]
friends_v5 = [voters[0], voters[1], voters[2]]
friends_v6 = [voters[0], voters[1]]

friend_structure_list = [friends_v1, friends_v2, friends_v3, friends_v4, friends_v5, friends_v6]


# candidates = list(range(1, (
#         prefLibParse.getNumberOfAlternatives(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
# voters = list(
#     range(1, (prefLibParse.getNumberOfVoters(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
# preference_in_table = prefLibParse.getPreferenceList(r"https://www.preflib.org/static/data/agh/00009-00000001.soc")
#
# # =====================================================f1
#
# g = graphCode.getGraph(0.03, len(voters))
# friend_structure_list = graphCode.getFriendStructureList(g)
#
# # =====================================================f1
#
# scale_free_graph = nx.barabasi_albert_graph(len(voters), 2)
# friend_structure_list_scale_free = graphCode.getFriendStructureList(scale_free_graph)


# =====================================================f1

def borda_score_df_func(candidates, voters, preference):
    column_names = []
    index_names = []
    for c in candidates:
        column_names.append(c)
    for v in voters:
        index_names.append(v)
    print(column_names)
    print(index_names)
    borda_score_df = pd.DataFrame(columns=column_names, index=index_names)
    for candidate in candidates:
        n = 0
        for voter in voters:
            borda_score_df.at[voter, candidate] = len(candidates) - 1 - preference[n].index(candidate)
            n += 1
    return borda_score_df


# print("bordascore each voter for each candidaate")
#
borda_score_df = borda_score_df_func(candidates, voters, preference_in_table)
print(borda_score_df)

















# from itertools import combinations
# import pandas as pd
#
#
# # pd.set_option('display.max_columns', None)
#
# # =====================================================
# # the input information
#
# candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
# voters = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']
#
# preferences_v1 = [candidates[0], candidates[1], candidates[2], candidates[3], candidates[4], candidates[5]]
# preferences_v2 = [candidates[1], candidates[3], candidates[4], candidates[2], candidates[5], candidates[0]]
# preferences_v3 = [candidates[5], candidates[4], candidates[1], candidates[0], candidates[3], candidates[2]]
# preferences_v4 = [candidates[3], candidates[2], candidates[0], candidates[5], candidates[1], candidates[4]]
# preferences_v5 = [candidates[2], candidates[0], candidates[5], candidates[4], candidates[3], candidates[1]]
# preferences_v6 = [candidates[4], candidates[5], candidates[3], candidates[1], candidates[0], candidates[2]]
#
# preference_in_table = [preferences_v1, preferences_v2, preferences_v3, preferences_v4, preferences_v5, preferences_v6]
#
# friends_v1 = [voters[1], voters[4], voters[5]]
# friends_v2 = [voters[0], voters[4], voters[5]]
# friends_v3 = [voters[3], voters[4]]
# friends_v4 = [voters[2]]
# friends_v5 = [voters[0], voters[1], voters[2]]
# friends_v6 = [voters[0], voters[1]]
#
# friend_structure_list = [friends_v1, friends_v2, friends_v3, friends_v4, friends_v5, friends_v6]
#
# '''
# candidates = list(range(1, (
#         prefLibParse.getNumberOfAlternatives(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
# voters = list(
#     range(1, (prefLibParse.getNumberOfVoters(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
# preference_in_table = prefLibParse.getPreferenceList(r"https://www.preflib.org/static/data/agh/00009-00000001.soc")
# friend_structure_list = graphCode.getFriendStructureList(0.05, prefLibParse.getNumberOfVoters(
#     r"https://www.preflib.org/static/data/agh/00009-00000001.soc"))'''
#
#
# # =====================================================
#
# def borda_score_df_func(candidates, voters, preference):
#     column_names = []
#     index_names = []
#     for c in candidates:
#         column_names.append(c)
#     for v in voters:
#         index_names.append(v)
#     print(column_names)
#     print(index_names)
#     borda_score_df = pd.DataFrame(columns=column_names, index=index_names)
#     for candidate in candidates:
#         n = 0
#         for voter in voters:
#             borda_score_df.at[voter, candidate] = len(candidates) - 1 - preference[n].index(candidate)
#             n += 1
#     return borda_score_df
#
#
# print("bordascore each voter for each candidaate")
# print(borda_score_df_func(candidates, voters, preference_in_table))
#
#
# def committee_borda_score_df_func(voters, candidates, committee_size, preference):
#     column_names_bs = []
#     index_names_bs = []
#
#     for c in candidates:
#         column_names_bs.append(c)
#     for v in voters:
#         index_names_bs.append(v)
#     borda_score_df_1 = pd.DataFrame(columns=column_names_bs, index=index_names_bs)
#     for candidate_bs in candidates:
#         n = 0
#         for voter_bs in voters:
#             borda_score_df_1.at[voter_bs, candidate_bs] = len(candidates) - 1 - preference[n].index(candidate_bs)
#             n += 1
#
#     subsets_candidates = list(combinations(candidates, committee_size))
#     column_names = list(range(0, len(subsets_candidates)))
#     index_names = index_names_bs
#
#     committee_bordascore_df = pd.DataFrame(columns=column_names, index=index_names)
#     for voter in voters:
#         for i in range(0, len(subsets_candidates)):
#             score_temp = 0
#             for can in subsets_candidates[i]:
#                 score_temp += borda_score_df_1.at[voter, can]
#             committee_bordascore_df.at[voter, i] = score_temp
#     return committee_bordascore_df
#
#
# '''print("bordascore each voter for the final committee")
# print(committee_borda_score_df_func(voters, candidates, 3, preference_in_table))'''
#
#
# def committee_borda_score_df_strict_func(voters, candidates, committee_size, preference):
#     column_names_bs = []
#     index_names_bs = []
#
#     for c in candidates:
#         column_names_bs.append(c)
#     for v in voters:
#         index_names_bs.append(v)
#     borda_score_df_1 = pd.DataFrame(columns=column_names_bs, index=index_names_bs)
#     for candidate_bs in candidates:
#         n = 0
#         for voter_bs in voters:
#             borda_score_df_1.at[voter_bs, candidate_bs] = len(candidates) - 1 - preference[n].index(candidate_bs)
#             n += 1
#
#     subsets_candidates = list(combinations(candidates, committee_size))
#     column_names = list(range(0, len(subsets_candidates)))
#     index_names = index_names_bs
#
#     committee_bordascore_df = pd.DataFrame(columns=column_names, index=index_names)
#     for voter in voters:
#         for i in range(0, len(subsets_candidates)):
#             score_temp = 0
#             for can in subsets_candidates[i]:
#                 if borda_score_df_1.at[voter, can] >= (len(candidates) - committee_size):
#                     score_temp += borda_score_df_1.at[voter, can]
#             committee_bordascore_df.at[voter, i] = score_temp
#     return committee_bordascore_df
#
#
# '''print("bordascore each voter for the final committee strict")
# print(committee_borda_score_df_strict_func(voters, candidates, 3, preference_in_table))'''
#
#
# def AvgFSI_df_func(voters, candidates, committee_size, preference, friend_structure):
#     column_names_bs = []
#     index_names_bs = []
#
#     for c in candidates:
#         column_names_bs.append(c)
#     for v in voters:
#         index_names_bs.append(v)
#     borda_score_df_1 = pd.DataFrame(columns=column_names_bs, index=index_names_bs)
#     for candidate_bs in candidates:
#         n = 0
#         for voter_bs in voters:
#             borda_score_df_1.at[voter_bs, candidate_bs] = len(candidates) - 1 - preference[n].index(candidate_bs)
#             n += 1
#
#     subsets_candidates = list(combinations(candidates, committee_size))
#     column_names = list(range(0, len(subsets_candidates)))
#     index_names = index_names_bs
#
#     committee_bordascore_df = pd.DataFrame(columns=column_names, index=index_names)
#     for voter in voters:
#         for i in range(0, len(subsets_candidates)):
#             score_temp = 0
#             for can in subsets_candidates[i]:
#                 if borda_score_df_1.at[voter, can] >= (len(candidates) - committee_size):
#                     score_temp += borda_score_df_1.at[voter, can]
#             committee_bordascore_df.at[voter, i] = score_temp
#
#     avg_fsi_df_1 = pd.DataFrame(columns=column_names, index=index_names)
#     for i in range(0, len(subsets_candidates)):
#         m = 0
#         for friends in friend_structure:
#             temp = 0
#             for friend in friends:
#                 temp += committee_bordascore_df.at[friend, i]
#             if len(friends) != 0:
#                 avg_fsi_df_1.at[voters[m], i] = temp / len(friends)
#             else:
#                 avg_fsi_df_1.at[voters[m], i] = 3
#             m += 1
#
#     return avg_fsi_df_1
#
#
# '''print(AvgFSI_df_func(voters, candidates, 3, preference_in_table, friend_structure_list))'''
#
#
# def MinFSI_df_func(voters, candidates, committee_size, preference, friend_structure):
#     column_names_bs = []
#     index_names_bs = []
#
#     for c in candidates:
#         column_names_bs.append(c)
#     for v in voters:
#         index_names_bs.append(v)
#     borda_score_df_1 = pd.DataFrame(columns=column_names_bs, index=index_names_bs)
#     for candidate_bs in candidates:
#         n = 0
#         for voter_bs in voters:
#             borda_score_df_1.at[voter_bs, candidate_bs] = len(candidates) - 1 - preference[n].index(candidate_bs)
#             n += 1
#
#     subsets_candidates = list(combinations(candidates, committee_size))
#     column_names = list(range(0, len(subsets_candidates)))
#     index_names = index_names_bs
#
#     committee_bordascore_df = pd.DataFrame(columns=column_names, index=index_names)
#     for voter in voters:
#         for i in range(0, len(subsets_candidates)):
#             score_temp = 0
#             for can in subsets_candidates[i]:
#                 if borda_score_df_1.at[voter, can] >= (len(candidates) - committee_size):
#                     score_temp += borda_score_df_1.at[voter, can]
#             committee_bordascore_df.at[voter, i] = score_temp
#
#     min_fsi_df_1 = pd.DataFrame(columns=column_names, index=index_names)
#     for i in range(0, len(subsets_candidates)):
#         m = 0
#         for friends in friend_structure:
#             temp = None
#             for friend in friends:
#                 if (temp == None) or (temp >= committee_bordascore_df.at[friend, i]):
#                     temp = committee_bordascore_df.at[friend, i]
#             min_fsi_df_1.at[voters[m], i] = temp
#             m += 1
#     return min_fsi_df_1
#
#
# '''print(MinFSI_df_func(voters, candidates, 3, preference_in_table, friend_structure_list))'''
#
#
# def MaxFSI_df_func(voters, candidates, committee_size, preference, friend_structure):
#     column_names_bs = []
#     index_names_bs = []
#
#     for c in candidates:
#         column_names_bs.append(c)
#     for v in voters:
#         index_names_bs.append(v)
#     borda_score_df_1 = pd.DataFrame(columns=column_names_bs, index=index_names_bs)
#     for candidate_bs in candidates:
#         n = 0
#         for voter_bs in voters:
#             borda_score_df_1.at[voter_bs, candidate_bs] = len(candidates) - 1 - preference[n].index(candidate_bs)
#             n += 1
#
#     subsets_candidates = list(combinations(candidates, committee_size))
#     column_names = list(range(0, len(subsets_candidates)))
#     index_names = index_names_bs
#
#     committee_bordascore_df = pd.DataFrame(columns=column_names, index=index_names)
#     for voter in voters:
#         for i in range(0, len(subsets_candidates)):
#             score_temp = 0
#             for can in subsets_candidates[i]:
#                 if borda_score_df_1.at[voter, can] >= (len(candidates) - committee_size):
#                     score_temp += borda_score_df_1.at[voter, can]
#             committee_bordascore_df.at[voter, i] = score_temp
#
#     max_fsi_df_1 = pd.DataFrame(columns=column_names, index=index_names)
#     for i in range(0, len(subsets_candidates)):
#         m = 0
#         for friends in friend_structure:
#             temp = None
#             for friend in friends:
#                 if (temp == None) or (temp <= committee_bordascore_df.at[friend, i]):
#                     temp = committee_bordascore_df.at[friend, i]
#             max_fsi_df_1.at[voters[m], i] = temp
#             m += 1
#     return max_fsi_df_1
#
# '''
# print(MaxFSI_df_func(voters, candidates, 3, preference_in_table, friend_structure_list))
# '''
#
# def AllFSI_df_func(voters, candidates, committee_size, preference, friend_structure):
#     column_names_bs = []
#     index_names_bs = []
#
#     for c in candidates:
#         column_names_bs.append(c)
#     for v in voters:
#         index_names_bs.append(v)
#     borda_score_df_1 = pd.DataFrame(columns=column_names_bs, index=index_names_bs)
#     for candidate_bs in candidates:
#         n = 0
#         for voter_bs in voters:
#             borda_score_df_1.at[voter_bs, candidate_bs] = len(candidates) - 1 - preference[n].index(candidate_bs)
#             n += 1
#
#     subsets_candidates = list(combinations(candidates, committee_size))
#     for i in range(0,len(subsets_candidates)):
#         print(i)
#         print(subsets_candidates[i])
#     column_names = list(range(0, len(subsets_candidates)))
#     index_names = index_names_bs
#
#     committee_bordascore_df = pd.DataFrame(columns=column_names, index=index_names)
#     for voter in voters:
#         for i in range(0, len(subsets_candidates)):
#             score_temp = 0
#             for can in subsets_candidates[i]:
#                   if borda_score_df_1.at[voter, can] >= (len(candidates) - committee_size):
#                     score_temp += borda_score_df_1.at[voter, can]
#             committee_bordascore_df.at[voter, i] = score_temp
#
#     avg_fsi_df_1 = pd.DataFrame(columns=column_names, index=index_names)
#     for a in range(0, len(subsets_candidates)):
#         b = 0
#         for friends in friend_structure:
#             temp = 0
#             for friend in friends:
#                 temp += committee_bordascore_df.at[friend, a]
#             avg_fsi_df_1.at[voters[b], a] = temp / len(friends)
#             b += 1
#
#     min_fsi_df_1 = pd.DataFrame(columns=column_names, index=index_names)
#     for j in range(0, len(subsets_candidates)):
#         k = 0
#         for friends in friend_structure:
#             temp = None
#             for friend in friends:
#                 if (temp == None) or (temp >= committee_bordascore_df.at[friend, j]):
#                     temp = committee_bordascore_df.at[friend, j]
#             min_fsi_df_1.at[voters[k], j] = temp
#             k += 1
#
#     max_fsi_df_1 = pd.DataFrame(columns=column_names, index=index_names)
#     for i in range(0, len(subsets_candidates)):
#         m = 0
#         for friends in friend_structure:
#             temp = None
#             for friend in friends:
#                 if (temp == None) or (temp <= committee_bordascore_df.at[friend, i]):
#                     temp = committee_bordascore_df.at[friend, i]
#             max_fsi_df_1.at[voters[m], i] = temp
#             m += 1
#
#     result_df = pd.DataFrame()
#
#     avg_avg = avg_fsi_df_1.mean()
#     min_avg = min_fsi_df_1.mean()
#     max_avg = max_fsi_df_1.mean()
#
#     avg_min = avg_fsi_df_1.min()
#     min_min = min_fsi_df_1.min()
#     max_min = max_fsi_df_1.min()
#
#     avg_max = avg_fsi_df_1.max()
#     min_max = min_fsi_df_1.max()
#     max_max = max_fsi_df_1.max()
#
#     result_df = result_df._append(avg_avg, ignore_index=True)._append(min_avg, ignore_index=True)._append(max_avg,
#                                                                                                           ignore_index=True)._append(
#         avg_min, ignore_index=True)._append(min_min, ignore_index=True)._append(max_min,
#                                                                                 ignore_index=True)._append(avg_max,
#                                                                                                            ignore_index=True)._append(
#         min_max, ignore_index=True)._append(max_max,
#                                             ignore_index=True)
#
#
#     result_df['Max'] = result_df.apply(max, axis=1)
#
#     max_location = result_df.idxmax(axis=1)
#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.max_columns', None)
#     print(result_df)
#
#     return max_location
#
#
# print(AllFSI_df_func(voters, candidates, 3, preference_in_table, friend_structure_list))
