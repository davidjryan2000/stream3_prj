#!/bin/sh
echo Configuring Environment Variables
export SECRET_KEY='ejc8=ez6qy+!i+^rb79s4cq8tk8&o!%z_3y8m*d@p469e4rrrv'
export DEBUG=True

export STRIPE_PUBLISHABLE_KEY='pk_test_HpjDh6Lu6A27SgKH90ANgPuY'
export STRIPE_SECRET_KEY='sk_test_9gmvzCpJrxorHGFMrqveMcYn'
export DATABASE_URL="postgres://ljtlursdqntalk:55f80030751603ba8a6c08813315676c190627412859b5ec16f10f14dfac6b63@ec2-54-75-227-173.eu-west-1.compute.amazonaws.com:5432/d6eun1cbhqm9eh"
export AWS_STORAGE_BUCKET_NAME=stream3-prj
export AWS_ACCESS_KEY_ID=AKIAJORL5RQQD6IBRJHA
export AWS_SECRET_ACCESS_KEY=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
echo Done
