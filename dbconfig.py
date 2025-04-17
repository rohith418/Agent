from dataclasses import dataclass
import datetime
from enum import Enum
import pathlib


class Bacķend(Enum):
MYSQL
1


POSTGRES
2


SQLITE


3


@dataclass


class BEConfiguration:
backend: Backend
minPoolConns: int
maxPoolConns: int


@dataclass
class ServerConfiguration:
port: int
log_file: pathlib.Path
@dataclass
class UserConfiguration:
name: str


birthday: datetime.date


@dataclass


class Configuration:
version: str
user: UserConfiguration
server: ServerConfiguration
db: BEConfiguration
