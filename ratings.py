import os
import struct
from typing import Tuple


class AnimeRating:
    def __init__(self, title: str, thumbnail: Tuple[bytes, str], animation_quality: int | float, music: int | float,
                 characters: int | float, character_development: int | float, story: int | float, plot: int | float,
                 entertainment: int | float, impact: int | float = None, immersion: int | float = None):
        self.title = title
        self.thumbnail = thumbnail
        self.animation_quality = animation_quality
        self.music = music
        self.characters = characters
        self.character_development = character_development
        self.story = story
        self.plot = plot
        self.entertainment = entertainment
        self.scores = [
            self.animation_quality, 
            self.music,
            self.characters,
            self.character_development,
            self.story,
            self.plot,
            self.entertainment
        ]
        if impact:
            self.impact = impact
            self.scores.append(self.impact)
        if immersion:
            self.immersion = immersion
            self.scores.append(self.immersion)

    def get_final_score(self):
        total = 0
        for value in self.scores:
            total += value
        score = (total / 80) * 10
        if int(str(score).split('.')[1]) == 0: return int(score)
        return score

    def save_as_binary_file(self):

        def fhex(__number: float) -> str:
            """
            Return the hexadecimal representation of a floating point number.

            ```python
            >>> fhex(17.5)
            '4031800000000000'
            ```
            """
            return hex(struct.unpack('<Q', struct.pack('<d', __number))[0])[2:]

        null_byte = b'\xff'
        with open(os.path.join("reviews", f"{self.title}.bin"), "wb") as f:
            f.write(self.title.encode())
            f.write(null_byte)
            f.write(self.thumbnail[1].encode())
            f.write(null_byte)
            f.write(self.thumbnail[0])
            f.write(null_byte * 2)

            for value in self.scores:
                f.write(fhex(value).encode())
                f.write(b"\xff")


class MovieRating(AnimeRating):
    def __init__(self, title: str, thumbnail: Tuple[bytes, str], production_quality: int | float, music: int | float,
                 characters: int | float, character_development: int | float, story: int | float, plot: int | float,
                 entertainment: int | float, impact: int | float = None, immersion: int | float = None):
        self.title = title
        self.thumbnail = thumbnail
        self.production_quality = production_quality
        self.music = music
        self.characters = characters
        self.character_development = character_development
        self.story = story
        self.plot = plot
        self.entertainment = entertainment
        self.scores = [
            self.production_quality, 
            self.music,
            self.characters,
            self.character_development,
            self.story,
            self.plot,
            self.entertainment
        ]
        if impact:
            self.impact = impact
            self.scores.append(self.impact)
        if immersion:
            self.immersion = immersion
            self.scores.append(self.immersion)


class TvShowRating(MovieRating):
    def __init__(self, title: str, thumbnail: Tuple[bytes, str], production_quality: int | float, music: int | float,
                 characters: int | float, character_development: int | float, story: int | float, plot: int | float,
                 entertainment: int | float, impact: int | float = None, immersion: int | float = None):
        super().__init__(title, thumbnail, production_quality, music, characters, character_development, story, plot,
                         entertainment, impact, immersion)
