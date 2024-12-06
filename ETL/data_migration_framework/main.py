import yaml
from src.migration_tests import test_data_migration

if __name__ == "__main__":
    with open("config/config.yaml") as file:
        config = yaml.safe_load(file)

    results = test_data_migration(config['source'], config['target'], config['validation_criteria'])
    for criterion, passed in results.items():
        print(f"{criterion}: {'PASSED' if passed else 'FAILED'}")
