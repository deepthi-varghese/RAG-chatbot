import os
from langchain_community.document_loaders import DirectoryLoader
from dotenv import load_dotenv

load_dotenv()

# Load GOOGLE API KEY stored in environment variable 'GOOGLE_API_KEY'
google_api_key = os.getenv("GOOGLE_API_KEY")



# Path to the data
DATA_PATH = r"data\all_files"



#till here should be moved to anothe rfile. data path should be given by user

def load_directories(): #have the user input data path
    loader = DirectoryLoader(DATA_PATH, glob="*.*")
    # documents = loader.load()

    return loader   #just return loader not the docs
# documents = load_directories()

# if __name__ == "__main__":
#     documents = load_directories()
#     for doc in documents:
#         file_name = doc.metadata.get('source', '').split('\\')[-1]  # Get the file name from metadata
#         print("File name:", file_name)



#create 3 loader - md,pdf, directory