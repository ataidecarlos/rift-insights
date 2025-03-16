from dataclasses import dataclass

@dataclass
class GameInfo:
    """Dataclass to represent game information."""
    match_id: str
    game_id: int
    game_creation: int
    game_duration: int
    game_start_timestamp: int
    game_end_timestamp: int
    game_mode: str
    game_name: str
    game_type: str
    game_version: str
    map_id: int

@dataclass
class GameParticipants:
    """Dataclass to represent game participants."""
    game_id: int
    champion_id: int
    champion_name: str
    kills: int
    deaths: int
    assists: int