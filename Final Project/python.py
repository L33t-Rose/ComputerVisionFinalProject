# import os
# import shutil

# # Source and destination directories
# source_directory = r"C:/Users/alexs\Downloads/Original X-ray 48 month/test"
# destination_directory = r"C:/Users/alexs/Desktop/Final Project/datasets/images/test"

# # Iterate through folders in the source directory
# for folder_name in os.listdir(source_directory):
#     folder_path = os.path.join(source_directory, folder_name)

#     # Check if the item in the directory is a folder
#     if os.path.isdir(folder_path):
#         # Look for the v06 folder inside each subdirectory
#         v06_folder_path = os.path.join(folder_path, 'v06')

#         # Check if the v06 folder exists
#         if os.path.exists(v06_folder_path):
#             # Find the jpg file inside the v06 folder
#             jpg_file_path = os.path.join(v06_folder_path, '001.jpg')

#             # Check if the jpg file exists
#             if os.path.exists(jpg_file_path):
#                 # Create the destination directory if it doesn't exist
#                 os.makedirs(destination_directory, exist_ok=True)

#                 # Construct the destination file path with the folder name
#                 destination_file_path = os.path.join(destination_directory, f'{folder_name}.jpg')

#                 try:
#                     # Copy the jpg file to the destination directory
#                     shutil.copy(jpg_file_path, destination_file_path)
#                     print(f'Successfully copied {jpg_file_path} to {destination_file_path}')
#                 except Exception as e:
#                     print(f'Error copying {jpg_file_path}: {e}')

#             else:
#                 print(f'Error: {jpg_file_path} not found in {v06_folder_path}')

# # Script completed
# print('Script execution completed.')

# import os

# # Source directory containing TXT files
# source_directory = r'C:/Users/alexs\Desktop/Final Project/datasets/labels/test'

# # Iterate through files in the source directory
# for file_name in os.listdir(source_directory):
#     file_path = os.path.join(source_directory, file_name)

#     # Check if the item in the directory is a file and ends with ".txt"
#     if os.path.isfile(file_path) and file_name.endswith('.txt'):
#         # Get the file name without extension
#         file_name_without_extension = os.path.splitext(file_name)[0]

#         # Remove the "_v06" part and construct the new file name
#         new_file_name = file_name_without_extension.replace('_v06', '')

#         # Construct the destination file path with the new file name
#         new_file_path = os.path.join(source_directory, f'{new_file_name}.txt')

#         try:
#             # Rename the file
#             os.rename(file_path, new_file_path)
#             print(f'Successfully renamed {file_path} to {new_file_path}')
#         except Exception as e:
#             print(f'Error renaming {file_path}: {e}')

# # Script completed
# print('Script execution completed.')


# def normalize(value, max_value):
#     return value / max_value

# def process_txt_files(directory_path):
#     for filename in os.listdir(directory_path):
#         if filename.endswith(".txt"):
#             txt_file_path = os.path.join(directory_path, filename)
#             process_single_txt_file(txt_file_path)

# def process_single_txt_file(txt_file_path):
#     with open(txt_file_path, 'r') as file:
#         lines = file.readlines()

#     image_width, image_height = get_image_dimensions(txt_file_path)

#     with open(txt_file_path, 'w') as file:
#         for line in lines:
#             if line.strip():
#                 parts = line.split()
#                 joint_name = parts[0]
#                 x = normalize(float(parts[1]), image_width)
#                 y = normalize(float(parts[2]), image_height)
#                 deg = float(parts[3])
#                 normalized_width = normalize(0.1, image_width)  # Change 0.1 to your desired width
#                 normalized_height = normalize(0.1, image_height)  # Change 0.1 to your desired height

#                 file.write(f'{joint_name} {x} {y} {deg} {normalized_width} {normalized_height}\n')

# def get_image_dimensions(txt_file_path):
#     image_filename = os.path.splitext(os.path.basename(txt_file_path))[0] + '.jpg'
#     image_path = os.path.join(os.path.dirname(txt_file_path), image_filename)

#     # Get image dimensions
#     with open(image_path, 'rb') as img_file:
#         from PIL import Image
#         image = Image.open(img_file)
#         image_width, image_height = image.size

#     return image_width, image_height

# # Example usage:
# directory_path = 'path/to/your/directory'  # Replace with the actual path to your directory
# process_txt_files(directory_path)

# from PIL import Image

# class_mapping = {
#     'mcp2': 0,
#     'pip2': 1,
#     'dip2': 2,
#     'mcp3': 3,
#     'pip3': 4,
#     'dip3': 5,
#     'mcp4': 6,
#     'pip4': 7,
#     'dip4': 8,
#     'mcp5': 9,
#     'pip5': 10,
#     'dip5': 11
# }

# # Replace 'path_to_images' with the actual path to your images directory
# path_to_images = "C:/Users/alexs/Desktop/Final Project/datasets/images/train"

# # Replace 'path_to_labels' with the actual path to your labels directory
# path_to_labels = "C:/Users/alexs/Desktop/Final Project/datasets/labels/train"

# def get_image_dimensions(image_path):
#     with Image.open(image_path) as img:
#         return img.size

# # Step 1: Create new files with "_yolo" suffix
# for filename in os.listdir(path_to_labels):
#     if filename.endswith('.txt'):
#         label_path = os.path.join(path_to_labels, filename)
#         image_path = os.path.join(path_to_images, filename.replace('.txt', '.jpg').replace('\\', '/'))

#         img_width, img_height = get_image_dimensions(image_path)

#         with open(label_path, 'r') as label_file:
#             lines = label_file.readlines()

#             yolo_labels = []
#             for line in lines:
#                 # Skip lines starting with 'q'
#                 if line.startswith('q'):
#                     continue

#                 parts = line.split()
#                 if len(parts) >= 3:  # Ensure at least 3 elements in a row (name, x, y)
#                     joint_name = parts[0]
#                     x_center = float(parts[1]) / img_width
#                     y_center = float(parts[2]) / img_height

#                     # Example: Convert width and height to be around 150 by 200 pixels
#                     pixel_width = 200
#                     pixel_height = 200

#                     # Normalize width and height to be between 0 and 1 based on the original image size
#                     normalized_width = pixel_width / img_width
#                     normalized_height = pixel_height / img_height

#                     class_index = class_mapping[joint_name]

#                     yolo_labels.append(f"{class_index} {x_center} {y_center} {normalized_width} {normalized_height}")
#                 else:
#                     print(f"Warning: Skipping line due to insufficient elements: {line.strip()}")

#             # Save the YOLO labels to a new file
#             yolo_label_path = os.path.join(path_to_labels, filename.replace('.txt', '_yolo.txt'))
#             with open(yolo_label_path, 'w') as yolo_label_file:
#                 yolo_label_file.write('\n'.join(yolo_labels))

# # Step 2: Delete old files and rename new files
# for filename in os.listdir(path_to_labels):
#     if filename.endswith('.txt'):
#         label_path = os.path.join(path_to_labels, filename)
#         yolo_label_path = os.path.join(path_to_labels, filename.replace('.txt', '_yolo.txt'))

#         if os.path.exists(yolo_label_path):
#             # If the "_yolo" version exists, delete the original file and rename the new file
#             os.remove(label_path)
#             os.rename(yolo_label_path, os.path.join(path_to_labels, filename))


# from PIL import Image
# import os
# import time

# def delete_images_with_large_width(folder_path, max_width):
#     for filename in os.listdir(folder_path):
#         if filename.endswith(('.jpg', '.jpeg', '.png')):
#             image_path = os.path.join(folder_path, filename)
#             try:
#                 with Image.open(image_path) as img:
#                     width, _ = img.size
#                     if width > max_width:
#                         os.remove(image_path)
#                         print(f"Deleted: {filename}")
#             except Exception as e:
#                 print(f"Error processing {filename}: {e}")
#                 # If the file is in use, try renaming the file and then deleting it
#                 try:
#                     renamed_path = image_path + "_renamed"
#                     os.rename(image_path, renamed_path)
#                     os.remove(renamed_path)
#                     print(f"Deleted (renamed): {filename}")
#                 except Exception as e:
#                     print(f"Failed to delete {filename} (renamed): {e}")

# # Example usage:
# folder_path = "C:/Users/alexs/Desktop/Final Project/datasets/images/train"  # Replace with the actual path to your image folder
# max_width = 2000  # Set the maximum width threshold

# delete_images_with_large_width(folder_path, max_width)

# import os

# def filter_txt_files(txt_folder, image_folder):
#     txt_files = [f for f in os.listdir(txt_folder) if f.endswith('.txt')]

#     for txt_file in txt_files:
#         image_name = os.path.splitext(txt_file)[0] + '.jpg'
#         image_path = os.path.join(image_folder, image_name)

#         if os.path.exists(image_path):
#             print(f"Keeping: {txt_file}")
#         else:
#             txt_path = os.path.join(txt_folder, txt_file)
#             os.remove(txt_path)
#             print(f"Deleted: {txt_file}")

# # Example usage:
# txt_folder = 'C:/Users/alexs/Desktop/Final Project/datasets/labels/train'  # Replace with the actual path to your txt folder
# image_folder = 'C:/Users/alexs/Desktop/Final Project/datasets/images/train'  # Replace with the actual path to your image folder

# filter_txt_files(txt_folder, image_folder)





