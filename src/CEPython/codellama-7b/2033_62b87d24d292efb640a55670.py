

def get_versions():
    try:
        import subprocess
        output = subprocess.check_output(['git', 'describe', '--tags'])
        versions = output.decode().strip().split('\n')
        return versions
    except subprocess.CalledProcessError:
        return ['default']
