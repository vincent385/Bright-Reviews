import struct
from pathlib import Path
from binascii import hexlify
from ratings import AnimeRating, MovieRating, TvShowRating


class Encoder:
    NotImplemented


class Decoder:
    NotImplemented


def load_rating_from_binary_file(file_path: Path, __type: AnimeRating | MovieRating | TvShowRating):

    def hexif(__bytes: bytes) -> int | float:
        """
        Return either an integer or floating point value from converting a double stored as hex bytes.

        ```python
        >>> hexif("4031800000000000")
        17.5

        >>> hexif("")
        ```
        """
        return struct.unpack('!d', bytes.fromhex(__bytes.decode()))[0]

    assert __type in [AnimeRating, MovieRating, TvShowRating], "The rating type must be for an Anime, Movie or Tv Show."
    with open(file_path, "rb") as f:
        contents = f.readlines()
    contents = [x.strip() for x in contents]
    print(contents)
    # title = file_path.split('.')[0].split('\\')[1]
    # thumbnail_img = convert_binascii(contents[0].decode()).encode()
    # thumbnail_fmt = convert_binascii(contents[1].decode())

    scores = [hexif(x) for x in contents]
    print(scores)
    # if len(scores) == 9:
    #     return __type(title, (thumbnail_img, thumbnail_fmt), scores[0], scores[1], scores[2], scores[3], scores[4],
    #                   scores[5], scores[6], scores[7], scores[8])
    # elif len(scores) == 10:
    #     return __type(title, (thumbnail_img, thumbnail_fmt), scores[0], scores[1], scores[2], scores[3], scores[4],
    #                   scores[5], scores[6], scores[7], scores[8], scores[9])
    # elif len(scores) == 11:
    #     return __type(title, (thumbnail_img, thumbnail_fmt), scores[0], scores[1], scores[2], scores[3], scores[4],
    #                   scores[5], scores[6], scores[7], scores[8], scores[9], scores[10])
    # else:
    #     assert False, "An unknown error occcured when creating a {__type} from {bin_file_path}."
