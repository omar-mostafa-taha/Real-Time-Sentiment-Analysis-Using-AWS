import boto3
import json

sagemaker_runtime = boto3.client('sagemaker-runtime')

# Function to invoke the SageMaker endpoint
def lambda_handler(event, context):
    # Get input from the event (you pass the input text in the event body)
    input_text = event.get('text', '')

    if not input_text:
        return {
            'statusCode': 400,
            'body': json.dumps('No input text provided')
        }

    # Prepare the payload for SageMaker (following your model's input format)
    payload = {"inputs": input_text}
    
    # Your SageMaker endpoint name
    endpoint_name = 'huggingface-pytorch-inference-2024-10-12-15-02-29-742'  

    # Invoke the SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',
        Body=json.dumps(payload)
    )

    # Parse the response from SageMaker
    result = json.loads(response['Body'].read().decode())

    # Extract the first label and score from the result
    prediction = result[0]  # Assuming the result is a list with at least one item
    label = prediction.get('label', 'Unknown')
    score = prediction.get('score', 0)

    # Map labels to "positive" or "negative"
    if label == 'LABEL_1':
        sentiment = 'positive'
    elif label == 'LABEL_0':
        sentiment = 'negative'
    else:
        sentiment = 'unknown'

    # Format a user-friendly response
    formatted_result = {
        'Sentiment': sentiment,
        'Confidence': round(score * 100, 2)  # Convert to percentage
    }

    # Return the formatted prediction result
    return {
        'statusCode': 200,
        'body': formatted_result
    }
