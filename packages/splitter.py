from loaders import load_directories  # Importing the load_documents function from loaders.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_text_splitters import CharacterTextSplitter  
def recursive_splitter(documents):
    recursive_text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=10,
        length_function=len,
        add_start_index=True
    )
    return recursive_text_splitter

    #there should be return statement, should be an option to input chunk size and chunk overlap in api

    # character_text_splitter = CharacterTextSplitter(
    #     separator="\n\n",
    #     chunk_size=1000,
    #     chunk_overlap=200,
    #     length_function=len,
    #     is_separator_regex=False,
    # )
    chunks = recursive_text_splitter.split_documents(documents=documents)   #comes in nb   
    print("First chunk \n:",chunks[0],"\n\n")
    print("Second Chunk \n:",chunks[1],"\n\n")
    print("third Chunk \n:",chunks[2],"\n\n")
    # print("Length of chunks:",len(chunks),"\n\n")



if __name__ == "__main__":
    documents = load_directories()

    recursive_splitter(documents)
