import tcod.sdl.audio
import soundfile as sf
import numpy as np

class SoundManager:
    def __init__(self):
        """Initialize the sound playback device."""
        self.device = tcod.sdl.audio.open()

    def load_sound(self, filename: str) -> np.ndarray:
        """Load a sound file as a NumPy array."""
        filepath = f"sound/{filename}.wav"
        data, _ = sf.read(filepath, dtype="float32")
        return data

    def play_sound(self, sound_enabled: bool, sound_data: np.ndarray) -> None:
        """Play a sound if enabled."""
        if sound_enabled:
            self.device.queue_audio(sound_data)  # Play sound asynchronously

# Global instance (can be used across files)
sound_manager = SoundManager()

# Preload sounds
pickup_sound = sound_manager.load_sound("pickup")
equip_sound = sound_manager.load_sound("equip")
drop_sound = sound_manager.load_sound("dropItem")
death_sound = sound_manager.load_sound("death")
hit_hurt_sound = sound_manager.load_sound("hitHurt")
power_up_sound = sound_manager.load_sound("powerUp")
next_level_sound = sound_manager.load_sound("next_level")
blip_sound2 = sound_manager.load_sound("blipSelect2") 
blip_sound = sound_manager.load_sound("blipSelect") 
explosion_sound = sound_manager.load_sound("explosion")
error_sound = sound_manager.load_sound("error")
impossible_sound = sound_manager.load_sound("impossible")