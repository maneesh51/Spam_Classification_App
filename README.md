# Spam_Classification_App

### App link: https://share.streamlit.io/maneesh51/spam_classification_app/main/spamclassify_app.py

### Information:
1. This app is part of the Udemy course projects (https://www.udemy.com/course/complete-natural-language-processing-nlp-with-spacy-nltk/), data file spam.tsv is provided within the course.
2. Models used in the app: RandomForest Classifier and Support Vector Machine (SVM). 


### Tips:
1. Generate requirement.txt file using command 'pipreqs' in Conda prompt in the project directory.
2. While uploading the app on streamlit.io, if the following error appears 
```python
AttributeError: module ‘click’ has no attribute ‘get_os_args’
``` 
then add 'click==7.1.2' in the requirement file. Some dependancy issue in streamlit backend.

3. Since this app make use of loading previously saved model using pickle, always add scikit_learn version, even if not importing the library. Here, i'm using scikit_learn==1.0.2



