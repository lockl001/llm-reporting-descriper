import os
import json
from pathlib import Path
from pprint import pprint

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import JSONLoader


OLLAMA_MODEL = "llama2"

prompt_template = """
    Pretend to be a administrator of Pure, a system created by Elsevier, 
    that wants to write a description to a table element with the title 
    “Most used journals by related outputs”, and write what filters are used by the related dataset from datasets 
    in the following JSON context.
    {context}

    Output:
"""
file_path='./data/Publication overview - last 3 years (2).json'
data = json.loads(Path(file_path).read_text())

#pprint(data)

loader = JSONLoader(
     file_path=file_path,
    jq_schema='.',
    text_content=False

)
data = loader.load()

pprint(data)
print(len(data))
#prompt = ChatPromptTemplate.from_template(prompt_template)
#llm = Ollama(model=OLLAMA_MODEL)
#chain = create_stuff_documents_chain(llm, prompt)

#print(chain.invoke({"context": data}))