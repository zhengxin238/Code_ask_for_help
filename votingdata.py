from dataclasses import dataclass
import prefLibParse
import graphCode_Coefficient_AvgAvg


@dataclass
class votingdata:
    candidates: []
    voters: []
    preference_in_table: []
    friend_structure_list: []
    committee_size: int


preflib_parse = prefLibParse
graph_code = graphCode

candidates = list(range(1, (
        preflib_parse.getNumberOfAlternatives(r"https://www.preflib.org/static/data/agh/00009-00000002.soc") + 1)))
voters = list(
    range(1, (preflib_parse.getNumberOfVoters(r"https://www.preflib.org/static/data/agh/00009-00000002.soc") + 1)))
preference_in_table = preflib_parse.getPreferenceList(r"https://www.preflib.org/static/data/agh/00009-00000002.soc")
"""friend_structure_list = graphCode.getFriendStructureList(0.03, preflib_parse.getNumberOfVoters(
    r"https://www.preflib.org/static/data/agh/00009-00000002.soc"))"""
