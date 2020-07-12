import pandas as pd
import os
from sklearn.model_selection import train_test_split
import argparse


def generate_split(original, mix, output_dir, ratio=None):
    labels = pd.read_csv(original)
    all_labels = pd.read_csv(mix)

    # shuffle dataframe
    shuffled_df = labels.sample(frac=1, random_state=42)

    # do a Stratify split
    train_df, val_df, _, _ = train_test_split(shuffled_df, shuffled_df['class'],
                                              stratify=shuffled_df['class'],
                                              test_size=float(ratio),
                                              random_state=42)

    train_df.reset_index(drop=True, inplace=True)
    aug_df = all_labels.loc[all_labels.filename.str.startswith(
        'aug_')].reset_index(drop=True)

    # merge augmented and train splot of original images

    training_df = pd.concat([train_df, aug_df])
    training_df = training_df.sample(
        frac=1, random_state=42).reset_index(drop=True)
    training_df.to_csv(f'{output_dir}/training.csv', index=None)

    val_df.reset_index(drop=True, inplace=True)
    val_df.to_csv(f'{output_dir}/validation.csv', index=None)
    print("Files created")


def main():
    parser = argparse.ArgumentParser(
        description="Create Training and Validatin splits")
    parser.add_argument("-og", "--original",
                        help="csv file of original images")
    parser.add_argument("-m", "--mix",
                        help="csv file of original and augmeneted images")
    parser.add_argument("-r", "--val_size",
                        help="sizeof validation dataset ")

    parser.add_argument("-o", "--output_dir",
                        help="Name of output directory")

    args = parser.parse_args()
    generate_split(args.original, args.mix, args.output_dir, args.val_size)


if __name__ == "__main__":
    main()
