async function translateText() {
    const apiKey = fef69584e6mshd2e29999cb26812p1a1d9ejsn3e42430982a0; // Replace with your API key
    const sourceText = document.getElementById('sourceText').value;
    const targetLanguage = document.getElementById('targetLanguage').value;

    if (!sourceText) {
        alert('Please enter text to translate.');
        return;
    }

    const url = `https://translation.googleapis.com/language/translate/v2?key=${apiKey}`;
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                q: sourceText,
                target: targetLanguage,
            }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('Error:', errorData);
            document.getElementById('translatedText').innerText = `Error: ${errorData.error.message}`;
        } else {
            const data = await response.json();
            document.getElementById('translatedText').innerText = data.data.translations[0].translatedText;
        }
    } catch (error) {
        console.error('Fetch error:', error);
        document.getElementById('translatedText').innerText = `Fetch error: ${error.message}`;
    }
}
