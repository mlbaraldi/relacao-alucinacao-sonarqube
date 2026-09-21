def _explore_folder(folder):
    import os
    from collections import defaultdict
    groups = defaultdict(list)
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            base = filename.split('.', 1)[0]
            groups[base].append(filename)
