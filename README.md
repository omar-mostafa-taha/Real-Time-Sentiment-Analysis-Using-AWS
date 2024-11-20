# Real-Time-Sentiment-Analysis-Using-AWS
## Request Flow
![Request Flow](https://github.com/omar-mostafa-taha/Real-Time-Sentiment-Analysis-Using-AWS/blob/ff2d99a108d5e11f68c9aa5abfa04633c917779d/Images/Request%20Flow.jpg)
This diagram illustrates the architecture for the sentiment analysis system. It highlights the following workflow:

* User Request: The user sends a request to the system.
* API Gateway: Manages the endpoints and forwards the request to the appropriate Lambda function.
* AWS Lambda: Executes the serverless function, which invokes the SageMaker endpoint for real-time inference.
* SageMaker Endpoint: Processes the data and returns the sentiment prediction.
* AWS S3: Stores the trained model.
* Response: The prediction is returned to the user as a JSON file.
## Model Performance
![Test Results](https://github.com/omar-mostafa-taha/Real-Time-Sentiment-Analysis-Using-AWS/blob/8ce558598572397a5377466b80b0b2e49d04d6a5/Images/Test%20Results.jpg)
## API Testing
![Testing API on Postman](https://github.com/omar-mostafa-taha/Real-Time-Sentiment-Analysis-Using-AWS/blob/8ce558598572397a5377466b80b0b2e49d04d6a5/Images/API%20Testing.png)

