import hub
import numpy as np
import argparse

annotations = {
    "data/2007_000039.jpeg": {
        "boxes": np.array([
            [
                0.31745737145347974,
                0.2709116400262058,
                0.42709666265213847,
                0.3691519874522164,
            ]
        ]),
        "labels": np.array([0.0]),
    },
    "data/2007_000042.jpeg": {
        "boxes": np.array([
            [0.0, 0.1247451524766171, 0.4770627739385478, 0.5194391814168501],
            [
                0.5184322952653565,
                0.12315034858961282,
                0.4815677047346435,
                0.5227269925511222,
            ],
        ]),
        "labels": np.array([1.0, 1.0]),
    },
    "data/2007_000061.jpeg": {
        "boxes": np.array([
            [
                0.35329217055746265,
                0.23641575039164037,
                0.20164142165921306,
                0.08232164809842311,
            ],
            [
                0.5517103649478234,
                0.16771213424856113,
                0.32244594477748206,
                0.5319518540333844,
            ],
        ]),
        "labels": np.array([2.0, 2.0]),
    },
}
class_names = ["Computer", "Train", "Boat"]

def export_dataset_hub(path_dataset: str):
    ds = hub.empty(path_dataset, overwrite=True)  # Create the dataset
    with ds:
        ds.create_tensor("images", htype="image", sample_compression="jpeg")
        ds.create_tensor("labels", htype="class_label", class_names=class_names)
        ds.create_tensor("boxes", htype="bbox")

        for fn_img, annotations_image in annotations.items():
            # Get the arrays for the bounding boxes and their classes
            boxes, labels = annotations_image["boxes"], annotations_image["labels"]
            # Append data to tensor)s
            ds.images.append(hub.read(fn_img))
            ds.labels.append(labels.astype(np.uint32))
            ds.boxes.append(boxes.astype(np.float32))

        # This line causes an issue
        # Comment the following line to avoid errors when loading the dataset
        ds.commit("test")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Export a mocked dataset on Activeloop Hub"
    )
    parser.add_argument(
        "--path",
        type=str,
        help="path of dataset e.g. s3://myBucket/myDataset",
    )
    args = parser.parse_args()
    export_dataset_hub(args.path)
