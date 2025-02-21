from actions.baseaction import Action
from entities.actor import Actor
from entities.item import Item

from sound import sound_manager, equip_sound

class EquipAction(Action):
    def __init__(self, entity: Actor, item: Item):
        super().__init__(entity)

        self.item = item

    def perform(self) -> None:
        self.entity.equipment.toggle_equip(self.item)
        sound_manager.play_sound(self.engine.sound_enabled, equip_sound)