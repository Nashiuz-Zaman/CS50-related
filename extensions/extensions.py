def main():
    file_name = normalize_string(input("File name: "))
    file_extension = find_extension(file_name)

    match file_extension:
        case ".gif":
            print("image/gif")
        case ".jpg" | ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


def normalize_string(str):
    return str.strip().lower()


def find_extension(file_name):
    if file_name.endswith(".gif"):
        return ".gif"
    elif file_name.endswith(".jpg"):
        return ".jpg"
    elif file_name.endswith(".jpeg"):
        return ".jpeg"
    elif file_name.endswith(".png"):
        return ".png"
    elif file_name.endswith(".pdf"):
        return ".pdf"
    elif file_name.endswith(".txt"):
        return ".txt"
    elif file_name.endswith(".zip"):
        return ".zip"
    else:
        return "unknown"


main()
