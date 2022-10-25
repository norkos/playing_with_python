import pytest
from pydantic import BaseModel, ValidationError
from datetime import datetime


class Tweet(BaseModel):
    id: int
    text: str | None = None
    created: datetime
    shared_by: list[int] = []


def test_create_tweet():
    data = {
        'id': 123,
        'text': 'dummy one',
        'created': '2019-06-01 12:22',
        'shared_by': [1, 2, 3]
    }

    tweet = Tweet(**data)
    assert data['id'] == tweet.id
    assert data['text'] == tweet.text


def test_create_tweet_without_text():
    data = {
        'id': 123,
        'created': '2019-06-01 12:22',
        'shared_by': [1, 2, 3]
    }

    tweet = Tweet(**data)
    assert data['id'] == tweet.id
    assert tweet.text is None


def test_create_tweet_without_id():
    data = {
        'created': '2019-06-01 12:22',
        'shared_by': [1, 2, 3]
    }
    with pytest.raises(ValidationError):
        Tweet(**data)
