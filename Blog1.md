# Kitchen Nightmare with Data Science and a Web App -- Part 1

In the very first Chipy (Chicago Python User Group) meeting that I attended, there were ten lightening talks on learning various aspects of Python. Each of them was given by a mentee in the ChiPy Mentorship Program. I was very surprised by the amount work put into this program by both mentees and and mentors. Since I am a newbie in the data science field and my goal is to dive deep, I decided to apply as a mentee. Luckily I got selected, and this is the first post about my experience as a mentee.

I have been working on my capstone project, which is part of the Data Science Immersive Program at General Assembly that I recently graduated from. Intrigued by my wondering why a restaurant I liked in Arlington Heights was permanently closed, my capstone project is dedicated to building a model that can predict restaurant failures in the near future. With what I have learned about Python at General Assembly, I collected data of permanently closed restaurants and open restaurants from Yelp and built a predictive model around it. Since the model still needs some fine-tuning, I am not going through the details of the model here. Knowing that I wanted to further extend this project even after my graduation, what I hoped to learn from the mentorship program is how to make a web app that returns the prediction of my model given the information of a restaurant.

Luckily I got to work with my mentor, Matt, who has expertise in Web application with Python. In the first meeting with him, I told him about my project and my idea of building a web app out of it, and we quickly decided that that is our project for the Chipy mentorship program. He also shared with me his own experience of learning this stuff himself. In addition to the web app, we also set other goals: improving my skills with Git, database/SQL, and general computer science/software engineering stuff.

So, first off, reading! Matt sent me a bunch of webpages and videos to get an idea about things like what DNS is, what 
## 1. Overview

Intrigued by wondering why a restaurant I liked in Arlington Heights was closed, this project is dedicated to build a model to predict whether a restaurant will be closed in the near future. The model is built on data of permanently closed restaurants and open restaurants obtained from Yelp.com.

## 2. Data Collection
To build a classification model for predicting closed restaurants and open restaurants, data of both sides should be obtained. While webpages of closed restaurants are not explicitly returned via the search under Yelp, they do exist on Yelp.com still. With the name of a closed restaurant given, its Yelp webpage can be accessed through an url in the form of https://www.yelp.com/biz/restaurant_name-chicago. Therefore, names of closed restaurants reported from the following three sources were used to create Yelp urls from which data were collected via the Request library in Python.
1. http://www.gayot.com/closed-restaurants/chicago-area.html
2. http://www.chicagotribune.com/redeye/redeye-closed-bars-and-restaurants-2016-20161228-story.html
3. http://www.chicagotribune.com/redeye/redeye-chicago-closed-bars-and-restaurants-2015-20160104-photogallery.html

### 2.1 Assumptions
#### 2.1.1 Time-wise
The same time window was intended for the inclusion of open and permanently closed restaurants in the data set. Since the date when a restaurant is opened or permanently closed for business is not recorded on Yelp webpages, the dates of the first review and last review were used to approximate those, respectively. A time window of 2012 to 2017 was set for the inclusion of the permanently closed restaurants. That is, for the closed restaurants reported from the three sources above, only those closed between 2012 and 2017 were considered. For fair comparison, only restaurants opened since 2010/01/01 till today are eligible as open restaurants in the data set to contrast with permanently closed restaurants that existed between 2010 till 2012, if any. Therefore, restaurants open today that have their first reviews later than 2010/01/01 were excluded as open restaurants in the data set. Only restaurants that have been reviewed were considered, otherwise the date when a restaurant was opened or permanently closed for business could not be approximated.

#### 2.1.2 Location-wise
The same neighborhoods were intended for the inclusion of open and permanently closed restaurants in the data set. Once the permanently closed restaurants were collected, the distribution of their neighborhoods were recorded. Open restaurants were then sampled from the distribution, in addition to the constraint on their first review dates mentioned above.

### 2.2 Predictors
For each restaurant, the following features were considered as binomial categorical predictors: whether it is claimed by the owner, whether it has a website, accepts credit cards, good for groups, good for kids, takes reservations, outdoor seating, take-out,  delivery, and whether it has TV. The following features were considered as polynomial categorical predictors: category, neighborhood, price range, attire (dressy, formal, casual), parking (garage, street, valet, validated, private lot), alcohol (no, full bar, beer & wine only), noise level (loud, very loud, quiet, average), and Wi-Fi (no, paid, free).

For a given restaurant, the date, star, and text of each review was included in the data set. For the model to be predictive, three time periods (13, 26, and 52 weeks) were set as "block weeks". The block weeks were used to exclude reviews within the last 13, 26, and 52 weeks for a given restaurant for the models to predict whether restaurant will survive in the next 13, 26, and 52 weeks, respectively. The remaining reviews were used to calculate the average number of reviews per year, average rating, and ratings for 5-, 4-, 3-, 2-, 1- star, as numerical predictors.

In addition, Vader sentiment analysis was performed on the text of each remaining review, and the compound and subjectivity scores were calculated. The average compound score, and subjectivity score were also calculated as numerical predictors for each restaurant. To investigate the predicting power of the reviews within a time period before the "block weeks", three time periods (26, 52, and 78 weeks) before the "block weeks" were set as "open weeks". During the "open weeks", linear regressions were performed for ratings, compound scores, and subjectivity scores, respectively, for the reviews in that period. The intercepts and coefficients of rating, compound score, and subjectivity score were also included as numerical predictors. In total, nine data sets were created for different combinations of block weeks and open weeks.

## 3. Model

The voting classifier was employed as the model that contains logistic regression, random forest, and gradient boosted trees. GridSearchCV was also employed to explore the parameter space with cross validation. Accuracy scores and best parameters were recorded. The accuracy scores were used to measure the success of a model.

## 4. Results
While the base line in test set is 0.729, the mean accuracy for 13, 26, and 52 "block weeks" models are 0.863, 0.863, and 0.860, respectively. For models that have the same "block weeks", the span of the accuracy is less than 0.03 for models with different "open weeks". This indicates that the reviews within the "open weeks" do not reinforce the predicting power of the model. Moreover, the predicting power of models to predict whether a restaurant will survive in the next 26, 52, and 78 weeks do not differ with each other significantly.

## 5. Future Work
The neural network modeling technique will be used to increase the accuracy score. In the current model, only neighborhoods are included to study the effect of the location on the failure of a restaurant. If the information of how many restaurants have existed in the past ten years for a specific restaurant location, then a model can be constructed to predict the restaurant failure for a specific location.
