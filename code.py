from itertools import combinations

import pandas as pd

from preflibtools.instances import PrefLibInstance

# pd.set_option('display.max_columns', None)

# =====================================================
# the input information

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
voters = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']

outcome_committee = [candidates[0], candidates[1], candidates[5]]

preferences_v1 = [candidates[0], candidates[1], candidates[2], candidates[3], candidates[4], candidates[5]]
preferences_v2 = [candidates[1], candidates[3], candidates[4], candidates[2], candidates[5], candidates[0]]
preferences_v3 = [candidates[5], candidates[4], candidates[1], candidates[0], candidates[3], candidates[2]]
preferences_v4 = [candidates[3], candidates[2], candidates[0], candidates[5], candidates[1], candidates[4]]
preferences_v5 = [candidates[2], candidates[0], candidates[5], candidates[4], candidates[3], candidates[1]]
preferences_v6 = [candidates[4], candidates[5], candidates[3], candidates[1], candidates[0], candidates[2]]

preference_in_table = [preferences_v1, preferences_v2, preferences_v3, preferences_v4, preferences_v5, preferences_v6]

friends_v1 = [voters[1], voters[3], voters[4], voters[5]]
friends_v2 = [voters[0], voters[4], voters[5]]
friends_v3 = [voters[3], voters[4]]
friends_v4 = [voters[0], voters[2]]
friends_v5 = [voters[0], voters[1], voters[2]]
friends_v6 = [voters[0], voters[1]]

friend_structure_list = [friends_v1, friends_v2, friends_v3, friends_v4, friends_v5, friends_v6]
# =====================================================
# voter-candidate borda score dataframe
borda_score_df = pd.DataFrame(
    columns=[candidates[0], candidates[1], candidates[2], candidates[3], candidates[4], candidates[5]],
    index=[voters[0], voters[1], voters[2], voters[3], voters[4], voters[5]])
for candidate in candidates:
    n = 0
    for voter in voters:
        preferences_index = 'preferences_' + voter
        borda_score_df.at[voter, candidate] = len(candidates) - 1 - preference_in_table[n].index(candidate)
        n += 1
print(borda_score_df)
# =====================================================
# voter-committee borda score dataframe
subsets = list(combinations(candidates, 3))
column_names = list(range(0, len(subsets)))
committee_borda_score_df = pd.DataFrame(columns=column_names,
                                        index=[voters[0], voters[1], voters[2], voters[3], voters[4], voters[5]])
for voter in voters:
    for i in range(0, len(subsets)):
        committee_borda_score_temp = 0
        for candidate in subsets[i]:
            committee_borda_score_temp += borda_score_df.at[voter, candidate]
        committee_borda_score_df.at[voter, i] = committee_borda_score_temp

print(committee_borda_score_df)

# =====================================================
# consider only the top x candidates
committee_borda_score_df_strict = pd.DataFrame(columns=column_names,
                                               index=[voters[0], voters[1], voters[2], voters[3], voters[4], voters[5]])
for voter in voters:
    for i in range(0, len(subsets)):
        committee_borda_score_temp = 0
        for candidate in subsets[i]:
            if borda_score_df.at[voter, candidate] >= 3:
                committee_borda_score_temp += borda_score_df.at[voter, candidate]
        committee_borda_score_df_strict.at[voter, i] = committee_borda_score_temp
print(committee_borda_score_df_strict)

# =====================================================
# consider the friend structure (AvgFSI of each voter for each committee)
AvgFSI_df = pd.DataFrame(columns=column_names,
                         index=[voters[0], voters[1], voters[2], voters[3], voters[4], voters[5]])

for i in range(0, len(subsets)):
    m = 0
    for friends in friend_structure_list:
        temp = 0
        for friend in friends:
            temp += committee_borda_score_df.at[friend, i]
        AvgFSI_df.at[voters[m], i] = temp / len(friends)
        m += 1

print(AvgFSI_df)

# =====================================================
# consider the friend structure (MinFSI of each voter for each committee)
MinFSI_df = pd.DataFrame(columns=column_names,
                         index=[voters[0], voters[1], voters[2], voters[3], voters[4], voters[5]])

for i in range(0, len(subsets)):
    m = 0
    for friends in friend_structure_list:
        temp = None
        for friend in friends:
            if (temp == None) or (temp >= committee_borda_score_df.at[friend, i]):
                temp = committee_borda_score_df.at[friend, i]
        MinFSI_df.at[voters[m], i] = temp
        m += 1

print(MinFSI_df)

# =====================================================
# consider the friend structure (MaxFSI of each voter for each committee)
MaxFSI_df = pd.DataFrame(columns=column_names,
                         index=[voters[0], voters[1], voters[2], voters[3], voters[4], voters[5]])

for i in range(0, len(subsets)):
    m = 0
    for friends in friend_structure_list:
        temp = None
        for friend in friends:
            if (temp == None) or (temp <= committee_borda_score_df.at[friend, i]):
                temp = committee_borda_score_df.at[friend, i]
        MaxFSI_df.at[voters[m], i] = temp
        m += 1

print(MaxFSI_df)

# =====================================================
# the result df
result_avg_df = pd.DataFrame()

avg_avg = AvgFSI_df.mean()
min_avg = MinFSI_df.mean()
max_avg = MaxFSI_df.mean()

result_avg_df = result_avg_df._append(avg_avg, ignore_index=True)._append(min_avg, ignore_index=True)._append(max_avg,
                                                                                                              ignore_index=True)
result_avg_df['Min'] = result_avg_df.apply(min, axis=1)
result_avg_df['Max'] = result_avg_df.apply(max, axis=1)
result_min_df = pd.DataFrame()

avg_min = AvgFSI_df.min()
min_min = MinFSI_df.min()
max_min = MaxFSI_df.min()

result_min_df = result_min_df._append(avg_min, ignore_index=True)._append(min_min, ignore_index=True)._append(max_min,
                                                                                                              ignore_index=True)
result_min_df['Min'] = result_min_df.apply(min, axis=1)
result_min_df['Max'] = result_min_df.apply(max, axis=1)

result_max_df = pd.DataFrame()

avg_max = AvgFSI_df.max()
min_max = MinFSI_df.max()
max_max = MaxFSI_df.max()

result_max_df = result_max_df._append(avg_max, ignore_index=True)._append(min_max, ignore_index=True)._append(max_max,
                                                                                                              ignore_index=True)
result_max_df['Min'] = result_max_df.apply(min, axis=1)
result_max_df['Max'] = result_max_df.apply(max, axis=1)

print(result_avg_df)
print(result_min_df)
print(result_max_df)

# =====================================================
