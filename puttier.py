# -*- coding: utf-8 -*-
from themeloader import *
from puttysessions import *
try:
    input = raw_input
except NameError: pass

class Puttier:

    @staticmethod
    def loadThemes():
        themes_db = ThemeLoader.loadThemes()
        default_theme = Theme.default()
        themes_db[default_theme.toHash()] = default_theme
        # putty_sessions = list(PuttyLoader.sessions())
        # for index, s in enumerate(putty_sessions):
        #     known_theme = None
        #     th_hash = s.theme.toHash()
        #     if th_hash in themes_db:
        #         known_theme = themes_db[th_hash].name
        #     print("{:3d}. Session: {} has theme = {}".format(index, s.name, known_theme if known_theme else "Custom" ))
        return themes_db

    @staticmethod
    def loadSessions(themes_db = None):
        putty_sessions = list(PuttyLoader.sessions())
        sessions_dict = dict()
        for index, s in enumerate(putty_sessions):
            known_theme = None
            th_hash = s.theme.toHash()
            if themes_db:
                if th_hash in themes_db:
                    known_theme = themes_db[th_hash].name
            sessions_dict[s] = known_theme
        return sessions_dict


def main():
    themes_db = ThemeLoader.loadThemes()
    default_theme = Theme.default()
    themes_db[default_theme.toHash()] = default_theme
    putty_sessions = list(PuttyLoader.sessions())
    session_len = 0
    for index, s in enumerate(putty_sessions):
        known_theme = None
        th_hash = s.theme.toHash()
        if th_hash in themes_db:
            known_theme = themes_db[th_hash].name
        print("{:3d}. Session: {} has theme = {}".format(index, s.name, known_theme if known_theme else "Custom" ))
        session_len = index

    session_idx_raw = int(input("Enter the Index of Session to Update: "))
    if not isinstance(session_idx_raw, int):
        raise Exception("Error: Invalid session given {}".format(session_idx_raw))
    session_idx = int(session_idx_raw)
    if session_idx <0 or session_idx > session_len:
        raise Exception("Error: Invalid session number given | max = {}".format(session_len))
    selected_session = putty_sessions[session_idx]
    print("Selected session: {}".format(selected_session.name))
    theme_name = None
    theme_names = {v.name: v for k,v in themes_db.items()}
    while theme_name not in theme_names:
        theme_name = input("Enter the Name of the Theme to use: ")
    PuttyUpdate.updateSession(selected_session.name, theme_names[theme_name])
    theme_updated = PuttyLoader.themeBySession(selected_session.name)
    theme_name_updated = themes_db[theme_updated.toHash()].name
    print("Theme updated to: {}".format(theme_name_updated))

if __name__ == "__main__":
    main()
