# Sentiment Analysis of IMDB Movie Reviews
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg">

## Context:

IMDB dataset having 50K movie reviews for natural language processing or Text analytics. This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training and 25,000 for testing. So, predict the number of positive and negative reviews using either classification or deep learning algorithms. For more dataset information, please go through the following link, http://ai.stanford.edu/~amaas/data/sentiment/

## Dataset:

https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

## What is Natural Language Processing?
<p>Natural Language Processing (NLP) is a computer programming ability to understand human language. NLP is a component of Artificial Intelligence (AI). Developing NLP is really a challenging problem for Computer Programmer. NLP follows some important conceptual mathematical statements and formulas for understanding the human language. I will be explained below that math behind NLP and how NLP actually works.You will see much time and also use this in your daily life, Google Assistant is one of the most popular NLP implementations, when you speak in front of your mobile, google assistant detecting your voice with the help of NLP. Syntactic analysis and semantic analysis are the main techniques used to complete Natural Language Processing tasks.</p>

## Converting Text into Vector:
<pre>
Converting Text into a vector is the first and most important techniques in NLP. Before explaining this let me give you an example for your better understanding. Suppose I have a dataset with three lines it like this 
R1 - This food is tasty 
R2 - This food is tasty and affordable
R3 - This food is not affordable and not so much tasty
So after reading this dataset, you will understand that R1 & R2 is very much similar than R1 & R3. So then we can write (R1, R2) > (R1, R3). Now if I put this into D- Dimensional space we can say that vector of  R1 and R2 must be closure than R1 and R3, and also if the reviews are similar then the distance will smaller, this process is called Simulation. This is the reason why text converted into Vector.
</pre>

## Data Cleaning:

<ul>
  <li>Bag of words</li>
  <li>Removing Stopwords</li>
  <li>Lower Case</li>
  <li>Stemming</li>
  <li>Lemmitization</li>
  <li>TF IDF</li>
  <li>Word2Vector</li>
 </ul>
 
