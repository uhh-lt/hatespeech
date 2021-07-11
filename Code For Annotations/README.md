# Annotations of the movie subtitles

The annotation of the movie subtitles were performed using Amazon Mechanical Turk(MTurk) crowd sourcing workers. The novel movie dataset we introduce consists of 6 movies. The movies have been chosen based on keyword tags provided by the [IMDB website](https://www.imdb.com/search/keyword/). The .srt files for the 6 movies are collected from [Open Subtitles online subtitles platform](https://www.opensubtitles.org/en/search/subs). The downloaded subtitles had a timestamp beside each dialogues/utterances. We performed the following operations to create the movie dataset:
1. Converted the SRT-format to CSV-format by separating start time, end time, and the subtitle text.
2. Fragmented subtitles which were originally single appearances on the screen and spanned across multiple screen frames were combined, by identifying sentence ending punctuation marks.
3. Combined single word subtitles with the previous subtitle because single word subtitles tend to be expressions and extension of the dialogue that has been said before.

Sound expressions,e.g [PEOPLE CHATTERING], [DOOR OPENING], (2) name header of the current speaker, e.g."DIANA: Hey, what’s up?" which refers to Diana is about to say something, HTML tags, non-alpha character subtitle, and non-ASCII characters.

Finally the movie datasets in ./CSV$ folder is used for the annotation task. Before the main annotation task, we have conducted an annotation pilot study, where 40 subtitles texts were randomly chosen from the movie subtitle dataset. Each of them has included 10 hate speech, 10 offensive, and 20 normal sub-titles that are manually annotated by experts.Each worker was assessed for accuracy and the 13 workers who have completed the task with the highest annotation accuracy were chosen for the main study task of annotating all the 6 movies.
The HTML template provided to the MTurk workers for annotation is as below
x-special/nautilus-clipboard
copy

![html_template](https://user-images.githubusercontent.com/2795092/125208975-10d07200-e296-11eb-9d26-e57aef079e4e.jpeg)
