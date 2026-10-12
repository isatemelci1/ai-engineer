def main():
    filename = input("File name: ").strip().lower()
    print(get_media_type(filename))


def get_media_type(filename):
    if filename.endswith(".gif"):
        return "image/gif"
    elif filename.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".pdf"):
        return "application/pdf"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


if __name__ == "__main__":
    main()