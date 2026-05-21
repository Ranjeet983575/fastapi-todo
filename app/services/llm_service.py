from groq import Groq
from app.services.config import Config


class LLService:
    
        def __init__(self, config: Config = None):
                self.config = config or Config()
                
                self.api_key = self.config.groq_api_key
                self.model = self.config.groq_model
                self.client = Groq(api_key=self.api_key)
            
            
        def ask_with_context(self, question: str, context: str) -> str:
            if not self.api_key:
                raise ValueError("GROQ_API_KEY environment variable not set.")
            
            prompt = f"Context: {context}\n\nQuestion: {question}"
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
            )
            return chat_completion.choices[0].message.content
        

        def ask(self, question: str) -> str:
            if not self.api_key:
                raise ValueError("GROQ_API_KEY environment variable not set.")
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                model=self.model,
            )
            return chat_completion.choices[0].message.content
