# Real-Time-Sentiment-Analysis-Using-AWS
This project focuses on building and deploying a real-time sentiment analysis system using machine learning and cloud technologies. The pretrained model (DistilBERT) is fine-tuned on the IMDB dataset to classify user reviews as positive or negative. It achieved an accuracy of 93%.
![Request Flow](https://github.com/omar-mostafa-taha/Real-Time-Sentiment-Analysis-Using-AWS/blob/ff2d99a108d5e11f68c9aa5abfa04633c917779d/Images/Request%20Flow.jpg)
This diagram illustrates the request flow and amazon services used in the project. It highlights the following workflow:

* User Request: The user sends a request to the system.
* API Gateway: Manages the endpoints and forwards the request to the appropriate Lambda function.
* AWS Lambda: Executes the serverless function, which invokes the SageMaker endpoint for real-time inference.
* SageMaker Endpoint: Processes the data and returns the sentiment prediction.
* AWS S3: Stores the trained model.
* Response: The prediction is returned to the user as a JSON file.
