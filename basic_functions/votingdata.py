from dataclasses import dataclass
import prefLibParse


@dataclass
class votingdata:
    candidates: []
    voters: []
    preference_in_table: []
    friend_structure_list: []
    committee_size: int



