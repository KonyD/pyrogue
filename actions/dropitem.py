from actions.item import ItemAction

from sound import sound_manager, drop_sound

class DropItem(ItemAction):
    def perform(self) -> None:
        if self.entity.equipment.item_is_equipped(self.item):
            self.entity.equipment.toggle_equip(self.item)
         
        self.entity.inventory.drop(self.item)
        sound_manager.play_sound(self.engine.sound_enabled, drop_sound)