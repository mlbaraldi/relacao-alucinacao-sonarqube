

def _group_files_by_xml_filename(source, xmls, files):
    # Create a dictionary to store the grouped files
    grouped_files = {}

    # Loop through each XML filename
    for xml_filename in xml_filenames:
        # Get the basename of the XML filename
        xml_basename = os.path.basename(xml_filename)

        # Create a list to store the files that match the XML basename
        matching_files = []

        # Loop through each file in the list of files
        for file in files:
            # Check if the file matches the XML basename
            if os.path.basename(file) == xml_basename:
                # Add the file to the list of matching files
                matching_files.append(file)

        # Add the list of matching files to the dictionary
        grouped_files[xml_basename] = matching_files

    # Return the dictionary of grouped files
    return grouped_files
