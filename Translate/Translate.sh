curl --request POST \
	--url https://deep-translate1.p.rapidapi.com/language/translate/v2/detect \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: deep-translate1.p.rapidapi.com' \
	--header 'x-rapidapi-key: fef69584e6mshd2e29999cb26812p1a1d9ejsn3e42430982a0' \
	--data '{"data":{"detections":[{"language":"en","isReliable":false,"confidence":0.9867512}]}}'