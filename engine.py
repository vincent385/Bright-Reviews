import struct
from io import BytesIO
from base64 import b64encode
from pathlib import Path
from binascii import hexlify
from ratings import AnimeRating, MovieRating, TvShowRating


class Decoder:
    def __init__(self, file_contents: bytes):
        self.data = BytesIO(file_contents)
        self.offset = 0
        tnfmt_len = self.read_null_terminated_int_lt16()
        self.offset += 2
        self.__thumbnail_fmt = self.read_fixed_length_string(tnfmt_len)
        self.offset -= tnfmt_len * 2 + 2
        self.__thumbnail_img = self.read_and_b64encode_img()
        number_of_scores = self.read_null_terminated_int_lt16()
        self.__scores = [self.read_null_terminated_double() for _ in range(number_of_scores)]

    def read_fixed_length_string(self, length):
        string = ""
        for _ in range(length):
            self.data.seek(self.offset)
            current_byte = bytes.fromhex(self.data.read(2).decode())
            self.offset += 2
            string += current_byte.decode("utf-8")
        return string

    def read_null_terminated_string(self):
        string = ""
        current_byte = b''
        while current_byte != b'\xff':
            string += current_byte.decode("utf-8")
            self.data.seek(self.offset)
            current_byte = bytes.fromhex(self.data.read(2).decode())
            self.offset += 2
        return string

    def read_null_terminated_int_lt16(self):
        current_byte = b''
        while current_byte != b'\xff':
            intv = current_byte
            self.data.seek(self.offset)
            current_byte = bytes.fromhex(self.data.read(2).decode())
            self.offset += 2
        return int.from_bytes(intv, 'big')

    def read_null_terminated_double(self):

        def hexf(__bytes: bytes) -> int | float:
            """
            Return a floating point value from converting a double stored as hex bytes.

            ```python
            >>> hexif("4031800000000000")
            17.5
            """
            return struct.unpack('!d', bytes.fromhex(__bytes.decode()))[0]
 
        hex_bytes = b''
        current_byte = b''
        while current_byte != b'ff':
            hex_bytes += current_byte
            self.data.seek(self.offset)
            current_byte = self.data.read(2)
            self.offset += 2
        value = hexf(hex_bytes)
        return value if int(str(value).split('.')[1]) != 0 else int(value)

    def read_and_b64encode_img(self):
        img_bytes = b''
        current_byte = b''
        buf4 = b''
        while buf4 != b'\xff\xff\xff\xff':
            img_bytes += current_byte
            self.data.seek(self.offset)
            current_byte = bytes.fromhex(self.data.read(2).decode())
            self.offset += 2
            if len(buf4) < 4:
                buf4 += current_byte
            else:
                buf4 = b''
        return b64encode(img_bytes)

    def get_thumbnail_img(self):
        return self.__thumbnail_img

    def get_thumbnail_fmt(self):
        return self.__thumbnail_fmt

    def get_scores(self):
        return self.__scores


def load_rating_from_binary_file(file_path: Path, __type: AnimeRating | MovieRating | TvShowRating) -> AnimeRating | MovieRating | TvShowRating:
    """
    Return a rating object of the type specified by __type if the binary file specified in file_path is read successfully.
    """
    assert __type in [AnimeRating, MovieRating, TvShowRating], "The rating type must be for an Anime, Movie or Tv Show."
    with open(file_path, "rb") as f:
        contents = hexlify(f.read())
    file_decoder = Decoder(contents)
    title = file_path.split('.')[0].split('\\')[1]
    thumbnail_img = file_decoder.get_thumbnail_img()
    thumbnail_fmt = file_decoder.get_thumbnail_fmt()
    scores = file_decoder.get_scores()

    if len(scores) == 7:
        return __type(title, (thumbnail_img, thumbnail_fmt), scores[0], scores[1], scores[2], scores[3], scores[4],
                      scores[5], scores[6])
    elif len(scores) == 8:
        return __type(title, (thumbnail_img, thumbnail_fmt), scores[0], scores[1], scores[2], scores[3], scores[4],
                      scores[5], scores[6], scores[7])
    elif len(scores) == 9:
        return __type(title, (thumbnail_img, thumbnail_fmt), scores[0], scores[1], scores[2], scores[3], scores[4],
                      scores[5], scores[6], scores[7], scores[8])
