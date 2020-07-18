- (5 Points) How is this project structure  
  different than a Flask (or Node) application? What role are the urls.py and views.py files responsible for?

ANSWER: urls.py is responsibe for the url paths and in passing data from the view to the url. While views.py take care of the template information and passing that data to urls. Key difference between flask and django is that its much easier to get started on flask but for scalability django would get the upperhand

- (5 Points) Why do we use 2 separate urls.py files? How do they interact?

ANSWER: The root project's urls.py is taking care of directing the url to the app and inside of the app you have another urls.py that controls the views within.

- (5 Points) When is it desirable to split our code over multiple apps? Why would we want to do so?

ANSWER: The reason to have our code split over multiple apps for easier reuasbility, and most importantly because every app is a different components of the project for example an online store might be split into cart, reviews and customers
