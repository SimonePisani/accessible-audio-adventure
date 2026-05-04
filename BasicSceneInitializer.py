from BasicScene import *

def InitializeScenes():
    """
    Inizializza e restituisce un dizionario di tutte le scene.
    """
    scenes = {
        "StartMenu": StartScene(),
        "Menu": MenuScene(),
        "SheetMenu": SheetScene(),
        "Keypad": KeypadScene(),
        "HelpScene": lambda help_message: HelpScene(help_message)
    }

    game_scenes_info = {
        "0001": {
            "linked_scenes": ["1399"],
            "narration_audio": ["Audios/_gameScene/_scenes/0001/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/0001/focus.mp3"]
        },
        "1399": {
            "linked_scenes": ["1581"],
            "narration_audio": ["Audios/_gameScene/_scenes/1399/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/1399/focus.mp3"]
        },
        "1581": {
            "linked_scenes": ["3078"],
            "narration_audio": ["Audios/_gameScene/_scenes/1581/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/1581/focus.mp3"]
        },
        "3078": {
            "linked_scenes": ["1225"],
            "narration_audio": ["Audios/_gameScene/_scenes/3078/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/3078/focus.mp3"]
        },
        "1225": {
            "linked_scenes": ["0221", "0161", "3310", "1198", "2289", "2880"],
            "has_help": True,
            "narration_audio": ["Audios/_gameScene/_scenes/1225/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/1225/focus.mp3"],
            "help_audio": ["Audios/_gameScene/_scenes/1225/help.mp3"],
            "comingback_audio": ["Audios/_gameScene/_scenes/1225/comingback.mp3"]
        },
        "0221": {
            "linked_scenes": ["3490", "1225"],
            "narration_audio": ["Audios/_gameScene/_scenes/0221/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/0221/focus.mp3"]
        },
        "0161": {
            "linked_scenes": ["5155", "1225"],
            "has_help": True,
            "narration_audio": ["Audios/_gameScene/_scenes/0161/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/0161/focus.mp3"],
            "help_audio": ["Audios/_gameScene/_scenes/0161/help.mp3"],
            "comingback_audio": ["Audios/_gameScene/_scenes/0161/comingback.mp3"]
        },
        "3310": {
            "linked_scenes": ["1225"],
            "mementos": ["lettera_preoccupata"],
            "narration_audio": ["Audios/_gameScene/_scenes/3310/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/3310/focus.mp3"]
        },
        "1198": {
            "linked_scenes": ["1225"],
            "items": ["torcia_elettrica", "magnete"],
            "narration_audio": ["Audios/_gameScene/_scenes/1198/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/1198/focus.mp3"]
        },
        "2289": {
            "linked_scenes": ["1225"],
            "mementos": ["quadro"],
            "narration_audio": ["Audios/_gameScene/_scenes/2289/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/2289/focus.mp3"]
        },
        "2880": {
            "linked_scenes": ["1225"],
            "mementos": ["biglietto"],
            "has_help": True,
            "narration_audio": ["Audios/_gameScene/_scenes/2880/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/2880/focus.mp3"],
            "help_audio": ["Audios/_gameScene/_scenes/2880/help.mp3"]
        },
        "3490": {
            "linked_scenes": ["1225"],
            "mementos": ["articoli_vittime"],
            "narration_audio": ["Audios/_gameScene/_scenes/3490/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/3490/focus.mp3"]
        },
        "5155": {
            "linked_scenes": ["1225", "5347"],
            "has_help": True,
            "narration_audio": ["Audios/_gameScene/_scenes/5155/narration.mp3"],
            "focus_audio": ["Audios/_gameScene/_scenes/5155/focus.mp3"],
            "help_audio": ["Audios/_gameScene/_scenes/5155/help.mp3"]
        },
        "5347": {
            "narration_audio": ["Audios/_gameScene/_scenes/ending.mp3"]
        }
    }

    def create_game_scene(key, info):
        """
        Crea una scena di gioco con le informazioni fornite.
        """
        return GameScene(
            key, 
            linked_scenes=info.get("linked_scenes", []),
            items=info.get("items", []),
            mementos=info.get("mementos", []),
            has_help=info.get("has_help", False),
            narration_audio=info.get("narration_audio", []),
            focus_audio=info.get("focus_audio", []),
            help_audio=info.get("help_audio", []),
            comingback_audio=info.get("comingback_audio", [])
        )

    for key, info in game_scenes_info.items():
        scenes[f"GameScene_{key}"] = create_game_scene(key, info)
    
    return scenes
