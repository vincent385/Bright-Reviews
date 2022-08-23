import os
import struct
from pathlib import Path
from typing import Tuple


"""
TODO
    Rewire the engine to read/write true .bin files instead of whatever i was doing..
"""
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
            '0x4031800000000000'
            ```
            """
            return hex(struct.unpack('<Q', struct.pack('<d', __number))[0])

        def ahex(__text: str) -> str:
            """
            Return the hexadecimal representation of an ascii string. There is no 0x prefix for each individual byte.

            ```python
            >>> ahex("A quick brown fox")
            '4120717569636b2062726f776e20666f78'
            ```
            """
            hex_str = ""
            for char in __text:
                hex_str += hex(ord(char))[2:]
            return hex_str

        with open(os.path.join("reviews", f"{self.title}.bin"), "wb") as f:
            # raw = bytes.fromhex(ahex(my_string))
            f.write(ahex(self.thumbnail[0].decode()).encode())
            f.write('\n'.encode())
            f.write(ahex(self.thumbnail[1]).encode())
            f.write('\n'.encode())

            for value in self.scores:
                if type(value) == int: f.write(bin(value).replace("0b", '').encode())
                else: f.write(fhex(value).encode())
                f.write("\n".encode())


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


def load_rating_from_bin(bin_file_path: Path, __type: AnimeRating | MovieRating | TvShowRating):

    def convert_binascii(binary: str) -> str:
        """
        Convert a binary string to an ascii string.

        :binary: Binary string to transform.
        :return: Ascii string
        """
        __ascii = ""
        for i in range(0, len(binary), 8):
            __ascii += chr(int(binary[i:i+8], 2))
        return __ascii

    def convert_binscore(binary: str) -> int | float:

        def convert_binfloat():
            t = int(binary, 2).to_bytes(8, byteorder="big")
            return struct.unpack(">d", t)[0]

        if len(binary) == 64: return convert_binfloat()
        return int(binary, 2)

    assert __type in [AnimeRating, MovieRating, TvShowRating], "The rating type must be for an Anime, Movie or Tv Show."
    with open(bin_file_path, "rb") as f:
        contents = f.readlines()
    contents = [x.strip() for x in contents]
    # Temporary solution
    title = bin_file_path.split('.')[0].split('\\')[1]
    print(title)
    thumbnail_img = convert_binascii(contents[0].decode()).encode()
    thumbnail_fmt = convert_binascii(contents[1].decode())
    print(thumbnail_fmt)
    scores = [convert_binscore(x.decode()) for x in contents[2:]]
    if len(scores) == 9:
        return __type(title, (thumbnail_img, thumbnail_fmt), scores[0], scores[1], scores[2], scores[3], scores[4],
                      scores[5], scores[6], scores[7], scores[8])
    elif len(scores) == 10:
        return __type(title, (thumbnail_img, thumbnail_fmt), scores[0], scores[1], scores[2], scores[3], scores[4],
                      scores[5], scores[6], scores[7], scores[8], scores[9])
    elif len(scores) == 11:
        return __type(title, (thumbnail_img, thumbnail_fmt), scores[0], scores[1], scores[2], scores[3], scores[4],
                      scores[5], scores[6], scores[7], scores[8], scores[9], scores[10])
    else:
        assert False, "An unknown error occcured when creating a {__type} from {bin_file_path}."
