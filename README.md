Hi !

This test has been designed to prove your knowledge of Python, Django and Docker.

# Youtube Clone

In this project you can list and enter a series of videos, you have been asked to add the following features:

- Create the URL "/popular/" to show the five most popular videos, based on the following rules:
 - Likes add 10 points of popularity
 - Dislikes subtract 5 points of popularity
 - Comments add 1 point of popularity
 - Today videos are 100 points of popularity worth than yesterday's videos
 - In case that all videos have the same popularity points, choose five videos at random.
 - include only the videos of the current month. If there aren't any new videos, pick five videos at random.
 - This website is on fast-growing, think on a scalable solution

example:
  Today video with 2 likes and 1 dislike, and 1 comments -> 116
  Yesterday video with 2 likes and 1 dislike, and 1 comments -> 16

- Create the URL "/history/" to show the videos that the logged user has seen, ordered from new to old, paginated by 10.
- Build the test you consider necessary to test /popular/ and /history/

You are also being asked to fix any issues that you find on any files of this project (we deliberately added quite a few)

# Clarifications

* You can create, modify and delete any Django app that you consider necessary
* You can add or remove any library you want
* In fact, you can add, edit or delete any file on this project (excluding this one) at your will