from voicevox_adapter import VoicevoxAdapter
from play_sound import PlaySound

input_str = "こんにちは、僕はずんだもんなのだ。"
voicevox_adapter = VoicevoxAdapter()
play_sound = PlaySound("DELL S2722QC (NVIDIA High Defin")
data, rate = voicevox_adapter.get_voice(input_str)
play_sound.play_sound(data, rate)