def _group_files_by_xml_filename(source, xmls, files):
    import os
    xml_basename_to_filename = {}
    for xml in xmls:
        base = os.path.splitext(os.path.basename(xml))[0]
        xml_basename_to_filename[base] = xml

    grouped = {xml: [] for xml in xmls}

    for file in files:
        file_base = os.path.splitext(os.path.basename(file))[0]
        if file_base in xml_basename_to_filename:
            xml_filename = xml_basename_to_filename[file_base]
            grouped[xml_filename].append(file)

    return {xml: Package(files) for xml, files in grouped.items()}
