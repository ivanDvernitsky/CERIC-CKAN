#!/usr/bin/env python
import urllib.request, urllib.error
import json
import pprint

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    'name': 'Actors',
    'notes': 'A dataset of different actors',
    'owner_org': 'Atlantic Records'
}

# Use the json module to dump the dictionary to a string for posting.
data_string = urllib.request.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
request = urllib.request.urlopen('http://127.0.0.1:5000/api/action/package_create')

# Creating a dataset requires an authorization header.
# Replace *** with your API key, from your user account on the CKAN site
# that you're creating the dataset on.
request.add_header('Authorization', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJZMTl4X2F5VDFnYTVQaWVadzFLR0FxamFWQ19OR1FycThJZTVYOVY5RmdNIiwiaWF0IjoxNzE1ODcwOTc4fQ.9vycTJ-h6rX_LGvPWn76iK9sAqjaAl973gEvbwEi_A0')

# Make the HTTP request.
response = urllib.request.urlopen(request, data_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)