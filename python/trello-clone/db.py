from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

from main import config
print("Config", config)
# username = "postgres"
# password = "7838e68ed462ebc61e745c07f0e27ab264a72ce5533d6216"
# hostname = "trolli.fly.dev"
# proxy_port = 5432
# database = "trolli"
# ipv6HostName = "[fdaa:0:69fa:a7b:2dbb:1:53d8:2]"

engine = create_engine(
    f"postgresql://{config.username}:{config.password}@{config.ipv6HostName}:{config.proxy_port}?options", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)

    boards = relationship("Board", back_populates="users")

    def __repr__(self):
        return f"BoardList(id={self.id!r}, name={self.name!r})"


class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    boards = relationship("User", back_populates="boards")

    def __repr__(self):
        return f"Board(id={self.id!r}, name={self.name!r})"


class BoardList(Base):
    __tablename__ = "board_lists"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    board_id = Column(Integer, ForeignKey("board.id"), nullable=False)

    def __repr__(self):
        return f"BoardList(id={self.id!r}, name={self.name!r})"


Base.metadata.create_all(engine)
