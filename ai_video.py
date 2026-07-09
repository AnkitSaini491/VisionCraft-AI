import os
import replicate

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

def generate_video(prompt):

    output = replicate.run(

        "kwaivgi/kling-v1.6-pro",

        input={
            "prompt": prompt
        }

    )

    return output
