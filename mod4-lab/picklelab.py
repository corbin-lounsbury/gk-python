import gzip
import pickle
from zipfile import ZipFile

zipContent = "Mitochondria is the powerhouse of the cell."
contentBytes = pickle.dumps(zipContent)


with gzip.open("gziptest.gz", "wb") as gfile:
    gfile.write(contentBytes)
gfile.close()

# with ZipFile("zipfiletest.zip",mode="w") as zfile:
#     zfile.write(contentBytes)

print(contentBytes)

contentText = pickle.loads(contentBytes)
print(contentText)