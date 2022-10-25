from pydantic import BaseModel
from rich import print
from devtools import debug

class MusicBand(BaseModel):
    name: str


class Song(BaseModel):
    title: str
    how_long: int


class Album(BaseModel):
    band: MusicBand
    songs: list[Song]


def t2est_metallica():
    data = {
        'band': {
            'name': 'Metallica',
        },
        'songs': [
            {
                'title': 'Killem all',
                'how_long': '320'
            },
            {
                'title': 'And justice for all',
                'how_long': '400'
            }
        ]
    }

    album_from_dict = Album(**data)

    album = Album(band={'name': 'Metallica'},
                  songs=[
                      {'title': 'Killem all', 'how_long': 320},
                      {'title': 'And justice for all', 'how_long': '400'}
                  ])

    assert 'Metallica' == album.band.name
    assert 320 == album.songs[0].how_long
    assert 'And justice for all' == album.songs[1].title
    assert album_from_dict == album
    print(album)
    debug(album)
