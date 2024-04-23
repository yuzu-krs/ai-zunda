import random
from obs_adapter import OBSAdapter
from voicevox_adapter import VoicevoxAdapter
#from openai_adapter import OpenAIAdapter
#LLMモデル
from llm_adapter import LLMAdapter

from youtube_comment_adapter import YoutubeCommentAdapter
from play_sound import PlaySound
from dotenv import load_dotenv
load_dotenv()
import os

class AITuberSystem:
    def __init__(self) -> None:
        video_id = os.getenv("YOUTUBE_VIDEO_ID")
        self.youtube_comment_adapter = YoutubeCommentAdapter(video_id)
        self.llm_adapter=LLMAdapter()
        self.voice_adapter = VoicevoxAdapter()
        self.obs_adapter = OBSAdapter()
        self.play_sound = PlaySound(output_device_name="CABLE Input (VB-Audio Virtual C")
        pass

    def talk_with_comment(self) -> bool:
        print("コメントを読み込みます…")
        comment = self.youtube_comment_adapter.get_comment()
        if comment==None:
            print("コメントがありませんでした。")
            return False
        response_text = self.llm_adapter.create_chat(comment)
        data,rate = self.voice_adapter.get_voice(response_text)
        self.obs_adapter.set_question(comment)
        self.obs_adapter.set_answer(response_text)
        self.play_sound.play_sound(data,rate)
        return True