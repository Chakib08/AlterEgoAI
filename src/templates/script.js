document.querySelectorAll('.drop-zone').forEach(zone => {
    const input = zone.querySelector('input');

    zone.addEventListener('click', () => input.click());

    zone.addEventListener('dragover', (e) => {
        e.preventDefault();
        zone.classList.add('hover');
    });

    zone.addEventListener('dragleave', () => {
        zone.classList.remove('hover');
    });

    zone.addEventListener('drop', (e) => {
        e.preventDefault();
        zone.classList.remove('hover');

        if (e.dataTransfer.files.length > 0) {
            input.files = e.dataTransfer.files;
        }
    });
});

document.getElementById('generate-btn').addEventListener('click', async () => {
    const userImage = document.getElementById('user-image').files[0];
    const characterImage = document.getElementById('character-image').files[0];

    if (!userImage || !characterImage) {
        alert('Please upload both images.');
        return;
    }

    const formData = new FormData();
    formData.append('user_image', userImage);
    formData.append('character_image', characterImage);

    document.getElementById('loading').style.display = 'block';
    document.getElementById('result').innerHTML = '';

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            body: formData
        });

        const imageUrl = await response.text();  // Expecting backend to return a URL or image blob

        document.getElementById('result').innerHTML = `<img src="${imageUrl}" alt="Result Image">`;
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while generating the image.');
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
});
