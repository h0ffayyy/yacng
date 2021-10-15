# YACNG (Yet Another Code Name Generator)

Flask application that generates a random single-word code name for projects, incidents, etc.

Demo: TBD

## Wordlists

To add your own custom wordlist, just add the file to `static/wordlists`. Use one word per line.

## Docker

To run the app in Docker, first clone the repository:

`git clone https://github.com/h0ffayyy/yacng.git`

Build the image:

`docker built -t yacng .`

Run the container:

`docker run -p 5000:5000 yacng`