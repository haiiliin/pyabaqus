from pathlib import Path

cwd = Path.cwd()


def process_dir(a_path: Path):
    if (a_path.is_file()):
        if (a_path.name == "__init__.py"):
            empty = False
            with open(a_path, 'r') as fin:
                contents = fin.read().strip()
                empty = len(contents) <= 0 or "# Import Processed" in contents

            if (empty):
                with open(a_path, 'w') as fout:
                    fout.write("from typing import Dict, Tuple, List, Union\n")
                    fout.write("COORDINATE_3D = Tuple[float, float, float]\n")
                    fout.write("# Import Processed")
            else:
                with open(a_path, 'a') as fout:
                    fout.write("from typing import Dict, Tuple, List, Union\n")
                    fout.write("COORDINATE_3D = Tuple[float, float, float]\n")
                    fout.write("# Import Preserved")

    else:
        for sub_path in a_path.iterdir():
            process_dir(sub_path)


process_dir(cwd)