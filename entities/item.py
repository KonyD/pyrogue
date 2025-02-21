from typing import Optional, Tuple
from render_order import RenderOrder

from components.consumable import Consumable
from entities.entity import Entity
from components.equippable import Equippable

class Item(Entity):
    def __init__(
        self,
        *,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        consumable: Consumable = None,
        equippable: Optional[Equippable] = None,
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            name=name,
            blocks_movement=False,
            render_order=RenderOrder.ITEM,
        )

        self.consumable = consumable
        
        if self.consumable:
            self.consumable.parent = self
        
        self.equippable = equippable

        if self.equippable:
            self.equippable.parent = self