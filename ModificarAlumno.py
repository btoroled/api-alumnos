import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    alumno_datos = event['body']['alumno_datos']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression='SET alumno_datos = :datos',
        ExpressionAttributeValues={':datos': alumno_datos},
        ConditionExpression='attribute_exists(alumno_id)',
        ReturnValues='ALL_NEW'
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'alumno': response['Attributes']
    }
