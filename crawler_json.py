import sql_utils
from models import GameInfo, GameParticipants
import orjson



def crawl_json(file_path:str ) -> None:
    """Crawl the JSON file and write the most used properties to the database"""

    with open(file_path, 'rb') as file:
        data = orjson.loads(file.read())
       
        if isinstance(data, dict):
            info = data.get("info", {})
            metadata = data.get("metadata", {})
            current_game = GameInfo(
                match_id=metadata.get("matchId"),
                game_id=info['gameId'],
                game_creation=info['gameCreation'],
                game_duration=info['gameDuration'],
                game_start_timestamp=info['gameStartTimestamp'],
                game_end_timestamp=info['gameEndTimestamp'],
                game_mode=info['gameMode'],
                game_name=info['gameName'],
                game_type=info['gameType'],
                game_version=info['gameVersion'],
                map_id=info['mapId']
            )
            print("Game Info:", current_game)
            participants = info.get("participants", [])
            for participant in participants:
                current_participant = GameParticipants(
                    current_game.game_id,
                    champion_id=participant.get("championId"),
                    champion_name=participant.get("championName"),
                    kills=participant.get("kills"),
                    deaths=participant.get("deaths"),
                    assists=participant.get("assists")
                )
                print("Participant Info:", current_participant)



if __name__ == "__main__":
    print("Starting the script...")
    crawl_json("./ignores/match.json")



