# 100 Ranked Trigram Parser

As a challenge, this tool was written to parse large amounts of text and subsequently output the top 100 most frequent trigrams that are found. 

in linguisitics, a trigram is defined as "a group of three consecutive written units such as letters, syllables, or words."

ngrams.py works by implementing a deque to efficiently parse every word in a given corpus or set thereof, and creating a collection of tuples containing frequency and set information, which is stored in a dict as the value for the key N which is the variable sequence length to match on.

Currently ngrams.py only supports python3, however with small efforts could be made doubly compatible. 

## Installing

The service only uses the Python Standard Library, so no installation efforts are needed.
If you wish to run the Dockerfile, see [Docker's instructions on how to get started here](https://docs.docker.com/get-started/)


## Basic Usage

`$ python ngrams.py corpus.txt`


Additionally, I support multiple file inputs and piping input from stdin:

`$ python ngrams.py file1.txt file2.txt filen.txt...`


`$ cat file.txt | python ngrams.py`


## Output and Functionality

An example out put using one of the sample corpi I've provided would look like so:

```$ python ngrams.py tests/kjb.txt
Ranked 100 ocurring 3-grams:
of the lord - 1742
the son of - 1450
the children of - 1355
the house of - 883
saith the lord - 854
out of the - 805
and i will - 672
```

Implying that past the header, the data is read as `tri-gram - frequency`

If given multiple files, the program will collapse them and treat all inputs as one corpus:

```$ python ngrams.py tests/kjb.txt tests/exodus.txt
Ranked 100 ocurring 3-grams:
of the lord - 1766
the son of - 1454
the children of - 1422
the house of - 885
saith the lord - 863
out of the - 826
children of israel - 709
```

If this is undesired functionality, it would be simple to run the script multiple times for comparative results. For future release discussion, see section below.

## Testing

I've provided a test suite for verifying various functionalities of the client requirements. For sake of speed and ease for functional testing like I've implemented, I've implemented `pytest` module. In order to get started:

# Install

`pip install -U pytest`

# Invoke

I prefer lazy invocation as such from the root of the project:

`python -m pytest -v`

But as expected, you may invoke pytest however you're most comfortable.

## Docker

This repo has been supplied with a Dockerfile so you can quickly run this application in a docker image. To do so, make sure you have docker installed and then from the root of the repo run the following:

`$ docker build -t your_image_name .`
`$ docker run your_image_name`

And Voila! You've ran this wonderful code in a docker container. For further details on docker capabilities and uses, I recommend checking out [their site](https://docs.docker.com/get-started/) for more information.

# Runtime Analysis and Memory usage

## Algorithmic Performance:
Given that the challenge was to generate trigrams from a given corpus, we know that at least every word must be read at least once, each word being represented by N. Since only O(1) operations we performed on the set N, we can assess this as a Linear time performing function, O(N). Or, as my old professor used to say "not bad". Aside from trivial optimizations, I don't see a way currently to improve run-time for a parser that has to read every word, but please leave a comment or issue if you come up with something

## Memory usage:
When first presented with the challenge, it's quite tempting to use one of the popular pre-built python libraries that can just do this for you, such as NLTK. While those are great and well documented, rarely do they take into account the memory usage that parsing massive (10g+) of data can do to ones resources. For those cases, loading the entire text into memory simply isn't an option. By using a deque, we're only using an amount of memory equal to size of the trigram dictionary + n words where n is the set size of gram we're looking to gather. So in other words, a very minimal amount. As you increase ngram set size you severely decrease likelihood of finding a matching gram, so even at larger gram sizes memory usage would not be a concern. 

## Additional performance thoughts:
There may be ways to split data and run in parallel, but I haven't investigated this past a small consideration yet.

## Improvements for the future

As you might have seen from my code, I left a lot of room for extensibility options in the future. The main improvements I had in mind were as follows:

1. Ability to specify the N in ngram, instead of just defaulting to three
	* In turn, this would look something like `python ngrams.py file.txt -n 4` and have an out put of quadrams
2. Ability to specify length of output list, instead of default top 100 occurrences
	* Similarly, this would look something like `python ngrams.py file.txt -l 55`
3. Ability to provide a range of N, and handle the output in a dictionary.
	* I already laid out almost all of the groundwork for this, one would need to take in arguments like so `python ngrams.py file.txt --min 2 --max 5`
4. Ability to get comparative of collapsed output for given input.
	* As I mentioned in the earlier section, right now it performs by collapsing since comparative could be generated by running the script more than once. However, it would be nice to add a flag that does it all in one run like so: `python ngrams.py file.txt --comparative`

While none of these are particularly challenging or unheard of, in the effort of the challenge and attempting to learn when to call some code "good", I did not include these features in this iteration. Given more time however, these would be quick on my to do list as they're already almost there.

## Sidenote

In my sample data set I've made use of King James' Bible and Exodus from the Tanakh due to their availability and ideal sizing. While these texts don't reflect my personal view, I ask that you be reverent and respectful when making use of them to keep our online community a supportive and welcoming place for everyone. Thank you! :) 
	
