# Resolvr: An app to query Wikidata with IDs

Resolvr is a lightweight Flask app where you can query Wikidata using existing IDs for entities from linked data services (LoC, FAST, Getty, etc.). Instead of having to reconcile labels, and/or to avoid that reconciliation being a fallback as in [OpenRefine](https://github.com/OpenRefine/OpenRefine/wiki/Reconciliation#reconciling-via-unique-identifiers), you can resolve your IDs to Wikidata, and if it exists, the Wikidata URI will be brought back. That's it!  

## Use case

The use of this app comes in when you have semi-structured data already. You have entities with IDs already, and want to grab the Wikidata URIs. You do not want fuzzy matching or matching on labels. You are simply making a query based on your IDs to query, and it is either there or not.   

Resolution is typically done after you have reconciled entities, or you just happen to have them at hand from past cataloging/description. For instance, many cataloged books at some point have FAST IDs. Or maybe you have already reconciled a list of topics to FAST, and you want to query those FAST IDs against Wikidata.    

## Setting Up Your Environment

### Using Anaconda (Preferred)

Create the `conda` environment using the environment yml, `flaskdev.yml`: 
```shell
$ conda env create -f flaskdev.yml
```
Then as usual, activate the environment:  
```shell
$ conda activate flaskdev
```

## How to run Resolvr

After setting up the environment and activating it, `cd` into the `/resolvr/` directory. Export the Flask environment variable: 
```shell
$ export FLASK_APP=resolvr.py
```

Finally, serve the app by typing `flask run`. It will run on localhost
