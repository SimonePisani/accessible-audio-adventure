# BasicSceneMapping.py

def GetPossibleOutputs(scene_type):
    """
    Restituisce un dizionario delle possibili azioni in base al tipo di scena.
    """
    switch = {
        "StartMenu": {
            0: "Chiudi applicazione",
            1: "Riascolta tutorial",
            5: "Riascolta le possibilità",
            10: "inizia il gioco",
        },
        "Menu": {
            0: "Chiudi applicazione",
            5: "Riascolta le possibilità",
            10: "Ritorna alla gamescene corrente",
        },
        "SheetMenu": {
            1: "Stampa le clessidre",
            2: "Stampa gli oggetti",
            3: "Stampa i ricordi",
            5: "Riascolta le possibilità",
            10: "Ritorna alla gamescene corrente",
        },
        "Keypad": {
            0: "Inserisci codice 0",
            1: "Inserisci codice 1",
            2: "Inserisci codice 2",
            3: "Inserisci codice 3",
            4: "Inserisci codice 4",
            5: "Inserisci codice 5", 
            6: "Inserisci codice 6",
            7: "Inserisci codice 7",
            8: "Inserisci codice 8",
            9: "Inserisci codice 9",
            10: "Ritorno alla gamescene corrente"
        },
        "GameScene": {
            0: "Vai al Menu",
            1: "Vai al keypad",
            2: "Vai alla scheda",
            3: "Prova ad usare un aiuto",
            4: "Narration Audio",
            5: "Riascolta le possibilità",
            6: "Focus Audio",
        },
        "HelpScene": {
            1: "Accetta l'aiuto e torna alla scena di gioco",
            2: "Rifiuta l'aiuto e torna alla scena di gioco",
            5: "Riascolta le possibilità"
        }
    }
    return switch.get(scene_type, {})


def InputElaboration(sessione, current_scene, input, scenes, current_game_scene):
    """
    Elabora l'input dell'utente in base alla scena corrente e restituisce l'azione e l'audio associato.
    """
    switch = {
        "StartMenu": {
            0: ("Chiudi", ["Audios/_generic/closingApp.mp3"]),
            1: (None, ["Audios/_startingMenu/im_description.mp3"]),
            5: (None, ["Audios/_startingMenu/im_input.mp3"]),
            10: (scenes["GameScene_0161"], None),
        },
        "Menu": {
            0: ("Chiudi", ["Audios/_generic/closingApp.mp3"]),
            5: (None, ["Audios/_gameMenu/gm_input.mp3"]),
            10: (current_game_scene, None),
        },
        "SheetMenu": {
            1: (None, ["Audios/_sheetScene/ss_hourglass.mp3", f"Audios/_generic/_numbers/{sessione.hourglass}.mp3"]),
            2: (None, ["Audios/_sheetScene/ss_items.mp3"] + [f"Audios/_generic/items/{item}.mp3" for item in sessione.items] if sessione.items else ["Audios/_sheetScene/ss_noItems.mp3"]),
            3: (None, ["Audios/_sheetScene/ss_mementos.mp3"] + [f"Audios/_generic/mementos/_short/{memento}.mp3" for memento in sessione.mementos] if sessione.mementos else ["Audios/_sheetScene/ss_noMementos.mp3"]),
            5: (None, ["Audios/_sheetScene/ss_input.mp3"]),
            10: (current_game_scene, None),
        },
        "Keypad": {
            0: (None, "inserisci codice 0"),
            1: (None, "inserisci codice 1"),
            2: (None, "inserisci codice 2"),
            3: (None, "inserisci codice 3"),
            4: (None, "inserisci codice 4"),
            5: (None, "inserisci codice 5"), 
            6: (None, "inserisci codice 6"),
            7: (None, "inserisci codice 7"),
            8: (None, "inserisci codice 8"),
            9: (None, "inserisci codice 9"),
            10: (current_game_scene, None),
        },
        "GameScene": {
            0: (scenes["Menu"], None),
            1: (scenes["Keypad"], None),
            2: (scenes["SheetMenu"], None),
            3: (None, current_game_scene.GetHelpAudio()) if current_game_scene and current_game_scene.HasHelp() and current_game_scene.help_unlocked else (scenes["HelpScene"](current_game_scene.GetHelpAudio()), None) if current_game_scene and current_game_scene.HasHelp() else (None, ["Audios/_generic/nohelp.mp3"]),
            4: (None, current_game_scene.GetNarrationAudio() if current_game_scene else None),
            5: (None, current_game_scene.GetInputAudio() if current_game_scene else None),
            6: (None, current_game_scene.GetFocusAudio() if current_game_scene else None),
            
        },
        "HelpScene": {
            1: (None, ["Help"]),
            2: (current_game_scene, None),
            5: (None, ["Audios/_helpMenu/hs_intro.mp3"])
        }
    }

    scene_type = current_scene.type
    if scene_type in switch:
        if input in switch[scene_type]:
            return switch[scene_type][input]
        else:
            return None, current_scene.possible_outputs.get(input)
    else:
        return None, None
