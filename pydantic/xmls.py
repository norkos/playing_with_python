from pydantic import BaseModel
from pydantic.utils import GetterDict
from typing import Any
from xml.etree.ElementTree import fromstring


xmlstring = """
<User Id="2008" Status="busy">
    <FirstName />
    <LastName Value="Janek" />
    <LoggedIn Value="true" />
</User>
"""


class UserGetter(GetterDict):

    def get(self, key: str, default: Any = None) -> Any:

        # attribute
        if key in {'Id', 'Status'}:
            return self._obj.attrib.get(key, default)

        # child
        try:
            return self._obj.find(key).attrib['Value']
        except(AttributeError, KeyError):
            return default


class User(BaseModel):
    Id: int
    Status: str | None = None
    FirstName: str | None = None
    LastName: str
    LoggedIn: bool

    class Config:
        orm_mode = True
        getter_dict = UserGetter


def test_parse_xml():
    xml = fromstring(xmlstring)
    user = User.from_orm(xml)
    assert 2008 == user.Id
    assert user.LoggedIn
    assert user.FirstName is None
    assert 'busy' == user.Status
    assert 'Janek' == user.LastName
