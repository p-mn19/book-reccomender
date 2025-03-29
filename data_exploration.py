import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("dylanjcastillo/7k-books-with-metadata")
books = pd.read_csv(f"{path}/books.csv")
print(books)