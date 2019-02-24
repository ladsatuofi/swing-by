# Swing-By: A ML community trust framework for intelligent event suggestion.
## Inspiration
As a group of Computer Science, Math, and Statistics majors, we have all have friends from different majors come to us asking about CS events on campus (that we’ve been sent by the CS Department). One thing that we agreed on was that events on campus are far from being consolidated enough into one platform.

Additionally, there are a variety of great events on campus, particularly from small organizations, that do not get the visibility that they are looking for, despite relevant interests from a large number of students. 

As a result, we felt that event information on campus needed balance; it needs to be both ubiquitous but also not spammy, and that’s where our data-driven approach to solving this problem comes from.

## What it Does 
Tackling the problem of on-campus events having low visibility, Swing-By takes a data-driven approach to community-based trust enablement, employing image recognition, natural language processing, and machine learning to share the most relevant on-campus events with students at UIUC and beyond.

The app allows users to let others know about on-campus events, while our intelligent platform helps to tag events and let relevant users know about their happenings. Relevance and credibility are ensured through Swing-By’s credibility system, through which community members can endorse or downvote event reports. Gradually, good players are able to gain credibility on our platform, while bad players have their opinions gradually silenced, as their credibility points decline.

## How We Built It / Technologies Used
For our backend system, we utilized a Redis database to store information including but not limited to the event objects that users submit, user identity information (including points, interactions, etc.), and other details pertaining to the interactions between community members and events happening on campus.

We wrote our relevance and credibility verification scripts in Python, additionally utilizing Tesseract and OpenCV for image recognition in order to scrape meeting dates, times, descriptions, and tags from sources such as email and image submissions. To buttress our OCR application, we used nltk and regular expressions, and applied the concepts of stopwords and tokenization to verify that key words that we parsed earlier indeed fit into one of our important categories used to define events on campus.

We wrote our frontend in JavaScript, specifically using React Native, for flexibility and adaptability to iOS and Android applications.
 
## Primary Technical Challenges 
The first challenge that we encountered was handling poorly-taken images from our users. That is, if our users submit a photo of an image, it would sometimes be difficult to read. We initially dealt with this issue with some resizing algorithm that we wrote, but later thought of applying a Gaussian blur to our images to remove noise prior to parsing.

Additionally, it was difficult to parse locations from text given a large number of locations and buildings on campus, and the large number of overlaps in location names at UIUC (e.g. Siebel Center for Design vs. for Computer Science). We gradually dealt with this problem through our tag-based system. For instance, a post with a Computer Science tag could be inferred to be located at the Siebel Center for Computer Science if any ambiguity were to arise. This, however, was much more than a simple regex issue, which we initially thought would be.

Another technical challenge that we faced, algorithmically, was the mathematical challenge of how we could calculate the authenticity of an event in a relatively short amount of time. Ultimately, after considering several options, we ended up choosing to store all the visitors’ identities in our Redis database, gathering the total number of potential likes given viewership, and calculating an arbitrary interval for which we believed would be reasonable in determining credibility.

Lastly, our team practically learned JavaScript through the duration of HackIllinois. React Native was new to us, and we definitely took a pretty large gamble in choosing it to be our framework over Android Studio, what we were all familiar with before.

## What’s Next for Swing By
We're planning on beta testing our product with a few thousand users, learn from their experiences, and train unsupervised learning models to revise users' interest tags over time to be more specific and targeted toward their true interests.

We're also in the process of writing a bot detection software, which detects irregularities in the amount of time logged in, the number of post interactions made in a short time span, etc.

In general, we're working towards making events geared towards any major or interest ubiquitous and consolidated information at UIUC and at all colleges across the United States.
