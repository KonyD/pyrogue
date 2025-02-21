from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING

import color
import exceptions # type: ignore

if TYPE_CHECKING:
    from engine import Engine
    from entities.entity import Entity
    from entities.actor import Actor
    from entities.item import Item


class Action:
    def __init__(self, entity: Actor) -> None:
        super().__init__()
        self.entity = entity

    @property
    def engine(self) -> Engine:
        """Return the engine this action belongs to."""
        return self.entity.gamemap.engine

    def perform(self) -> None:
        """
        Perform this action with the objects needed to determine its scope.

        `self.engine` is the scope this action is being performed in.

        `self.entity` is the object performing the action.

        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()