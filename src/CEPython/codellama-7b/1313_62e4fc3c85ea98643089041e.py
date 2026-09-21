

def _inline_r_setup(code: str) -> str:
    # Set the R options for the current session
    code = f"options(repos = c(CRAN = 'https://cran.rstudio.com/')," \
           f"download.file.method = 'libcurl'," \
           f"download.file.method.libcurl = 'curl')"
    return code
