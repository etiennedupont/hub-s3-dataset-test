# Hub error reproduction code

## Usage

- `pip install -r requirements.txt`
- `python export_yolo_dataset_mocked.py --path s3://my-bucket/my-dataset` you can choose any path within a s3 bucket that you have access to
- `python load_dataset.py --path s3://my-bucket/my-dataset`

## Comments

- The line that causes the issue is highlighted in "export_yolo_dataset_mocked.py"
- The error I received is the following

```
KeyError: NoSuchKey('An error occurred (NoSuchKey) when calling the GetObject operation: The specified key does not exist.')
```

- Also, after importing, the datasets are either not visible or visible with impossibility to view the images on "https://app.activeloop.ai/". This also applies with the error line commented in "export_yolo_dataset_mocked.py"