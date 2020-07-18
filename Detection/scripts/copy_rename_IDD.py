import os
import shutil
import itertools


def move_or_copy(from_folders, dest_folder, doCopy=True):
    i = 0
    for folder in from_folders:
        all_files = []
        for root, _, files in itertools.islice(os.walk(folder), 1, None):
            for filename in files:
                all_files.append(os.path.join(root, filename))

        for filename in all_files:
            dest_name = os.path.join(dest_folder, f'{i}.jpg')
            print(f"\r{i} files transfered.", end="")
            if doCopy:
                shutil.copy(filename, dest_name)
            else:
                shutil.move(filename, dest_name)
            i += 1


def rename_IDD_data(folder):
    xml_files = sorted(
        [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.xml')])
    print(len(xml_files))
    jpg_files = sorted(
        [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.jpg')])
    print(len(jpg_files))

    jpg_files = []
    images_missing = []

    for idx, file in enumerate(xml_files):
        fname, _ = os.path.splitext(file)
        name = f'{fname}.jpg'
        if os.path.exists(name):
            jpg_files.append(name)
        else:
            images_missing.append(idx)

    for i in images_missing:
        xml_files.pop(i)

    assert len(xml_files) == len(
        jpg_files), "Different number of files present"

    for i, (xml, jpg) in enumerate(zip(xml_files, jpg_files), 1):
        xml_text_check = os.path.splitext(xml)[0]
        jpg_text_check = os.path.splitext(jpg)[0]
        assert xml_text_check == jpg_text_check, "File name doesn't match"
        jpg_filename = f'IDD_{i}.jpg'
        xml_filename = f'iDD_{i}.xml'
        os.rename(xml, xml_filename)
        os.rename(jpg, jpg_filename)


if __name__ == '__main__':
    src_folder = [
        'frontFar',
        'frontNear'
    ]
    dst_folder = input("Enter destination folder name: ")
    if not os.path.isdir(dst_folder):
        os.makedirs(dst_folder)

    # move_or_copy(src_folder, dst_folder, doCopy=True)
    rename_IDD_data('IDD_data')
