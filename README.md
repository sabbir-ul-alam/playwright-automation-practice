# playwright-automation-practice

# to run all the tests under a test file
`pytest <file_name>`

# to run a single test under a test file
`pytest <file_name>::<test_name>`

# when running in a head mode
by default pytest will run the tests in headless mode
`pytest <file_name> --headed`

# codegen with playwright
`playwright codegen <url>`

# to see screenshot and trace
`pytest --tracing on`

`playwright show-trace .\trace.zip`

# run with env from powershell
`$env:ENV="stg"; pytest tests/test_e2e.py`

# generate html report
 `pytest --html=report.html --self-contained-html`
if no env is set from cmd, then it will read from .env file

# to generate requirement.txt
`pip freeze > requirements.txt`
or
`pipreqs . --force`
