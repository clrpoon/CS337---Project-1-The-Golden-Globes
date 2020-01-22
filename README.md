# CS337-Project-1-The-Golden-Globes

Project Deliverables:

All code must be in Python 3. You can use any Python package or NLP toolkit, but please save and share your requirements, i.e., create an environment for the project, run "pip freeze > requirements.txt" before submitting, and include this "requirements.txt" in your submission/repository.
You must use a publicly accessible repository such as Github, and commit code regularly. When pair programming, note in the commit message those who were present and involved. We use these logs to verify complaints about AWOL teammates, and to avoid penalizing the entire group for one student’s violation of academic integrity. We don’t look at the commits unless there’s something really wrong with the code, or there’s a complaint.
Please use the Python standard for imports described here:https://www.python.org/dev/peps/pep-0008/#imports (Links to an external site.) (Links to an external site.)
Bundle all your code together, your submission will be a .zip file on canvas.
If you use a DB, it must be Mongo DB, and you must provide the code you used to populate your database.
Your code must be runnable by the TA: Include a readme.txt file with instructions on what file(s) to run, what packages to download / where to find them, how to install them, etc and any other necessary information. The readme should also include the address for your Github repository.
Your code must run in a reasonable amount of time. Your grade will likely be impacted if this is greater than 10 minutes.
Your code cannot rely on a single Twitter user for correct answers. Particularly, the official Golden Globes account.
 

Minimum Requirements:

Fulfilling only the minimum requirements puts your group on track for a B

A project must do a reasonable job identifying each of these components.

Host(s) (for the entire ceremony)
Award Names
Presenters, mapped to awards*
Nominees, mapped to awards*
Winners, mapped to awards*
* These will default to using a hardcoded list of the awards to avoid penalizing you for cascading error.

It is OK not to have 100% accuracy on some of these components. It's very rare for any group not to have some error, especially with nominees. Even getting just half of the nominees for a given award is quite good performance.

Additional Goals:

To get better than a B, you must do exceptionally well on the minimum requirements, or complete one or more additional goals. Some examples of additional goals:

Red carpet – For example, determine who was best dressed, worst dressed, most discussed, most controversial, or perhaps find pictures of the best and worst dressed, etc.
Humor – For example, what were the best jokes of the night, and who said them?
Parties – For example, what parties were people talking about the most? Were people saying good things, or bad things?
Sentiment – What were the most common sentiments used with respect to the winners, hosts, presenters, acts, and/or nominees?
Acts – What were the acts, when did they happen, and/or what did people have to say about them?
Your choice – If you have a cool idea, suggest it to the TA! Ideas that will require the application of NLP and semantic information are more likely to be approved.
Typical performance on the minimum requirements, plus a well-done additional goal, is likely to earn an A- or better.

Required Output Format:

You are required to output your results in two different formats.

A human-readable format. This is where your additional goals output happens. For example:
Host: Seth Meyers

Award: Best Motion Picture - Drama
Presenters: Barbara Streisand
Nominees: “Three Billboards Outside Ebbing, Missouri”, "Call Me by Your Name", "Dunkirk", "The Post", "The Shape of Water"
Winner: “Three Billboards Outside Ebbing, Missouri”

Best Dressed: Jane Doe
Worst Dressed: John Doe
Most Controversially Dressed: John Smith
A JSON format compatible with the autograder (to be provided shortly); this is only containing the information for the minimum tasks. For example:
{

"Host" : "Seth Meyers",

 

"Best Motion Picture - Drama" : {

"Presenters" : ["Barbra Streisand"],

"Nominees" : ["Three Billboards Outside Ebbing, Missouri", "Call Me by Your Name", "Dunkirk", "The Post", "The Shape of Water"],

"Winner" : "Three Billboards Outside Ebbing, Missouri"

},

 

"Best Motion Picture - Musical or Comedy" : {

"Presenters" : ["Alicia Vikander", "Michael Keaton"],

"Nominees" : ["Lady Bird", "The Disaster Artist", "Get Out", "The Greatest Showman", "I, Tonya"],

"Winner" : "Lady Bird"

},

 

The Data:

Uploaded to canvas -> Files -> Project 1-> gg2020.zip

 

[{u'id': 554402424728072192, u'text': u'just had to scramble to find a golden globes stream for my brother. :D', u'user': {u'id': 19904553, u'screen_name': u'baumbaTz'}, u'timestamp_ms': u'1421014813011'}, {"text": "What?!? https://t.co/NSPtGtbCvO", "id_str": "950142397194821632"}, ...

]

 

Tweets for 2020 were collected if they matched the query
"golden globe OR golden globes OR goldenglobes OR goldenglobe OR gg2020 OR globe OR globes OR goldenglobes2020 -filter:retweets"
You will be graded on at least one year you have not seen (e.g., 2019, 2018).
