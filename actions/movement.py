from actions.direction import ActionWithDirection
import exceptions

from sound import sound_manager, impossible_sound

class MovementAction(ActionWithDirection):
    def perform(self) -> None:
        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            # Destination is out of bounds.
            sound_manager.play_sound(self.engine.sound_enabled, impossible_sound)
            raise exceptions.Impossible("That way is blocked.")
        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:
            # Destination is blocked by a tile.
            sound_manager.play_sound(self.engine.sound_enabled, impossible_sound)
            raise exceptions.Impossible("That way is blocked.")
        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            # Destination is blocked by an entity.
            sound_manager.play_sound(self.engine.sound_enabled, impossible_sound)
            raise exceptions.Impossible("That way is blocked.")

        self.entity.move(self.dx, self.dy)