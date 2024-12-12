import io
from dotenv import load_dotenv
import os
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

load_dotenv(dotenv_path='..\\Data\\.env')

DREAMSTUDIO = "sk-9CNBobKWFvZj2obR6uXUM0YrRdcKWotn8U590KcbrLZeF4Os"

def generate_image(text):
    stability_api = client.StabilityInference(
        key=DREAMSTUDIO,
        verbose=True,
    )

    # The object returned is a Python generator
    answers = stability_api.generate(
        prompt=text,
        seed=95456,  # if provided, specifying a random seed makes results deterministic
    )

    print("Generator created. Iterating over responses...")

    # Iterating over the generator produces the API response
    response_found = False
    for resp in answers:
        print(f"Processing response: {resp}")
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                print("WARNING: Your request activated the API's safety filters and could not be processed."
                      "Please modify the prompt and try again.")
                return
            elif artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.show()
                response_found = True

    if not response_found:
        print("No valid image response received.")