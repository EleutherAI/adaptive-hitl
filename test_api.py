from backend.pipeline.text_captions import TextCaptionPipeline
from backend.client.text_captions import TextCaptionClient
from backend.api import CHEESE

from datasets import load_from_disk

if __name__ == "__main__":
    cheese = CHEESE(
        TextCaptionPipeline, client_cls = TextCaptionClient, 
        pipeline_kwargs={"read_path": "dataset", "write_path": "data_res", "force_new": True}
    )

    url = cheese.create_client(1)
    print(url)

    # Test to make sure this showed up in the final dataset
    #res_dataset = load_from_disk("data_res")
    #print(res_dataset["text"])
    #print(res_dataset["captions"])
    #print(res_dataset["caption_index"])
    #print(res_dataset["id"])