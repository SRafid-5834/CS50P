# File Extensions

def main():
    user_input = input("File name: ").lower().strip()
    print(find_extension(user_input))


def find_extension(ext):
    if ext.endswith(".jpg") or ext.endswith(".jpeg"):
        return "images/jpeg"
    elif ext.endswith(".gif"):
        return "image/gif"
    elif ext.endswith(".png"):
        return "image/png"
    elif ext.endswith(".pdf"):
        return "application/pdf"
    elif ext.endswith(".txt"):
        return "text/plain"
    elif ext.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


if __name__ == "__main__":
    main()
