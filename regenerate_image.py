Install the replicate Python client from PyPI:
pip install replicate


Next, grab an API token and authenticate by setting it as an environment variable:
export REPLICATE_API_TOKEN=[token]
Then run the model with just a few lines of code:

import replicate

model = replicate.models.get("tencentarc/gfpgan")
version = model.versions.get("9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3")

# https://replicate.com/tencentarc/gfpgan/versions/9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3#input
inputs = {
    # Input
    # 'img': open("path/to/file", "rb"),

    # GFPGAN version. v1.3: better quality. v1.4: more details and better
    # identity.
    'version': "v1.4",

    # Rescaling factor
    'scale': 2,
}

# https://replicate.com/tencentarc/gfpgan/versions/9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3#output-schema
output = version.predict(**inputs)
print(output)