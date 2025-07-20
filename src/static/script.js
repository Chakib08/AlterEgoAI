function previewImage(inputId, previewId) {
    const fileInput = document.getElementById(inputId);
    const preview = document.getElementById(previewId);
    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}

document.getElementById('user-image').addEventListener('change', () => {
    previewImage('user-image', 'user-preview');
});

document.getElementById('character-image').addEventListener('change', () => {
    previewImage('character-image', 'character-preview');
});

document.getElementById('generate-btn').addEventListener('click', async () => {
    const userImage = document.getElementById('user-image').files[0];
    const characterImage = document.getElementById('character-image').files[0];
    const promptText = document.getElementById('prompt').value;

    if (!userImage) {
        alert('Please upload at least your image.');
        return;
    }

    const formData = new FormData();
    formData.append('user_image', userImage);
    formData.append('character_image', characterImage);
    formData.append('prompt', promptText);

    document.getElementById('loading-bar').style.display = 'block';
    document.getElementById('result').innerHTML = '';

    // Fake progress bar animation
    let progress = 0;
    const interval = setInterval(() => {
        progress += Math.random() * 5;
        if (progress >= 100) progress = 99;
        document.getElementById('progress').value = progress;
    }, 500);

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            body: formData
        });

        const imageUrl = await response.text();
        document.getElementById('result').innerHTML = `
            <img id="result-img" src="${imageUrl}" alt="Result Image">
            <br>
            <a id="download-btn" href="${imageUrl}" download="alter_ego_result.png">
                <button>Download Image</button>
            </a>`;
    } catch (error) {
        console.error('Error:', error);
        alert('Something went wrong. Please try again.');
    } finally {
        clearInterval(interval);
        document.getElementById('progress').value = 100;
        document.getElementById('loading-bar').style.display = 'none';
    }
});
