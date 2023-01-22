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
    helps: list


@dataclass
class InterestsList:
    """
    The list of all the interests.
    """
    listy = []

    def __init__(self) -> None:
        self.listy.append(Interest('Transportation', ['Boredom', 'Loneliness']))
        self.listy.append(Interest('Performing Arts', ['Anger', 'Boredom', 'Loneliness']))
        self.listy.append(Interest('Landmark or Attraction', ['Stress', 'Boredom', 'Sadness']))
        self.listy.append(Interest('Featured Park', ['Anger', 'Stress']))
        self.listy.append(Interest('Nature', ['Anger', 'Stress']))
        self.listy.append(Interest('Garden / Conservatory', ['Sadness', 'Stress', 'Loneliness']))
        self.listy.append(Interest('Landmark', ['Anger', 'Sadness', 'Boredom']))
        self.listy.append(Interest('Gallery', ['Boredom', 'Loneliness']))
        self.listy.append(Interest('Visitor Information', ['Boredom']))
        self.listy.append(Interest('Attraction', ['Stress', 'Boredom', 'Loneliness']))
        self.listy.append(Interest('Museum', ['Stress', 'Boredom']))
        self.listy.append(Interest('Convention & Trade Centres', ['Boredom', 'Loneliness']))
        self.listy.append(Interest('Sports / Entertainment Venue', ['Sadness', 'Boredom', 'Loneliness']))


@dataclass
class TherapyTravel:
    """
        The main system class
        Attributes:
            - main_dict is the dictionary with 5 main emotions. It stores the results of the 15-question survey.

        >>> abc = TherapyTravel()
        >>> interest_List = InterestsList()
    """
    main_dict: dict

    def __init__(self) -> None:
        self.main_dict = {'Anger': 0, 'Boredom': 0, 'Loneliness': 0, 'Stress': 0, 'Sadness': 0}

    def set_Emotions_test(self) -> None:
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
        # The copy was created so that the pop method below wouldn't mutate the original dictionary
        copy_of_dict = self.main_dict.copy()

        max_key = max(copy_of_dict, key=copy_of_dict.get)
        st_value = (max_key, copy_of_dict[max_key])
        copy_of_dict.pop(st_value[0])
        max_key = max(copy_of_dict, key=copy_of_dict.get)
        nd_value = (max_key, copy_of_dict[max_key])
        point_difference = st_value[1] - nd_value[1]

        if point_difference > 5:
            return st_value[0]  # 'Anger' or 'Sadnessm' for example
        else:
            return st_value[0], nd_value[0]


def emotion_giving_method(sys: TherapyTravel, interests: InterestsList) -> str:
    """
    Method that will return an emotion based on the results of the 15-question survey
    """
    new_interests = []
    input_emotion = sys.two_strongest_emotions()

    if type(input_emotion) is not tuple:
        for interest in interests.listy:
            if input_emotion in interest.helps:
                new_interests.append(interest)
    else:
        for interest in interests.listy:
            if (input_emotion[0] in interest.helps) and (input_emotion[1] in interest.helps):
                new_interests.append(interest)
    return random.choice(new_interests).title
