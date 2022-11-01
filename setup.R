library(reticulate)
# library(devtools)
venv_path = '/home/rstudio/projects/tercen_python_test/venv'
use_virtualenv(venv_path, required=TRUE)
reticulate::repl_python()


# py_install(
#   "git+https://github.com/tercen/tercen_python_client.git",  
#   pip=TRUE
# )


config <- reticulate::py_config()
system2(config$python, c("-m", "pip", "install", "--force-reinstall", shQuote("/home/rstudio/projects/tercen_python_client/")))



py_install(envname = venv_path,
  packages="git+https://github.com/tercen/pytson@1.0",
   force=TRUE, pip_ignore_installed=TRUE, pip=TRUE
)


py_install(packages = "pandas",
           envname = venv_path,
           force=TRUE, pip_ignore_installed=TRUE, pip=TRUE
)



