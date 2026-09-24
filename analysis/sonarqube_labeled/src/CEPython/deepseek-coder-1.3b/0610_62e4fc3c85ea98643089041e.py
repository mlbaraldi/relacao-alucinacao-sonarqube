import subprocess


def _inline_r_setup(code: str) -> str:
    """
    Some behaviour of R cannot be configured via env variables, but can
    only be configured via R options once R has started. These are set here.
    """
    # Create a temporary file to store the R code
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(code.encode())

    # Run the R script using subprocess
    result = subprocess.run(['Rscript', temp.name], capture_output=True, text=True)

    # Check the result
    if result.returncode != 0:
        raise Exception(f'R script failed with error: {result.stderr}')

    return result.stdout
