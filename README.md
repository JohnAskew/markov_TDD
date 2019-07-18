# markov_TDD
Test driven design using Markov Chain.

The program markov.py will load a default text page (in our case, the 'pp.txt' file)
and will return a command line prompt waiting for you to enter a partial search string, 
from 1 to 4 characters. The intent is to find the string somewhere in the text and 
present back to the user the very next character to appear in the text file.

This might seem pointless, but the idea is to only introduce the concept of the Markov Chain,
while providing an introduction into Test Driven Design.

## Usage:
python markov.py -f <text_file_to_parse> -s <size_of_search_string (values = 1 to 4)
### Testing:
python test_markov.py

I suggest you review each module, but especially "test_markov.py" to
understand what tests are being conducted. Generally, this test driven
design is written first, knowing it will fail, as there is no code behind
it. Once the test program is completed and we have a series of fails, we
start to write the code, to satisfy only the first failed test. Once we 
have a test complete successfully, we start coding to satisfy the next 
test, and so on.
