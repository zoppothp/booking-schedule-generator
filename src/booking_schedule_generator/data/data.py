from datetime import datetime

seasons = {
    "winter_pre": {"start": datetime(2024, 11, 1), "end": datetime(2024, 12, 23)},
    "christmas": {"start": datetime(2024, 12, 24), "end": datetime(2025, 1, 8)},
    "winter_past": {"start": datetime(2025, 1, 9), "end": datetime(2025, 3, 31)},
    "spring": {"start": datetime(2025, 4, 1), "end": datetime(2025, 6, 30)},
    "summer": {"start": datetime(2025, 7, 1), "end": datetime(2025, 9, 1)},
    "fall": {"start": datetime(2025, 9, 2), "end": datetime(2025, 10, 31)},
}

appartments = {
    "wg_1": {
        "name_full": "WG 1",
        "type": "Typ C",
        "size": "75 m2",
        "cleaning_price": 60,
        "prices": {
            "winter_pre": {"3 Pers.": 88, "4 Pers.": 93},
            "christmas": {"3 Pers.": 118, "4 Pers.": 123},
            "winter_past": {"3 Pers.": 108, "4 Pers.": 110},
            "spring": {"3 Pers.": 88, "4 Pers.": 93},
            "summer": {"3 Pers.": 98, "4 Pers.": 103},
            "fall": {"3 Pers.": 88, "4 Pers.": 93},
        },
    },
    "wg_2": {
        "name_full": "WG 2",
        "type": "Typ A",
        "size": "36 m2",
        "cleaning_price": 40,
        "prices": {
            "winter_pre": {"2 Pers.": 70, "3 Pers.": 73},
            "christmas": {"2 Pers.": 98, "3 Pers.": 101},
            "winter_past": {"2 Pers.": 86, "3 Pers.": 89},
            "spring": {"2 Pers.": 70, "3 Pers.": 73},
            "summer": {"2 Pers.": 80, "3 Pers.": 83},
            "fall": {"2 Pers.": 70, "3 Pers.": 73},
        },
    },
    "wg_3": {
        "name_full": "WG 3",
        "type": "Typ B",
        "size": "50 m2",
        "cleaning_price": 50,
        "prices": {
            "winter_pre": {"2 Pers.": 80, "3 Pers.": 85, "4 Pers.": 90},
            "christmas": {"2 Pers.": 108, "3 Pers.": 113, "4 Pers.": 118},
            "winter_past": {"2 Pers.": 98, "3 Pers.": 103, "4 Pers.": 108},
            "spring": {"2 Pers.": 80, "3 Pers.": 85, "4 Pers.": 90},
            "summer": {"2 Pers.": 90, "3 Pers.": 95, "4 Pers.": 100},
            "fall": {"2 Pers.": 80, "3 Pers.": 85, "4 Pers.": 90},
        },
    },
    "wg_4": {
        "name_full": "WG 4",
        "type": "Typ D",
        "size": "90 m2",
        "cleaning_price": 70,
        "prices": {
            "winter_pre": {"4 Pers.": 107, "5 Pers.": 110, "6 Pers.": 113},
            "christmas": {"4 Pers.": 135, "5 Pers.": 138, "6 Pers.": 141},
            "winter_past": {"4 Pers.": 125, "5 Pers.": 130, "6 Pers.": 135},
            "spring": {"4 Pers.": 107, "5 Pers.": 110, "6 Pers.": 113},
            "summer": {"4 Pers.": 117, "5 Pers.": 120, "6 Pers.": 123},
            "fall": {"4 Pers.": 107, "5 Pers.": 110, "6 Pers.": 113},
        },
    },
    "wg_5": {
        "name_full": "WG 5",
        "type": "Typ B",
        "size": "50 m2",
        "cleaning_price": 50,
        "prices": {
            "winter_pre": {"2 Pers.": 80, "3 Pers.": 85, "4 Pers.": 90},
            "christmas": {"2 Pers.": 108, "3 Pers.": 113, "4 Pers.": 118},
            "winter_past": {"2 Pers.": 98, "3 Pers.": 103, "4 Pers.": 108},
            "spring": {"2 Pers.": 80, "3 Pers.": 85, "4 Pers.": 90},
            "summer": {"2 Pers.": 90, "3 Pers.": 95, "4 Pers.": 100},
            "fall": {"2 Pers.": 80, "3 Pers.": 85, "4 Pers.": 90},
        },
    },
    "wg_6": {
        "name_full": "WG 6",
        "type": "Typ B",
        "size": "50 m2",
        "cleaning_price": 50,
        "prices": {
            "winter_pre": {"2 Pers.": 80, "3 Pers.": 85, "4 Pers.": 90},
            "christmas": {"2 Pers.": 108, "3 Pers.": 113, "4 Pers.": 118},
            "winter_past": {"2 Pers.": 98, "3 Pers.": 103, "4 Pers.": 108},
            "spring": {"2 Pers.": 80, "3 Pers.": 85, "4 Pers.": 90},
            "summer": {"2 Pers.": 90, "3 Pers.": 95, "4 Pers.": 100},
            "fall": {"2 Pers.": 80, "3 Pers.": 85, "4 Pers.": 90},
        },
    },
}
