import os
import struct
from pathlib import Path
from typing import Tuple


"""
TODO
    Design the UI and logic.
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

    def save_as_binary(self):

        def fbin(__number: float) -> str:
            """
            Get the 64-bit binary representation of a floating point number.

            :__number: Float value to transform.
            :return: 64-bit binary string.
            """
            [t] = struct.unpack(">Q", struct.pack(">d", __number))
            return f'{t:064b}'

        def abin(__text: str) -> str:
            """
            Convert a string containing ascii characters to an unseparated binary string.

            :__text: String to transform.
            :return: Unseparated binary string.
            """
            binary = ""
            for char in __text:
                raw = bin(ord(char)).replace("0b", '')
                while len(raw) < 8:
                    raw = '0' + raw
                binary += raw
            return binary

        with open(os.path.join("reviews", f"{self.title}.bin"), "wb") as f:
            f.write(abin(self.thumbnail[0].decode()).encode())
            f.write('\n'.encode())
            f.write(abin(self.thumbnail[1]).encode())
            f.write('\n'.encode())

            for value in self.scores:
                if type(value) == int: f.write(bin(value).replace("0b", '').encode())
                else: f.write(fbin(value).encode())
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
