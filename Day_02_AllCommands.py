"""🚀 PLAYWRIGHT COMMANDS (Most Important)

🛠 INSTALLATION COMMANDS
Command	Use
pip install playwright	Install Playwright library
pip install pytest pytest-html	Install pytest + HTML report plugin
playwright install	Install all Playwright browsers
playwright install chromium	Install only Chromium
pytest --help	Show all pytest supported commands

🧪 BASIC PYTEST EXECUTION COMMANDS
Command	Use
pytest test_file.py	Run one test file
pytest -v	Verbose mode (show test names)
pytest -s	Show print statements in console
pytest -k "login"	Run only tests containing word login
pytest -m smoke	Run tests marked as @pytest.mark.smoke

🌍 RUN TESTS ON SPECIFIC BROWSER
Command	Use
pytest test.py --browser chromium	Run on Chromium
pytest test.py --browser firefox	Run on Firefox
pytest test.py --browser webkit	Run on Safari/WebKit
pytest test.py --browser chromium --headed	Run Chromium in headed mode
pytest test.py --browser chromium --headless	Run Chromium in headless mode

🌐 RUN TESTS ON MULTIPLE BROWSERS
Command	Use
pytest test.py --browser chromium --browser firefox --browser webkit	Run on all 3 browsers
pytest --browser chromium --browser firefox -v -s	Multi-browser test with logs
pytest test.py --browser chromium --browser firefox --headed	Multi-browser headed

🖥 HEADLESS / HEADED EXECUTION
Command	Use
pytest test.py --headed	Run browser with UI
pytest test.py --headless	Run without UI (default)

📄 HTML REPORTING
Command	Use
pytest --html=Report.html	Generate HTML report
pytest test.py --browser chromium --html=TestReport.html	Test + HTML report
pytest test.py --browser chromium --headed --html=ExecutionReport.html -v	Full test with report

Code Generator (Auto Script Recording)
Command	Use
playwright codegen https://www.facebook.com/	Open browser and auto-generate code
playwright codegen --target python https://google.com	Generate Python Playwright code
playwright codegen --device="iPhone 12"	

Video record
pytest test.py --browser chromium --video=on

B. Save video only for failures
pytest test.py --video=retain-on-failure

TAKE SCREENSHOTS
pytest test.py --browser chromium --screenshot=on

B. Save screenshots only for failures
pytest test.py --screenshot=only-on-failure

"""