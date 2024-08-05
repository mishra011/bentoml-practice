
import bentoml

with bentoml.SyncHTTPClient('http://localhost:3000') as client:
    text_to_summarize: str = input("Enter text to summarize: ")
    summarized_text: str = client.summarize([text_to_summarize])[0]
    print(f"Summarized text: {summarized_text}")


