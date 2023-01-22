from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional
import csv
import copy
import random

@dataclass
class Interest:
    """An interest, like Art, Sports, Music, Skiing

    Instance Attributes:
      - every attribute is a bool value that decides if the interest helps to deal with an emotion
      - title is the title of the interest
    """
    title: str
    combats_Anger: bool
    combats_Sadness: bool
    combats_Stress: bool
    combats_Boredom: bool
    combats_Loneliness: bool


@dataclass
class InterestsList:
    """
    The listy of all the interests.
    """
    listy = []

    def __init__(self, interests: listy) -> None:
        self.listy.append(Interest('Transportation', False, False, False, True, True))
        self.listy.append(Interest('Performing Arts', True, False, False, True, False))
        self.listy.append(Interest('Landmark or Attraction', False, True, True, True, False))
        self.listy.append(Interest('Featured Park', True, False, True, False, False))
        self.listy.append(Interest('Nature', True, False, True, False, False))
        self.listy.append(Interest('Garden / Conservatory', False, True, True, False, True))
        self.listy.append(Interest('Landmark', True, True, False, True, False))
        self.listy.append(Interest('Gallery', False, False, False, True, True))
        self.listy.append(Interest('Visitor Information', False, False, False, True, False))
        self.listy.append(Interest('Attraction', False, False, True, True, True))
        self.listy.append(Interest('Museum', False, False, True, True, False))
        self.listy.append(Interest('Convention & Trade Centres', False, True, False, True, True))
        self.listy.append(Interest('Sports / Entertainment Venue', False, True, False, True, True))


def get_set_of_interests() -> Any:
    """Return the listy of interests.
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
    # return names, categs
    return categs


@dataclass
class TherapyTravel:
    """
        The main system class
        >>> abc = TherapyTravel()
        >>> interest_List = InterestsList()
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
        copy_of_dict = self.main_dict.copy()    #The copy was created so that the pop method below wouldn't
                                                # mutate the original dict

        max_key = max(copy_of_dict, key=copy_of_dict.get)
        st_value = (max_key, copy_of_dict[max_key])
        copy_of_dict.pop(st_value[0])
        max_key = max(copy_of_dict, key=copy_of_dict.get)
        nd_value = (max_key, copy_of_dict[max_key])
        point_difference = st_value[1] - nd_value[1]

        if point_difference > 5:
            return st_value[0]  # Anger or Sadness
        else:
            return st_value[0], nd_value[0]


def emotion_giving_method(sys: TherapyTravel, interests: InterestsList) -> str:
    """
    Method that will return an emotion based on the results of the 15-question survey
    """
    new_interests = []
    emotion = None
    two_emotions = None
    if type(sys.two_strongest_emotions()) is tuple:
        two_emotions = sys.two_strongest_emotions()
    else:
        emotion = sys.two_strongest_emotions()


    if type(sys.two_strongest_emotions()) is not tuple:
        if sys.two_strongest_emotions() == 'Anger':
            for interest in interests.listy:
                if interest.combats_Anger is True:
                    new_interests.append(interest)
        elif sys.two_strongest_emotions() == 'Boredom':
            for interest in interests.listy:
                if interest.combats_Boredom is True:
                    new_interests.append(interest)
        elif sys.two_strongest_emotions() == 'Loneliness':
            for interest in interests.listy:
                if interest.combats_Loneliness is True:
                    new_interests.append(interest)
        elif sys.two_strongest_emotions() == 'Sadness':
            for interest in interests.listy:
                if interest.combats_Sadness is True:
                    new_interests.append(interest)
        elif sys.two_strongest_emotions() == 'Stress':
            for interest in interests.listy:
                if interest.combats_Stress is True:
                    new_interests.append(interest)
    else:
        if 'Anger' and 'Boredom' in sys.two_strongest_emotions():
            for interest in interests.listy:
                if (interest.combats_Anger is True) or (interest.combats_Boredom is True):
                    new_interests.append(interest)
        elif 'Anger' and 'Loneliness' in sys.two_strongest_emotions():
            for interest in interests.listy:
                if (interest.combats_Anger is True) or (interest.combats_Loneliness is True):
                    new_interests.append(interest)
        elif 'Anger' and 'Stress' in sys.two_strongest_emotions():
            for interest in interests.listy:
                if (interest.combats_Anger is True) or (interest.combats_Stress is True):
                    new_interests.append(interest)


    return random.choice(new_interests)
