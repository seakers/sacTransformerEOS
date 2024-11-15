import json
import sys
import argparse
import traceback

from classes.sac import SoftActorCritic
from classes.utils import DataFromJSON
from classes.client import Client

if __name__ == "__main__":
    try:
        # Gather the arguments
        argparse = argparse.ArgumentParser()

        argparse.add_argument("--host", default="localhost", type=str, help="Host address.")
        argparse.add_argument("--port", default=5555, type=int, help="Port number.")

        args = argparse.parse_args()

        # Create agent
        client = Client(gym_host=args.host, gym_port=args.port)

        # Load the configuration file
        with open(f"{sys.path[0]}\\sacConfiguration.json", "r") as file:
            config = json.load(file)

        # Create configuration object
        conf = DataFromJSON(config, "configuration")

        # Create the SAC algorithm
        sac = SoftActorCritic(conf, client)

        # Train the agent
        sac.train()
    
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

    finally:
        sac.client.shutdown_gym()
        