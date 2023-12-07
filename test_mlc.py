import os
import unittest

from mlc_chat import ChatModule
from mlc_chat.callback import StreamToStdout, StreamIterator

from threading import Thread

class TestMLC(unittest.TestCase):
    def get_llama_model(self):
        arch = os.uname().machine
        if arch == 'x86_64':
            return "Llama-2-7b-chat-hf-q4f16_1-metal_x86_64"
        elif arch == 'arm64':
            return "Llama-2-7b-chat-hf-q4f16_1"
        else:
            raise Exception(f'Unknown architecture: {arch}')
    
    def test_llama(self):
        model = self.get_llama_model()
        cm = ChatModule(model=model)
        
        prompt = "What is the meaning of life?"
        
        stream = StreamIterator(callback_interval=2)
        
        generation_thread = Thread(target=cm.generate,
            kwargs={
                "prompt" : prompt,
                "progress_callback" : stream
            })
        
        generation_thread.start()
            
        output = ""
            
        for delta_message in stream:
            output += delta_message
                
        generation_thread.join()
        
        #print(f"Statistics: {cm.stats()}\n")
        self.assertTrue("Epicurean Perspective" in output, msg="Check generated result")
        
if __name__ == '__main__':
    unittest.main()
