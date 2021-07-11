
We have used both social media datasets(Fox news comments and Twitter) for transfer learning and also the movies Dataset made up of 6 hand picked movies.

### Twitter
It consists of 24,802 [Tweets](https://github.com/t-davidson/hate-speech-and-offensive-language/). We identified 204 of them as duplicates and removed them to achieve accurate training results. The corpus was labelled by CrowdFlower workers into 3 classes: **Hate speech, Offensive and Neither.**

### Fox News
The [Fox news corpus](https://github.com/sjtuprog/fox-news-comments) is publicly available. It consistsof 1,528 annotated comments whose sources are 10 discussion threads that happened on the FoxNews website in 2016. The corpus was annotated into **Normal** and **Hate speech** comments,thus for evaluation, we treated offensive classified movie subtitles in movies as hate. The comments are annotated by 2 trained native English speakers. We have identified 13 duplicates and 2 empty comments in this corpus and removed them for accurate training results.

### Novel Movie Dataset
The novel movie dataset we introduce consists of 6 movies. The movies have been chosen based on keyword tags provided by the [IMDB website](https://www.imdb.com/search/keyword/).The tags Hate-speech and racism were chosen because we assumed that they were likely to containa lot of hate and offensive speech. The tag friendship was chosen to get contrary movies contain-ing a lot of normal subtitles, with less hate speechcontent. In addition, we excluded movie genres like documentations, fantasy, or musicals to keep the movies comparable to each other. Namely we have chosen the movies BlacKkKlansman (2018) which was tagged as hate-speech, Django Un-chained (2012), American History X (1998) and Pulp Fiction (1994) which were tagged as racism whereas South Park (1999) as well as The Wolf of Wall Street (2013) were tagged as friendship in December 2020.
From the movie subtitles the utterances were scraped, cleaned and annotated bs Amazon MTurk workers. The annotated utterances  of all the movies are combined to a single file 'all_movies.csv'. Use this file to use the entire dataset of all the 6 movies. 

