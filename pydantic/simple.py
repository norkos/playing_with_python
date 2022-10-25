import json
import pytest
from pydantic import BaseModel, ValidationError, parse_obj_as, Field
from datetime import datetime
from uuid import UUID, uuid4


class Tweet(BaseModel):
    id: int
    text: str | None = None
    created: datetime
    shared_by: list[int] = []

    class Config:
        allow_mutation = False


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


def test_immutability():
    data = {
        'id': 123,
        'created': '2019-06-01 12:22',
        'shared_by': [1, 2, 3]
    }

    tweet = Tweet(**data)
    with pytest.raises(TypeError):
        tweet.id = 12


def test_create_tweet_without_id():
    data = {
        'created': '2019-06-01 12:22',
        'shared_by': [1, 2, 3]
    }
    with pytest.raises(ValidationError):
        Tweet(**data)


def test_object_parsing():
    data = {
        'id': 123,
        'created': '2019-06-01 12:22',
        'shared_by': [1, 2, 3]
    }
    tweet = Tweet.parse_obj(data)
    assert data['id'] == tweet.id


def test_raw_parsing():
    data = '{"id": "123", "created": "2019-06-01 12:22"}'
    jsonized = json.loads(data)

    tweet = Tweet.parse_raw(data)
    assert jsonized['id'] == str(tweet.id)


class MyModel(BaseModel):
    uuid: UUID = Field(default_factory=uuid4)
    updated: datetime = Field(default_factory=datetime.utcnow)


def test_default_factory():
    model = MyModel()
    assert model.uuid
    assert model.updated

