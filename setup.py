import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="N-Back test",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[]}},
    executables = executables
)