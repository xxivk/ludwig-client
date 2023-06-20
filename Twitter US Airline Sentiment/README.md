
this project aims for only Ludwig CLI ( yaml file )
Data set was taken from
Analyze how travelers in February 2015 expressed their feelings on Twitter
A sentiment analysis job about the problems of each major U.S. airline. Twitter data was scraped from February of 2015 and contributors were asked to first classify positive, negative, and neutral tweets, followed by categorizing negative reasons (such as "late flight" or "rude service").


 https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment?resource=download

  - run python -m spacy download en (NLP en_core_web_sm)

  
> Commands : 

Train command 
> ludwig train --dataset "Twitter US Airline Sentiment\Tweets.csv" --config "Twitter US Airline Sentiment\config.yml" --output_directory "Twitter US Airline Sentiment\results"

>  ludwig predict --dataset <input_dataset> --model_path <model_path> --output_directory <output_directory>

Predict command 
> ludwig predict --dataset "Twitter US Airline Sentiment\Tweets.csv" –-model_path "Twitter US Airline Sentiment\results\experiment_run_0\model" --output_directory "Twitter US Airline Sentiment"

Vis Command
> ludwig visualize --visualization learning_curves --training_statistics "Twitter US Airline Sentiment\results\experiment_run_0\training_statistics.json"


>git push --force origin main


ludwig train --dataset "Twitter US Airline Sentiment\Tweets.csv" --config "Twitter US Airline Sentiment\config.yml" --output_directory "Twitter US Airline Sentiment\results"
