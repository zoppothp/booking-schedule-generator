from datetime import datetime

seasons = {
    "winter_pre": (datetime(2024, 11, 1), datetime(2024, 12, 23)),
    "christmas": (datetime(2024, 12, 24), datetime(2025, 1, 8)),
    "winter_past": (datetime(2025, 1, 9), datetime(2025, 3, 31)),
    "spring": (datetime(2025, 4, 1), datetime(2025, 6, 30)),
    "summer": (datetime(2025, 7, 1), datetime(2025, 9, 1)),
    "fall": (datetime(2025, 9, 2), datetime(2025, 10, 31)),
}

appartments = {
    "typ_a": {
        "name": "Wohnung Typ A",
        "size": "36 m2",
        "cleaning_price": 40,
        "prices": {
            "winter_pre": {"2 persons": 70, "3 persons": 73},
            "christmas": {"2 persons": 98, "3 persons": 101},
            "winter_past": {"2 persons": 86, "3 persons": 89},
            "spring": {"2 persons": 70, "3 persons": 73},
            "summer": {"2 persons": 80, "3 persons": 83},
            "fall": {"2 persons": 70, "3 persons": 73},
        },
    },
    "typ_b": {
        "name": "Wohnung Typ B",
        "size": "50 m2",
        "cleaning_price": 50,
        "prices": {
            "winter_pre": {"2 persons": 80, "3 persons": 85, "4 persons": 90},
            "christmas": {"2 persons": 108, "3 persons": 113, "4 persons": 118},
            "winter_past": {"2 persons": 98, "3 persons": 103, "4 persons": 108},
            "spring": {"2 persons": 80, "3 persons": 85, "4 persons": 90},
            "summer": {"2 persons": 90, "3 persons": 95, "4 persons": 100},
            "fall": {"2 persons": 80, "3 persons": 85, "4 persons": 90},
        },
    },
    "typ_c": {
        "name": "Wohnung Typ C",
        "size": "75 m2",
        "cleaning_price": 60,
        "prices": {
            "winter_pre": {"3 persons": 88, "4 persons": 93},
            "christmas": {"3 persons": 118, "4 persons": 123},
            "winter_past": {"3 persons": 108, "4 persons": 110},
            "spring": {"3 persons": 88, "4 persons": 93},
            "summer": {"3 persons": 98, "4 persons": 103},
            "fall": {"3 persons": 88, "4 persons": 93},
        },
    },
    "typ_d": {
        "name": "Wohnung Typ D",
        "size": "90 m2",
        "cleaning_price": 70,
        "prices": {
            "winter_pre": {"4 persons": 107, "5 persons": 110, "6 persons": 113},
            "christmas": {"4 persons": 135, "5 persons": 138, "6 persons": 141},
            "winter_past": {"4 persons": 125, "5 persons": 130, "6 persons": 135},
            "spring": {"4 persons": 107, "5 persons": 110, "6 persons": 113},
            "summer": {"4 persons": 117, "5 persons": 120, "6 persons": 123},
            "fall": {"4 persons": 107, "5 persons": 110, "6 persons": 113},
        },
    },
}
