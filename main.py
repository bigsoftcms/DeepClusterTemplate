# import your packages

# do not rename the functions
def main(dataset_path, output_path):
    print("start running training job")
    config_path = "./config.yaml"
    # invoke your training function


# to test your code locally, you can either run main.py directly
# such as "python main.py --output_path=<path>"
# or ddlcli localrun --output_path=<path>
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--output_path',
        type=str,
        required=True,
        help='Path where job should output to')    
    
    FLAGS, _ = parser.parse_known_args()
    main(FLAGS.dataset_path, FLAGS.output_path)