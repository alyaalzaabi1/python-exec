def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) >= 2:
        return f"{parts[-1]}, {' '.join(parts[:-1])}"
    return full_name


name = input("Enter your full name: ")
print("Formatted:", format_name(name))
