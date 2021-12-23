import hub
from PIL import Image
import argparse


def load_dataset_hub(path_dataset: str):
    ds = hub.load(path_dataset, read_only=True)
    W = ds.images[0].numpy()  # Fetch an image and return a NumPy array
    X = ds.labels[0].numpy(aslist=True)  # Fetch a label and store it as a
    Y = ds.boxes[0].numpy()
    Z = ds.tensors.keys()
    print("All tensors  = {}".format(Z))
    print("First image classes = ", X)
    print("First image boxes = ", Y)
    print("Will save first image locally at path 'test.jpg'")
    # Save first image locally
    im = Image.fromarray(W)
    im.save("test.jpeg")
    print("Create torch dataloader")
    dataloader = ds.pytorch()
    print("len dataloader = {}".format(len(dataloader)))
    print("first item = {}".format(next(iter(dataloader))))
    return



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load a mocked dataset on Activeloop Hub"
    )
    parser.add_argument(
        "--path",
        type=str,
        help="path of dataset e.g. s3://myBucket/myDataset",
    )
    args = parser.parse_args()
    load_dataset_hub(args.path)