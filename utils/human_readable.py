def humanbytes(size):
    if not size:
        return ""
    
    size_in_mb = size / (1024 * 1024)  # Convert size to megabytes

    if size_in_mb < 1:
        # If size is less than 1 MB, round to the nearest 1 MB
        return f"{round(size_in_mb)}MB"
    elif size_in_mb < 1000:
        # If size is less than 1000 MB (1 GB), round to the nearest 10 MB
        rounded_size = round(size_in_mb, -1)
        return f"{int(rounded_size) if rounded_size.is_integer() else rounded_size}MB"
    else:
        # If size is 1000 MB or greater, round to the nearest 100 MB
        rounded_size_gb = round(size_in_mb / 10) / 100
        return f"{int(rounded_size_gb) if rounded_size_gb.is_integer() else rounded_size_gb:.2f}GB"
