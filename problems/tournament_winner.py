from typing import Dict, List


def add_result_to_winner_dict(
    winner_dict: Dict,
    team: str
):
    if team not in winner_dict:
        winner_dict[team] = 0

    winner_dict[team] += 1


def tournamentWinner(
    competitions: List[str],
    results: List[int],
) -> str:
    winner_dict = {}
    
    for idx in range(len(results)):
        if results[idx] == 1:
            add_result_to_winner_dict(
                winner_dict,
                competitions[idx][0],
            )
        else:
            add_result_to_winner_dict(
                winner_dict,
                competitions[idx][1],
            )

    return max(winner_dict, key=winner_dict.get)