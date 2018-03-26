# InstacartShopperChallenge
## Part 1:

I used Python's flask simple web server.  In order to run it you will need:
- Python 3.X
- flask (pip install flask)

You can run it by using the following two commands on the command line:
set FLASK_APP=InstacartFlaskServer.py
flask run

Alternatively, you can run it from the python shell:
set FLASK_APP=InstacartFlaskServer.py
python -m flask run

The server will be running on:
http://127.0.0.1:5000/

I used Twitter Bootstrap 4 as a basis to create the front end.  It is pretty rough
and I did not get a chance to test as much as I wanted to, but it is mostly there.
I used the Cover template to start as I thought it looked nice and fit the
requirements well enough.


## Part 2:

I used Python again for part 2.  In order to run my script you will need:
- Python 3.X
- sqlite3 (pip install sqlite3)
- dateutil (pip install python-dateutil)

You can run with the following command:
python Query.py start_date end_date

I tried two different query methods.  The first was running a query per week and
using the GROUP BY keyword to do the heavy lifting for me.  I then printed out
the results returned from each query.  For my testing, this seemed to be a faster
query so I chose to go with this for my final submission.
The second option I tried was a single query and then I parsed the results and
built the result sets in python.  This, based on the profiler was slower.  I did
not try to run larger or smaller data set sizes to see how that impacted each
option.

### License:
I have not attributed a license to this project.  I am not sure what License
Instacart may require for a project like this.  As soon as I get Confirmation
from them I will update the license.
