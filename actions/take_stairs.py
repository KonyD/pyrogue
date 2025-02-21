from actions.baseaction import Action
import color
import exceptions

from sound import sound_manager, next_level_sound

class TakeStairsAction(Action):
    def perform(self) -> None:
        """
        Take the stairs, if any exist at the entity's location.
        """
        if (self.entity.x, self.entity.y) == self.engine.game_map.downstairs_location:
            self.engine.game_world.generate_floor()
            self.engine.message_log.add_message(
                "You descend the staircase.", color.descend
            )
            sound_manager.play_sound(self.engine.sound_enabled, next_level_sound)
        else:
            raise exceptions.Impossible("There are no stairs here.")