

def _should_attempt_c_optimizations():
    return (sys.implementation.name == 'pypy' and
            os.environ.get('PURE_PYTHON') != '1')
