
this project aims for only Ludwig CLI ( yaml file )
Data set was taken from

 https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment?resource=download

  - run python -m spacy download en (NLP en_core_web_sm)

  
> Commands : 
> ludwig train --dataset "Twitter US Airline Sentiment\Tweets.csv" --config "Twitter US Airline Sentiment\config.yml" --output_directory "Twitter US Airline Sentiment\results"

>  ludwig predict --dataset <input_dataset> --model_path <model_path> --output_directory <output_directory>


> ludwig visualize --visualization learning_curves --training_statistics ratings_sample.meta.json


>git push --force origin main


ludwig train --dataset "Twitter US Airline Sentiment\Tweets.csv" --config "Twitter US Airline Sentiment\config.yml"