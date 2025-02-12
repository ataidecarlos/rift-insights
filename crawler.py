import constants, sql_utils
import json
import requests
import time

APIKEY: str = constants.RIOT_API

def crawl_matches(region: str, server: str, match_id: int) -> int:
    """Returns JSON for the requested match id"""
    uri: str = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{server.upper()}_{match_id}'
    result  = requests.get(uri, timeout=5, headers={'X-Riot-Token': APIKEY})

    sql_utils.write_match(server, region, match_id, result.status_code)
    print(f"Match {match_id} - {result.status_code}")

    if result.status_code == 200:
        with open(f'./raw/{region}_{server}_{match_id}.json', 'w', encoding='utf-8') as file:
            json.dump(result.json(), file)

        return match_id
    elif result.status_code == 404:
        return result.status_code * -1
    elif result.status_code == 401:
        return result.status_code * -1
    elif result.status_code == 403:
        return result.status_code * -1
    else:
        return -1



if __name__ == "__main__":
    # For the time being, this is hardcoded to EUW
    region: str = "EUROPE"
    server: str = "EUW1"

    all_good: bool = True
    match_id: int = sql_utils.get_crawler_next_match_reverse(region, server)

    while all_good is True:
        if crawl_matches(region, server, match_id) < 0:
            all_good = False
            break
        match_id -= 1
        time.sleep(1.5)
