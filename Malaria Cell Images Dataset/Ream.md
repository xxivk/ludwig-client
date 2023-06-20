The dataset contains 2 folders

Infected
Uninfected
And a total of 27,558 images.
Acknowledgements
This Dataset is taken from the official NIH Website: https://ceb.nlm.nih.gov/repositories/malaria-datasets/
And uploaded here, so anybody trying to start working with this dataset can get started immediately, as to download the
dataset from NIH website is quite slow.
Photo by Егор Камелев on Unsplash
https://unsplash.com/@ekamelev

Inspiration
Save humans by detecting and deploying Image Cells that contain Malaria or not!

#python create_dataset.py -p `pwd` -n malaria_cells.csv


>generate  image folders names  to CSV for Ludwig 

python "c:\Users\crypto\Desktop\ludwig-client\Malaria Cell Images Dataset\create_dataset.py" -p "Malaria Cell Images Dataset" -n malaria_cells.csv

ludwig train --dataset "Twitter US Airline Sentiment\Tweets.csv" --config "Twitter US Airline Sentiment\config.yml" --output_directory "Twitter US Airline Sentiment\results"

ludwig train --data_train_csv malaria_cells_train.csv --data_test_csv malaria_cells_validation.csv --model_definition_file model_definition.yaml --output_directory result_demo
