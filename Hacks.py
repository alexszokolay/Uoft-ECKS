from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional
import csv

@dataclass
class Interest:
    """An interest, like Art, Sports, Music, Skiing

    Instance Attributes:
      - every attribute is a bool value that decides if the interest helps to deal with an emotion
    """
    combats_Anger: bool
    combats_Sadness: bool
    combats_Stress: bool
    combats_Boredom: bool
    combats_Loneliness: bool


@dataclass
class InterestsList:
    """
    The list of all the interests.
    """
    _list = []

    def add_Interest(self, interest: Interest) -> None:
        """
        Adds a given interest to the list
        """


def read_csv_file() -> Any:
    """Return the set of interests.
    -
    Preconditions:
      - filename refers to a valid csv file with headers
    """
    import csv

    file = "places_of_interest.csv"

    # create lists of names, categories
    # (file) -> (listOfNames, listOfCategories)

    names = []
    categs = []
    with open(file, 'r', newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            for i in range(len(row)):
                if i == 0:
                    names.append(row[i])
                elif i == 2:
                    categs.append(row[i])
    #return names, categs
    return set(categs)


@dataclass
class TherapyTravel:
    """
        The main system class
        >>> abc = TherapyTravel()
        Representation Invariants:
        -
    """
    # anger: (str, int)
    # boredom: (str, int)
    # loneliness: (str, int)
    # stress: (str, int)
    # sadness: (str, int)
    main_dict: dict

    def __init__(self) -> None:
        self.main_dict = {'Anger': 0, 'Boredom': 0,
                          'Loneliness': 0, 'Stress': 0, 'Sadness': 0}

    def set_Emotions(self) -> None:
        """
        Just a set method for testing purposes
        """
        self.main_dict['Anger'] = 2
        self.main_dict['Boredom'] = 5
        self.main_dict['Loneliness'] = 5
        self.main_dict['Stress'] = 6
        self.main_dict['Sadness'] = 15

    def two_strongest_emotions(self) -> Any:
        """
        Method that returns two strongest emotions and the point difference between them or just the strongest emotion
        """
        max_key = max(self.main_dict, key=self.main_dict.get)
        st_value = (max_key, self.main_dict[max_key])
        self.main_dict.pop(st_value[0])
        max_key = max(self.main_dict, key=self.main_dict.get)
        nd_value = (max_key, self.main_dict[max_key])
        point_difference = st_value[1] - nd_value[1]

        if point_difference > 5:
            return st_value[0] #Anger or Sadness
        else:
            return st_value[0], nd_value[0]


def emotion_giving_method(sys: TherapyTravel) -> str:
    """
    Method that will return an emotion based on the results of the 15-question survey
    """
    if sys.two_strongest_emotions() == 'Anger':
        return "anger remedy"
    elif sys.two_strongest_emotions() == 'Boredom':
        return 'boredom remedy'
    elif sys.two_strongest_emotions() == 'Loneliness':
        return 'loneliness remedy'
    elif sys.two_strongest_emotions() == 'Sadness':
        return 'sadness remedy'
    elif sys.two_strongest_emotions() == 'Stress':
        return 'stress remedy'
